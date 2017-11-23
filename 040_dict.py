#!/usr/bin/python3

myBio = { 'name' : "unknown", 'age' : 666, 'hobby' : 'hacking' }
print(myBio)

myBio["name"] = "x"
print(myBio["name"])

dict_hax= { (1,2) : "y", 1 : "hax" }
print(type(dict_hax[(1)]))
print(dict_hax[(1)], end="")
print(dict_hax[(1,2)])
