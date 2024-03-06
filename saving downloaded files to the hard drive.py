import requests

res=requests.get('https://automatetheboringstuff.com/files/rj.txt')

res.raise_for_status()

playfile=open('romeoandjuliet.txt', 'wb')

for i in res.iter_content(100000):
    playfile.write(i)

playfile.close()
