import requests

url = 'https://sikee18-docuai.hf.space/_upload'

# Create a tiny dummy file
with open('dummy.txt', 'wb') as f:
    f.write(b"Hello world")

files = {'files': open('dummy.txt', 'rb')}

response = requests.post(url, files=files)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")
