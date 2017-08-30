import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/post'
	payload = {'name':'Laura', 'course':'python', 'level':'advanced'}
	headers = {'Content-Type':'application/json', 'access-token':'12345'}
	
	response = requests.post(url, data = json.dumps(payload), headers = headers)
	print('\nURL    : ',response.url)
	
	if response.status_code == 200:
	
		headers_response = response.headers
		response_js = json.loads(response.text)
		print('\n', response_js)
		
		print('\n',headers_response)
		server = headers_response['Server']
		print('\nServer : ',server)
		