import requests

url="http://127.0.0.1:5000/"
text="It was the worst and horrible exp"


r_get=requests.get(url)
print(r_get.text)


r_post=requests.post(url,json=text)
print(r_post.text)