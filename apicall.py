import requests

#r = requests.get('https://jsonplaceholder.typicode.com/posts')
r = requests.get('https://hlv7793ve8.execute-api.us-east-1.amazonaws.com/jsontest')

print(r.status_code)
print("---")
print(r.headers)
print("---")
for item in r.json():
    print(item)
