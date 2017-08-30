import requests
import json

if __name__ == '__main__':

	url = 'http://httpbin.org/delete'
	payload = {'name':'Laura', 'course':'python', 'level':'advanced'}
	headers = {'Content-Type':'application/json', 'access-token':'12345'}
	
	response = requests.delete(url, data = json.dumps(payload), headers = headers)
	
	print(response.url)
	
	if response.status_code == 200:
		headers_response = response.headers 
		server = headers_response['Server']
		print(server)
	
	
	
	
	
	