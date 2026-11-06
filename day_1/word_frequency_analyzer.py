import re

text = """
Python is powerful.
Python is easy to learn.
Programming with Python is interesting.
Learning programming requires practice.
"""

"""Convert everything to lowercase.
Remove punctuation.
Count each word.
Find the most frequently occurring word.
Sort words by frequency, highest first. For ties, sort alphabetically."""
d={}
print(text.lower())
cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
words = cleaned_text.split()
d = {}
highest=0
higheest_word=''
for word in words:
    if word in d:
        d[word]+=1
    else:
        d[word]=1
print(d)
for key,value in d.items():
    if value>highest:
        highest=value
        higheest_word=key
print(higheest_word)

print((sorted(d.items(), key=lambda x: x[1], reverse=True)))