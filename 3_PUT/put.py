import requests
import json

if __name__ == '__main__':

	url = 'http://httpbin.org/put'
	payload = {'name':'Laura', 'course':'python', 'level':'advanced'}
	headers = {'Content-Type':'application/json', 'access-token':'12345'}
	
	response = requests.put(url, data = json.dumps(payload), headers = headers)
	
	print(response.url)
	
	if response.status_code == 200:
		headers_response = response.headers
		server = headers_response['Server']
		print(server)
	
	
	
	
	
	