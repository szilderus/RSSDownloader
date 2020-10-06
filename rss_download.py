import feedparser, requests, os


#https://feeds.twit.tv/sn.xml

d = feedparser.parse('https://feeds.twit.tv/sn_video_hd.xml')
fileUrl = d.entries[0].id
print(fileUrl)

filename = fileUrl.split('/')[-1]
print(filename)
r = requests.get(fileUrl, allow_redirects=True)

if not os.path.exists(filename) :
    #download file as 
    print('File %s doesn\'t exists. Downloading...' % (filename))
    open(filename, 'wb').write(r.content)

print('File %s exists. Opening...' % (filename))
os.system('vlc %s' % (filename))