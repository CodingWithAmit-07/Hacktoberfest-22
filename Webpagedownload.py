import urllib.request

try:
    file = urllib.request.urlopen("https://www.techexploits.com/")
    content = file.read()
    
except urllib.error.HTTPError:
    print('The web page does not exist')
    exit()

f = open('myfile.html', 'wb')
f.write(content)
f.close()

