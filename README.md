# copies sample sentences of specific words to a word doc
# opens new tabs of definitions of specific words

def michael():
	from bs4 import BeautifulSoup as bs
	import requests, docx, snake
	snake.go()
	doc = docx.Document()
	savior = input('Enter challenge number: ')
	while True:
		word = input('Vocab: ')
		if word == 'end':
			break
		web = requests.get('http://sentence.yourdictionary.com/' + word)
		soup = bs(web.text)
		sentence = soup.find('li').text
		if sentence == 'English Grammar Rules and Usage All the help you need for punctuation, capitalization and word usage.':
			print('Unable to find anything. Please check for any spelling errors')
			continue
		print(sentence)
		doc.add_paragraph(sentence)
	doc.save(str(savior) + ' sentence.docx')
    
