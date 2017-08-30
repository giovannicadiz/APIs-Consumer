import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/get'
	args = {'name':'Laura', 'course':'python', 'level':'advanced'}

	response = requests.get(url, params=args)
	print('\n',response.url)
	
	if response.status_code == 200:
		response_js = json.loads(response.text) # import json
		print('\n',response_js)
		origin = response_js['origin']
		print('\nORIGIN : ',origin)