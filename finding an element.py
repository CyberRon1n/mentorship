import bs4
examplefile = open('example.html')
examplesoup = bs4.BeautifulSoup(examplefile.read(), 'html.parser')
elems = examplesoup.select('#author')
print(type(elems))

print(len(elems))

print(str(elems[0]))

print(elems[0].getText())

print(elems[0].attrs)
