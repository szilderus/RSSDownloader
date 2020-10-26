import feedparser, requests, os, subprocess, shlex, time
#mp3 feed - https://feeds.twit.tv/sn.xml

d = feedparser.parse('https://feeds.twit.tv/sn_video_hd.xml')
fileUrl = d.entries[0].id
print(fileUrl)

filename = fileUrl.split('/')[-1]
print(filename)

if not os.path.exists(filename) :
    #download file as 
    print('File %s doesn\'t exists.' % (filename))
else :
	print('File %s exists. Opening...' % (filename))

	command_line = "vlc /home/pi/RSSDownloader/%s -f" % (filename)
	args = shlex.split(command_line)

	#['vlc', '%s' % (filename),'-f']
	#p = subprocess.run(['vlc', '%s' % (filename),'-f'], capture_output=True, shell=True)
	p = subprocess.Popen(args)

	print(args)
	print(p.pid)
	wait_timeout_and_close(p, 1800)
