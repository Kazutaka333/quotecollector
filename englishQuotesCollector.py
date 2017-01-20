#coding: utf-8
import sys, json, time, urllib2
from pyquery import PyQuery


def getPyQueryFromURL(url):
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'mozilla 3.6')] #fake agent
	return PyQuery(opener.open(url).read())

dic = { "results" :[]}

originalUrl = 'http://www.brainyquote.com/quotes/topics/topic_success.html'
q = getPyQueryFromURL(originalUrl)

# find the last page
pagingUl = q.find(".pagination, .bqNPgn, .pagination-sm")
pagingUlQ = PyQuery(pagingUl)
aTags = pagingUlQ.find('a')
aTags.pop()
lastPage = int(PyQuery(aTags.pop()).text())

print "There are " + str(lastPage) + " pages"

def printProgressBar(current,maximum):
	percentage = int(float(current)/float(maximum)*100.0)
	blockNum = percentage/2
	blockStr = '['
	for i in range(0,blockNum):
		blockStr += "■"
	for i in range(0,50-blockNum):
		blockStr += " "
	blockStr += "]"
	sys.stdout.write("\r%d%% %s " % (percentage, blockStr))
	sys.stdout.flush()


#for i in range(1,lastPage+1):
for i in range(1,5):

	# progress bar
	percentage = int(float(i)/float(lastPage)*100.0)
	blockNum = percentage/2
	blockStr = '['
	for i in range(0,blockNum):
		blockStr += "■"
	for i in range(0,50-blockNum):
		blockStr += " "
	blockStr += "]"
	sys.stdout.write("\r%d%% %s " % (percentage, blockStr))
	sys.stdout.flush()
	

	if i == 1:
		page = ''
	else:
		page = str(i)
	url = originalUrl[0:len(originalUrl)-5]+page+'.html'
	q = getPyQueryFromURL(url)

	for quoteDiv in q.find('.masonryitem, .boxy, .bqQt, .bqShare, .masonry-brick'): 
		tempDict = {}
		quoteDivQ = PyQuery(quoteDiv)
		quoteText = quoteDivQ.find('.bqQuoteLink')[0]
		author = quoteDivQ.find(".bq-aut")[0]
		tagDiv = quoteDivQ.find(".body, .bq_boxyRelatedLeft, .bqBlackLink")
		tags = PyQuery(tagDiv).find('a')
		tempDict['quote'] = PyQuery(quoteText).text()
		tempDict['source'] = PyQuery(author).text()
		tempDict['tags'] = []
		for tag in tags:
			txt = PyQuery(tag).text()
			tempDict['tags'].append(txt)
		tempDict['views'] = 0
		tempDict['category'] = 'Success'
		dic["results"].append(tempDict)

text = json.dumps(dic, sort_keys=True, ensure_ascii=False, indent=4)
with open('englishQuotes.json', 'w') as f:
    f.write(text.encode("utf-8"))
