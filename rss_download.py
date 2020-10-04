import feedparser, requests, os

d = feedparser.parse('https://feeds.twit.tv/sn.xml')
mp3url = d.entries[0].id
print(mp3url)

filename = mp3url.split('/')[-1]
print(filename)
r = requests.get(mp3url, allow_redirects=True)

if not os.path.exists(filename) :
    #download file as 
    print('File %s doesn\'t exists. Downloading...' % (filename))
    open(filename, 'wb').write(r.content)

print('File %s exists. Opening...' % (filename))
os.system('vlc %s' % (filename))