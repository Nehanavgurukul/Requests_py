import requests
import json

req = requests.get("http://saral.navgurukul.org/api/courses")

s = json.dumps(req.json(), indent=4)

myjsonfile = open('courses.json','w')
myjsonfile.write(s)