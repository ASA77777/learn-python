browser = "Google Chrome"

print(browser.find("C"))
print(browser.find("Ch"))
print(browser.find("o"))
print(browser.find("G"))
print(browser.find("Z"))
print(browser.find("Zxy"))
print(browser.find("c"))

print()

print(browser.find("o"))
print(browser.find("o", 2))
print(browser.find("o", 5))

print("Ch" in browser)

print(browser.index("C"))
#print(browser.index("Z")) #Will raise ValueError


best_sport = "Tennis is the best sport"

print(best_sport.rfind("t"))

print(best_sport.rfind("Tennis"))

print(best_sport.rfind("n",2 ))