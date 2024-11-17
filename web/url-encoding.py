import urllib.parse

originalString = "Hello Timik! This is a test /URL with spaces and symbols like % and @."

encodedString = urllib.parse.quote(originalString)

print("Original string:=> ", originalString)
print("Encoded string:=> ", encodedString)