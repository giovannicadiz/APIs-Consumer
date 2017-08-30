import requests

if __name__ == '__main__':

	url = 'http://httpbin.org/get'
	args = {'name':'Laura', 'course':'python', 'level':'advanced'}#key : value
	response = requests.get(url, params=args)
	print('\n',response.url,'\n')
	
	if response.status_code == 200:
		content = response.content
		print(content)