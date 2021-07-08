thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = input("Type brand")

def test():
    var_y = thisdict[x]
    return var_y

print(test())