#coding: utf-8
import sys, json, time, urllib2
from pyquery import PyQuery


def getPyQueryFromUrl(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'mozilla 3.6')] #fake agent
    return PyQuery(opener.open(url).read())

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
    if current >= maximum:
        print

def writeDictionary(dict, fileName):
    text = json.dumps(dic, sort_keys=True, ensure_ascii=False, indent=4)
    with open(fileName, 'w') as f:
        f.write(text.encode("utf-8"))

def numberPageUrl(url):
    # example url: http://www.brainyquote.com/quotes/topics/topic_success.html
    if i == 1:
        page = ''
    else:
        page = str(i)
    return url[:len(url)-5] + page + '.html'

dic = { "results" :[]}

TOPIC_URL = "https://www.brainyquote.com/quotes/topics.html"
ORIGINAL_URL = 'http://www.brainyquote.com/quotes/topics/topic_success.html'
OUTPUT_FILENAME = 'englishQuotes.json'

# find how many topics exist
q = getPyQueryFromUrl(TOPIC_URL)
topicRowDivs = q.find(".topicContentName")
print len(topicRowDivs)
'''
# iterate through topics



# find the last page number on the topic
q = getPyQueryFromURL(ORIGINAL_URL)
pagingUl = q.find(".pagination, .bqNPgn, .pagination-sm")
pagingUlQ = PyQuery(pagingUl)
aTags = pagingUlQ.find('a')
aTags.pop()
lastPage = int(PyQuery(aTags.pop()).text())


print "There are " + str(lastPage) + " pages in this topic"

for i in range(1,lastPage+1):

    printProgressBar(i,lastPage)

    url = numberPageUrl(ORIGINAL_URL)

    q = getPyQueryFromURL(url)

    # filter out quote and info
    for quoteDiv in q.find('.bqQt'): 

        tempDict = {}
        quoteDivQ = PyQuery(quoteDiv)
        quoteText = quoteDivQ.find('.b-qt')[0]
        author = quoteDivQ.find(".bq-aut")[0]
        tagDiv = quoteDivQ.find(".kw-box")
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

# convert into json and write
writeDictionary(dic, OUTPUT_FILENAME)
'''
