#Task 1 Ash Eshghi
from ast import literal_eval
sample = literal_eval(input("Enter a list of tuples: "))
for i in range(len(sample)):
    for j in range(i + 1, len(sample)):
        if sample[i][len(sample[i])-1]>sample[j][len(sample[j])-1]:
            sample[i], sample[j] = sample[j], sample[i]
print("Sorted list:", sample)


