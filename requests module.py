import requests
res=requests.get('https://automatetheboringstuff.com/files/rj.txt')

playfile=open('romeoandjuliet.txt','wb')
for chunk in res.iter_content(100000):
    playfile.write(chunk)

playfile.close()
