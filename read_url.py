import httplib2

url = "http://mf2.dit.ie/gettysburg.txt"

h = httplib2.Http(".cache")

headers, body = h.request(url)

for header in headers:
    print("{}: {}".format(header, headers[header]))

print("-"*30)

decoded = body.decode()
print(decoded)
print("-"*30)