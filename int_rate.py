# Interest Rate Calculator

def interest(initial_amount, years, annual_interest):
    if years < 0:
        return False
    if years == 0:
        return initial_amount
    year_amount = initial_amount + (annual_interest * initial_amount) / 100
    return interest(year_amount, years - 1, 10)

print(f"${interest(100, 1, 10)}")
