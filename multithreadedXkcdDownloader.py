import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startcomic, endcomic):
    for urlnumber in range(startcomic, endcomic):
        print('downloading page https://xkcd.com/',urlnumber)
        res = requests.get('https://xkcd.com/%s'%(urlnumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('could not find comic image.')

        else:
            comicurl = comicElem[0].get('src')
            print('Downloading image %s...'%(comicurl))
            res = requests.get('https:'+ comicurl)
            res.raise_for_status()

            imagefile = open(os.path.join('xkcd', os.path.basename(comicurl)),'wb')

            for chunk in res.iter_content(100000):
                imagefile.write(chunk)
            imagefile.close()

downloadthreads = []
for i in range(0, 140, 10):
    start = i
    end = i+9
    if start == 0:
        start = 1
    downloadthread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadthreads.append(downloadthread)
    downloadthread.start()

for downloadthread in downloadthreads:
    downloadthread.join()
print('done')
