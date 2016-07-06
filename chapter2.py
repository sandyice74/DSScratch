# author = Di
"""for i in [1, 2, 3, 4, 5]:
    print (i)
    for j in [1, 2, 3, 4, 5]:
        print (j)
        print (i + j)
    print (i)
print ("done looping")


def subtract(a=0, b=0):
    return a - b


print (subtract(10, 5))

try:
    print (0/0)
except ZeroDivisionError:
    print ("cannot divide by zero")

x = [1,2,3]
x.extend([4,5,6])
print (x)

x = [1,2,3]
y = x + [4,5,6]
print (x)
print (y)

tweet = {
    "user": "joelgrus",
    "text": "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()
print (tweet.items())

#word_count
# method 1
word_counts = {}
for word in document:
    if word in word_counts:
        word_count[word] += 1
    else:
        word_count[word] = 1

# 2

word_count = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] =1
#3

word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous + 1

# 4
from collections import defaultdict
word_counts = defaultdict(dict)
for word in document:
    word_counts[word] += 1"""

lazy_evens_below_20 = (i for i in lazy_range(20) if i %2 == 0)





