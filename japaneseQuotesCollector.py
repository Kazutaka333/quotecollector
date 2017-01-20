#coding: utf-8
import sys, json
from pyquery import PyQuery

dic = { "results" :[]}
for i in range(1,99):
	print i
	urlStr = 'http://www.meigensyu.com/quotations/index/page' + str(i) + '.html'
	q = PyQuery(url=urlStr)
	# Meigen
	for meigenBox in q.find('.meigenbox'):
		tempList = {}
		meigenBoxQ = PyQuery(meigenBox)
		meigenText = meigenBoxQ.find('.text')[0]
		meigenQ = PyQuery(meigenText)
		enText = meigenQ.find('.en_text')
		if len(enText):
			enTextQ = PyQuery(enText[0])
			tempList['quote_en'] = enTextQ.text()
		meigenQ.remove(".en_text")
		tempList["quote"] = meigenQ.text()
		linkBlock = meigenBoxQ.find('.link')[0]
		linkBlockQ = PyQuery(linkBlock)
		for ele in linkBlockQ.find('li'):
			eleQ = PyQuery(ele)
			if eleQ.text() == '[詳細]':
				break
			elif eleQ.text()[0:3] == '出典:':
				tempList["reference"] = eleQ.text()[4:]
			elif eleQ.text()[0:3] == '著者:':
				if len(eleQ.text()[4:]):
					tempList["author"] = eleQ.text()[4:]
			elif eleQ.text()[0:4] == 'キャラ:':
				tempList["character"] = eleQ.text()[5:]
			else:
				tempList["source"] = eleQ.text()
		tagBox = meigenBoxQ.find(".tags")
		tagBoxQ = PyQuery(tagBox)
		tagList = []
		for tag in tagBoxQ.find('a'):
			tagQ = PyQuery(tag)
			tagList.append(tagQ.text())
		tempList['tags'] = tagList
		tempList['views'] = 0
		dic["results"].append(tempList)


	

text = json.dumps(dic, sort_keys=True, ensure_ascii=False, indent=4)
with open('meigen.json', 'w') as f:
    f.write(text.encode("utf-8"))
