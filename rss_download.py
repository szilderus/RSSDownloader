import feedparser, requests, os, subprocess

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename
    
#mp3 feed - https://feeds.twit.tv/sn.xml

d = feedparser.parse('https://feeds.twit.tv/sn_video_hd.xml')
fileUrl = d.entries[0].id
print(fileUrl)

filename = fileUrl.split('/')[-1]
print(filename)

if not os.path.exists(filename) :
    #download file as 
    print('File %s doesn\'t exists. Downloading...' % (filename))
    
    # this only make sense for small files that fit into memory
    #r = requests.get(fileUrl, allow_redirects=True)
    #open(filename, 'wb').write(r.content)
    
    #this method is dividing download for chunks
    download_file(fileUrl)

print('File %s exists. Opening...' % (filename))

p = subprocess.run(['vlc', '%s' % (filename),'-f'])

print(p)


