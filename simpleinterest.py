def simple_interest(p, r, t):
    return (p * r * t) / 100

if _name_ == "_main_":
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest: "))
    t = float(input("Enter time: "))

    print("Simple Interest is: ", simple_interest(p, r, t))