# phonebook array
Phonebook = []

# limit of loop
n=int(input("Set the limit maximum number of name"))

# creating loop to store data in array
for i in range(0,n):
    name=input("enter names:  ")
    Phonebook.append(name)

# creating filter array with no duplicate data in it
filter_array =[]
# storing all array data in var i
for i in Phonebook:
    # checking if values of i not in filter_array then append them into filter_array
    if i not in filter_array:
        filter_array.append(i)


# creating a phonebook.txt file in append mod to store multi times data in it
with open('phonebook.txt', 'a') as filehandle:
    # now putting listitems in phonebook and saving them as string in phonebook via filehandle variable
    for listitem in filter_array:
        filehandle.write('%s\n' % listitem)
