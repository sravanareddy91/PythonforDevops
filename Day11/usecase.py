import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

#print(response)
#print(type(response))
#print(response.json())
#print(response.status_code)

output = response.json()
#print(output[0]["id"])

for i in range(len(output)):
    print(output[i]["user"]["login"])