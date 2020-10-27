import feedparser, requests, os, subprocess, shlex, time
#mp3 feed - https://feeds.twit.tv/sn.xml

def wait_timeout_and_close(proc, seconds):
    """Wait for a process to finish, or raise exception after timeout"""
    start = time.time()
    end = start + seconds
    interval = min(seconds / 1000.0, .25)

    while True:
        result = proc.poll()
        if result is not None:
            return result
        if time.time() >= end:
            proc.kill()
            #raise RuntimeError("Process timed out")
        time.sleep(interval)
        
        
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
