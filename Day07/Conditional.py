import sys

type = sys.argv[1]

if type == "t2.micro":
    print("we will create instance for you")
else:
    print("please provide a valid instance type")