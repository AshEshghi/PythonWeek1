#Task3 Ash Eshghi
sample = [
    {'make': 'Google', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]
print("Original list of dictionaries: ",sample)
sample.sort(key=lambda item: item['model'], reverse=True)
print("Sorting the List of dictionaries:")
print(sample)
sample= []
number= int(input("How many dictionaries do you want?"))
for i in range(number):
    make = input("Make: ")
    model = int(input("Model: "))
    color = input("Color: ")
    item = {
        'make': make,
        'model': model,
        'color': color
    }
    sample.append(item)
sample.sort(key=lambda item: item['model'], reverse=True)
print(sample)
