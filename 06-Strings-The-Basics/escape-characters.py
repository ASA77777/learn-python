print("This will \nbegin on a \nnew line")

print("\tOnce upon a time") #\t = tab

print("\"To be or not to be\", said Hamlet") #Slash in front of the second set of quotes (Escaping double quotes)
print('\'To be or not to be\', said Hamlet') #Escaping single quotes
print("Let's print a backslash: \\") #Escape backslash

file_name = r"C:\news\travel" #r = raw string (String to be taken literally)
print(file_name)

some_randome_number = 5
some_obscure_calculation = 25
some_additional_statistic_fetched_from_somewhere = 10

#backslash to break off expressions across multiple lines
final = some_randome_number + \
    some_obscure_calculation + \
    some_additional_statistic_fetched_from_somewhere

print(some_randome_number,
    some_obscure_calculation, 
    some_additional_statistic_fetched_from_somewhere)

