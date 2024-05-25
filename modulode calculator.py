# Welcome to modulus calculator
# Here is the formula for modulus
# x % y = z
# z * y = x
# using this logic to create modulus caculator
print("|__--__|`Welocome to Modulus calculator`|__--__|")
user_intp1 = float(input("Enter the Dividend = "))
user_intp2 = float(input("Enter the Divisor  = "))
formula = user_intp1 % user_intp2
constant = formula * user_intp2
# final_prt = str(user_intp1 + user_intp2)
print(f'-:-:-:-The modulus of {user_intp2} % {user_intp1} is {constant}')