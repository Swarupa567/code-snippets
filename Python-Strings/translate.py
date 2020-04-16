dict = str.maketrans("abc", "def")
print(dict)
value = "aabbcc"
result = value.translate(dict)
print(result)
