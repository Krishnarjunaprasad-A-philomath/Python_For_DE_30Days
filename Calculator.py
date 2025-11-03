print("Please enter A: ")
A= int(input())
print("Please enter B: ")
B=int(input())
print("Please enter Operarion: 'ADD', 'SUB', 'DIV', 'MUL' ")
Operation = input().upper()
if Operation == 'ADD' :
    print(A + B)
elif Operation == 'SUB':
    print(A - B)
elif Operation == 'DIV':
    print(A / B)
elif Operation == 'MUL':
    print(A * B)
else:
    print("Please enter the Proper operation: 'ADD', 'SUB', 'DIV', 'MUL' ")