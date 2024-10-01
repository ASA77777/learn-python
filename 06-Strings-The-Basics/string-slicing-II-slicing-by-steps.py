alphabet = "abcdefghijklmnopqrstuvwxyz"

print(alphabet[0:10:2])
print(alphabet[0:26:3])
print(alphabet[:26:3])
print(alphabet[0::3])
print(alphabet[::3]) # lines 4,5,6,7 give the same results

print(alphabet[4:20:5])
print(alphabet[-20:-8:5])

print(alphabet[::-3])
print(alphabet[::-2])
print(alphabet[::-1]) #Gives you the entire string in reverse order