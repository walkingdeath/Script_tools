import requests
import json
load = {"password":"admin","rememberMe":True,"username":"admin"}
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
r = requests.post("http://10.165.33.20:8090/api/authenticate", data = json.dumps(load),headers =headers )
print(r.content)


print(type(load))