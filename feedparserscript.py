import feedparser
import simplejson as json

d=feedparser.parse(r'http://www.wsj.com/xml/rss/3_7014.xml')
x0 = d.feed.link
x1 = d.feed.image
x2 = d.feed.title
x3 = d.feed.description
x4 = d.feed.date
print(json.dumps(x0, sort_keys=True, indent=4 * ' '))
print(json.dumps(x1, sort_keys=True, indent=4 * ' '))
print(json.dumps(x2, sort_keys=True, indent=4 * ' '))
print(json.dumps(x3, sort_keys=True, indent=4 * ' '))
print(json.dumps(x4, sort_keys=True, indent=4 * ' '))