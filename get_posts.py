import cgi

#!C:\Python227\python.exe
print("Content-type: text/html\n\n")

form = cgi.FieldStorage()
userName = form.getvalue()

print(userName)
