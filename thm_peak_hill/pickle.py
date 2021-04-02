#!/usr/bin/env python3

import pickle


unpickled = pickle.load(open("creds","rb"))

for j in range(7):
	for i in range(len(unpickled)):
		if f"ssh_user{j}" == unpickled[i][0]:
			print(unpickled[i][1], end="")

print("\n")

for j in range(28):
	for i in range(len(unpickled)):
		if f"ssh_pass{j}" == unpickled[i][0]:
			print(unpickled[i][1], end="")


print("\n")