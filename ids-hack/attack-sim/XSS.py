import requests

# URL of your local test app
url = "http://localhost:8000/search"

# Payload to test XSS
payload = "<script>alert('XSS')</script>"

# Send the payload as a GET parameter
params = {"q": payload}

response = requests.get(url, params=params)

if payload in response.text:
    print("[!] Vulnerable to XSS")
else:
    print("[+] Not vulnerable")