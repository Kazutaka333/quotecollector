import json
from pprint import pprint

quoteList = []
deletedIndexes = []
with open('englishQuotes.json', "r") as data_file:    
    data = json.load(data_file)
    quotes = data["results"]
for i in range(len(quotes)):
	quoteData = quotes[i]
	if quoteData != None:
		if quoteData['quote'] not in quoteList:
			quoteList.append(quoteData['quote'])
		else:
			deletedIndexes.append(i)
	# quoteData.pop('createdAt', None)
	# quoteData.pop("updatedAt", None)
	# quoteData.pop("objectId", None)
for i in deletedIndexes:
	quotes[i] = None
while None in quotes:
	quotes.remove(None)
print len(quotes)
with open('englishQuotes.json', "w") as data_file:    
	json.dump(data, data_file, indent = 4)