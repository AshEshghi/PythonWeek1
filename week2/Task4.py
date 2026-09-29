#Task 4 Ash EShghi
sample = []
number = int(input("How many strings do you want?"))
for i in range(number):
    word= input("Enter string: ")
    sample.append(word)
result = list(map(lambda x: [x], sample))
print("Original list:", sample)
print("List of lists:", result)
