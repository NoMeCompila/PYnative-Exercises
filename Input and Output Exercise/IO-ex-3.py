"""
Convert Decimal number to octal using print() output formatting
"""

def parse_octal():
    try:
        x = int(input("Enter a number to convert: "))
        print(f"number {x} in octal is:{oct(x)}")

    except ValueError:
        print("invalid value... try again")
        parse_octal()


parse_octal()