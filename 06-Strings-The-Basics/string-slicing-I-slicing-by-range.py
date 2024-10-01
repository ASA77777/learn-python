address = "Attractive Street, Beverly Hills, CA 90210"

print(address[0:3]) #left = inclusive, right = exclusive
print(address[0:4]) 
print(address[0:17]) 
print(address[19:32]) 
print(address[10:100]) #Doesnt give us an error, just gives us the entire sentence

print("\n") #Line break

print(address[34:-6]) #Inclusion and exclusion rule still exists
print(address[-8:-6])
print(address[-8:36]) #Top 3 lines of code will give the same output just diff ways of applying the syntax

print("\n")

print(address[5:]) #5th index till the end
print(address[13:])
print(address[-10:])

print(address[:10]) #Start from beginning of the string till the mentioned index position
print(address[0:10]) #Same as above
print(address[:23])
print(address[:-3])

print(address[:]) #Will give you the complete copy of the string (it is a brand new string object though)