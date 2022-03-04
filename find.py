# calling for phonebook and reading it
text_file = open('phonebook.txt', 'r')
lines = text_file.read()
text_file.close()

# splitting phonebook data into str to use in array
content_lines = lines.split("\n")
# sorting array
content_lines.sort()
# checking the number of indexes used in our array
print("number of item in list = ", len(content_lines))
print(content_lines)

# checking the lenght of list
length = len(content_lines)
for i in range(len(content_lines)):
    half_index = length // 2
    first_half = content_lines[:half_index]
    second_half = content_lines[half_index:]

name = input("enter name to find")
position = -1

for i in range(len(content_lines)):
    if first_half[i] == name or second_half[i] == name:
        position = i
        break

    else:
        print(name,"not found")
if position > -1:
    print(name, "found at", position)


#