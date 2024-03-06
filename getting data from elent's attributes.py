import bs4
soup= bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanelem = soup.select('span')[0]
print(str(spanelem))

print(spanelem.get('id'))

print(spanelem.get('some_nonexistent_addr') == None)

print(spanelem.attrs)

