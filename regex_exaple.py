import re

pattern = r"at"
text = "The cat sat on the mata."

matches = re.findall(pattern, text)
print(matches)