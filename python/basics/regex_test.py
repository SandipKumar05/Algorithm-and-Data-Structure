import re

regex = r"\w+\."
s = "sandip. kumar gupta"

res = re.search(regex, s)
print(res)