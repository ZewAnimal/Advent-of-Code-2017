from bs4 import BeautifulSoup, Comment
from collections import Counter
import urllib2

r = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
soup = BeautifulSoup(r, "html.parser")

for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
    if comment.strip() == 'find rare characters in the mess below:':
        comment = comment.next_sibling

rares = Counter(comment).most_common()

print [i[0].encode('ascii') for i in rares if i[1] < 100]
