# here we find top 3 common words

from collections import Counter
import re

text = '''Hello world! Hello everyone. Welcome to the world of Python. Python is great, 
and the world is vast. Python is easier than java and cpp demand of Python is widely increasing'''

# words=text.split()
words=re.findall('\w+',text)

cout=Counter(words)
print(cout.most_common(3))
