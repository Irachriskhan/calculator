
class Calculate:
    def __init__(self, calc):
        self.calc = calc

    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    def calculation(self):
        if self.calc == '1':
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                from operator import add
                print(num1, "+", num2, "=", add(num1, num2))
            except Exception:
                print("Invalid Input")

        elif self.calc == '2':
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                from operator import sub
                print(num1, "-", num2, "=", sub(num1, num2))
            except Exception:
                print("Invalid Input")

        elif self.calc == '3':
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                from operator import mul
                print(num1, "*", num2, "=", mul(num1, num2))
            except Exception:
                print("Invalid Input")

        elif self.calc == '4':
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                from operator import floordiv
                print(num1, "/", num2, "=", floordiv(num1, num2))
            except Exception:
                print("Invalid Input")

        else:
            print("Invalid Input")


"""You can use below portion of code on the same page. 
Or create an init.py file and import the file and execute from another file"""
# if __name__ == '__main__':
#     while True:
#         option = input("Choose your option: [1, 2 , 3 ]: ")
#         if(option == "1" or option == "2" or option == "3"):
#             r = Calculate(option)
#             r.calculation()
#         elif(option == "Q"):
#             break

