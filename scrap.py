import requests
from bs4 import BeautifulSoup
from random import choice
data=[]

n=1
while True:
	response=requests.get(f'http://quotes.toscrape.com/page/{n}/')
	html=response.text
	soup=BeautifulSoup(html,'html.parser')
	quotes=soup.select(".quote")
	for quote in quotes:
		text=quote.find("span").get_text()
		url=quote.find("a")["href"]
		res=requests.get(f"http://quotes.toscrape.com{url}")
		soup2=BeautifulSoup(res.text,'html.parser')
		name=soup2.select(".author-title")[0].get_text()
		dob=soup2.select(".author-born-date")[0].get_text()
		loc=soup2.select(".author-born-location")[0].get_text()
		data.append([text,name,dob,loc])
	if soup.find(class_="next")==None:
		break
	n+=1
def check():
	global flag,n
	i=input()
	if i.lower()==quote[1].lower():
		flag=True
		print('You guessed correctly! Congratulations!')
		return
	n-=1
o='y'
while o.lower()=='y':
	quote=choice(data)
	n=4
	flag=False
	print(f"Here's a Quote:\n{quote[0]}")
	print(f"Who said this? Guesses remaining: {n}.",end=" ")
	check()
	if not flag:
		print(f"Here's a hint: The author was born in {quote[2]} {quote[3]}")
		print(f"Who said this? Guesses remaining: {n}. ",end=" ")
		check()
	if not flag:
		print(f"Here's a hint: The author first name starts with {quote[1].split()[0][0]}")
		print(f"Who said this? Guesses remaining: {n}. ",end=" ")
		check()
	if not flag:
		print(f"Here's a hint: The author last name starts with {quote[1].split()[-1][0]}")
		print(f"Who said this? Guesses remaining: {n}. ",end=" ")
		check()
	if n==0:
		print(f"Sorry,you've run out of gusses. The answer was {quote[1]}")
	print("Would you like to play again(y/Y)?")
	o=input()
