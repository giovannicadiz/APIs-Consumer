import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/post'
	payload = {'name':'Laura', 'course':'python', 'level':'advanced'}
	
	response = requests.post(url, data = json.dumps(payload))

	print('\n',response.url)
	
	if response.status_code == 200:
		response_js = json.loads(response.text)
		print('\n',response_js)
