from bs4 import BeautifulSoup, Comment
import urllib2
import re

r = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
soup = BeautifulSoup(r, "html.parser")

comment = soup.find(string=lambda text: isinstance(text, Comment))
comment = comment.split()
print comment

answers = []
for line in comment:
    expression = re.search('[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}', line)
    if expression is not None:
        answers.append(expression.group())

print answers

