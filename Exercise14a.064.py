import requests

url = 'https:\w3schools.com\python\demopage.htm'
html_output = input('Name for html file: ')

req = requests.get(url, 'html.parser')

f = open(html_output, 'w')
f.write(req.text)
f.close()
