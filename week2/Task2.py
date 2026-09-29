#Task 2 Ash Eshghi
s1= input("Enter a string: ")
total= 0
count= 0
for character in s1:
    if character.isdigit():
        number= int(character)
        total= total+number
        count= count+1
if count > 0:
    average= total/count
else:
    average= 0

print("Sum:", total)
print("Average:", average)
