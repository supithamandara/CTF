# Import the libraries we downloaded earlier
# if you try importing without installing them, this step will fail
from bs4 import BeautifulSoup
import requests
for api_key in range(1,100,2):	
	# replace testurl.com with the url you want to use.
	# requests.get downloads the webpage and stores it as a variable
	html = requests.get(f'http://10.10.243.50/api/{api_key}')
	print(html.text)

