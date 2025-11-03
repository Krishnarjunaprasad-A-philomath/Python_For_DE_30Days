print("Hello!, Please Enter your Age: ")
Age = int(input())
breakpoint
if Age < 18 or Age >90:
     print("You are not eligible to vote")
else:
    print("You are eligible to Vote")
    print("Please enter 'Y' to caste your Vote")
    print("Please Enter 'N' to gave vote to 'NOTA' ")
    Button = input().upper()
    if Button == 'Y' and 'N' :
        print("You have succesfully casted your vote")
    else:
        print ("Please Enter proper Letter 'Y' or 'N' ")

