import re
string = " 'I AM NOT YELLING', she said. Though we knew it to be true."
#print(string)
#new = re.sub('[a-z]', '', string)
#new = re.sub('[.,\']', '', string)
#new = re.sub('[.,\'a-z]', '', string)
#new = re.sub('[.,\'a-zA-Z]', '', string)
#new = re.sub('[.,\'A-Z]', '', string)
#new = re.sub('[.,\'A-Z+" "]', '', string)
string = string, "6 298 - 345"
print(string)
new = re.sub('[^str(0-9]', '', string)
print(new)