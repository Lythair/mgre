import json
data = 'testing'
with open('test.txt', 'w') as outfile:
	json.dump(data, outfile)
