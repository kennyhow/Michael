# copies sample sentences of specific words to a word doc
# opens new tabs of definitions of specific words

def michael():
	from bs4 import BeautifulSoup as bs
	from selenium import webdriver
	from selenium.webdriver import ActionChains
	from selenium.webdriver.common.keys import Keys
	import requests, docx, snake, time
	snake.go()
	doc = docx.Document()
	savior = input('Enter challenge number: ')
	words = []
	driver = webdriver.Chrome()
	while True:
		word = input('Vocab: ')
		if word == 'end':
			break
		words.append(word)
		web = requests.get('http://sentence.yourdictionary.com/' + word)
		soup = bs(web.text, 'lxml')
		sentence = soup.find('li').text
		if sentence == 'English Grammar Rules and Usage All the help you need for punctuation, capitalization and word usage.':
			print('Unable to find anything. Please check for any spelling errors')
			continue
		doc.add_paragraph(sentence)
	for word in words[:-1]:
		driver.get('https://www.google.com/search?q=define%20{}/'.format(word))
		actions = ActionChains(driver)
		about = driver.find_element_by_link_text('Settings')
		actions.key_down(Keys.CONTROL).click(about).key_up(Keys.CONTROL).perform()
		driver.switch_to.window(driver.window_handles[-1])
		time.sleep(1)
	driver.get('https://www.google.com/search?q=define%20{}/'.format(words[-1]))
	doc.save(str(savior) + ' sentence.docx')
