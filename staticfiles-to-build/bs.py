#!/usr/bin/python3

"""
Use beautiful soup to change these gallery subsection of template (does not work on base atm
"""

lines=open('gallery.html.template').readlines()

html_doc=''.join(lines)


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

hrefs=soup.find_all('a')




for el in soup.find_all('a'):
    oldsource=el['href']
    parsed = str('"{% static'+' '+'"' +oldsource+'"'+ ' '+'%}"')
    el['href']=parsed[1:-1]

for el in soup.find_all('img'):
    oldsource1=el['src']
    parsed = str('"{% static'+' '+'"' +oldsource1+'"'+ ' '+'%}"')
    el['src']=parsed[1:-1]



print(soup.prettify())


#hrefs[1]['href']
