import json

d= {"o":[[1,2,3], [9]], 
    "t": "sdfsdfsdf"}

dump = json.dumps(d)
s = json.loads(dump)
print(type(s))
print(s)
