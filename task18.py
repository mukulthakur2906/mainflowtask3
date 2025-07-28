#-------------------------------------------
# Swap Two Numbers Without Third Variable
#-------------------------------------------
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a  # or use a = a + b; b = a - b; a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)
