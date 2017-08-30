import requests

if __name__ == '__main__':
	url = 'http://www.httpbin.org/'
	response = requests.get(url)
	
	if response.status_code == 200:
		content = response.content
		
		file = open('httpbin.html', 'wb')
		file.write(content)
		file.close()