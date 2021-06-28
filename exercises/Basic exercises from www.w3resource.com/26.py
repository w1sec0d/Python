def histogram(list):
    for integer in list:
        print("*"*abs(int(integer)))


histogram(input("Please type your elements separated by a comma").split(","))
