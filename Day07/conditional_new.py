
import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it will charge you 2 dollars")
elif type == "t2.medium":
    print("it will charge you 4 dollars")
elif type == "t2.xlarge":
    print("it will charge you 8 dollars")
else:
    print("please provide a valid instance type")