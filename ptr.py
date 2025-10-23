
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal

P = 10000  # Principal amount
R = 5      # Rate of interest
T = 3      # Time in years

simple_interest = calculate_simple_interest(P, R, T)
compound_interest = calculate_compound_interest(P, R, T)

print(f"Simple Interest: ₹{simple_interest}")
print(f"Compound Interest: ₹{round(compound_interest, 2)}")
