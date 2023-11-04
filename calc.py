"""
This is a simple implementation for a calculator
"""
A = 9
B = 4
OP = '+'
if OP.strip() == '+':
    print(A+B)
elif OP.strip() == '-':
    print(A-B)
elif OP.strip() == '*':
    print(A*B)
elif OP.strip() == '/':
    if B!=0:
        print(A/B)