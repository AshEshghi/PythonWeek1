"""Task 3: Convert between basic Python data types."""

# 1. Integer to floating-point number.
integer_number = 10
floating_point_number = float(integer_number)
print("Integer to float:", integer_number, "->", floating_point_number)
print("Result type:", type(floating_point_number))

# 2. Floating-point number to integer (the fractional part is removed).
original_float = 10.5
converted_integer = int(original_float)
print("\nFloat to integer:", original_float, "->", converted_integer)
print("Result type:", type(converted_integer))

# 3. Integer to string.
number = 42
converted_string = str(number)
print("\nInteger to string:", number, "->", repr(converted_string))
print("Result type:", type(converted_string))

# 4. String containing a number to integer.
number_text = "123"
parsed_integer = int(number_text)
print("\nString to integer:", repr(number_text), "->", parsed_integer)
print("Result type:", type(parsed_integer))

# 5. Integer to Boolean (zero is False, nonzero is True).
boolean_source = 1
converted_boolean = bool(boolean_source)
print("\nInteger to Boolean:", boolean_source, "->", converted_boolean)
print("Result type:", type(converted_boolean))
