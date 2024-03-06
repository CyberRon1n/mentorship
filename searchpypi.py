#import requests,sys,webbrowser,bs4

#print('searching.....')

#search_query=' '.join(sys.argv[1:])

#res=requests.get('https://google.com/search?q='+ search_query)

#res.raise_for_status()

#soup = bs4.BeautifulSoup(res.text, 'html.parser')

#linkelems = soup.select('.tF2Cxc a')

#numopen=min(5,len(linkelems))

#for i in range(numopen):
#    urltoopen= 'https://www.google.com' + linkelems[i].get('href')
#    print('Opening', urltoopen)
#    webbrowser.open(urltoopen)



import sys
from googlesearch import search
import webbrowser

print('searching.....')

search_results = search(' '.join(sys.argv[1:]), num=5, stop=5, pause=2)

for i, result in enumerate(search_results):
    print('Opening result {}: {}'.format(i + 1, result))
    webbrowser.open(result)

