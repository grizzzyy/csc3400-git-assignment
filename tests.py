from calculator import add, subtract, multiply, divide, power, square_root

def test(name, actual, expected):
    if actual == expected:
        print(name + ": PASS")
    else:
        print(name + ": FAIL")
        print("  Got:", actual)
        print("  Expected:", expected)

print("Running calculator tests...\n")

test("Add", add(2, 3), 5)
test("Subtract", subtract(10, 4), 6)
test("Multiply", multiply(3, 5), 15)
test("Divide", divide(10, 2), 5)
test("Power", power(2, 4), 16)

test("Square Root", square_root(9), 3.0)

test("Divide by zero", divide(5, 0), "Error: Cannot divide by zero")
test("Square root negative", square_root(-1), "Error: Cannot take square root of a negative number")

