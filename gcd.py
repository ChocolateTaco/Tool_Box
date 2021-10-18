def gcd(num1, num2):
    """
    This is a recursive calculator of the greatest common divisor (GCD)

    Args:
        num1 (integer): the first integer being questioned for the GCD
        num2 (integer): the second integer being questioned for the GCD

    Returns:
        integer: greatest common divisor of the inputted num1 and num2
    """
    if num1 % num2 == 0:
        print(num1, "=", int(num1 / num2), "*", num2, "+", num1 % num2)
        print(f"The GCD value computes to: {num2}")
        return num2
    print(num1, "=", int(num1/num2),"*" ,num2, "+", num1%num2)
    return gcd(num2, num1 % num2)

def main():
    """Calculates the GCD of two integers"""
    var1 = int(input("GCD Calculator\nInput the first value:\n>>> "))
    var2 = int(input("Input the second value:\n>>> "))
    gcd(var1, var2)
    input("Enter any key to quit\n")

if __name__ == "__main__":
    main()