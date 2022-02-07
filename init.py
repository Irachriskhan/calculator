from Calculator import Calculate

if __name__ == '__main__':
    while True:
        option = input("Choose your option: [1, 2 , 3 ]: ")
        if(option == "1" or option == "2" or option == "3"):
            r = Calculate(option)
            r.calculation()
        elif(option == "Q"):
            break





