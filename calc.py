import sys

# handle add for multiple args
# for example add 1 2 3 4 5 6
# number of args can be empty(ignored)
def additionHandler(func):
    res = 0
    try:
        for index in range(1, len(func)):
            res += int(func[index])
    except ValueError as error:
        print(error.args)
        raise
    return res

# handle multiply for multiple args
# for example mutiply 2 3 4 5 6 7
# number of args must be greater than 2
def multiplyHandler(func):
    if(len(func) < 3):
        raise Exception("Not enough args supplied to multiply function")
    res = 1
    try:
        for index in range(1, len(func)):
            res *= int(func[index])
    except ValueError as error:
        print(error.args)
        raise
    return res

# handle func for add and multiply
# we can add other function later
def handleFunc(func):
    if func[0] == 'add':
        return additionHandler(func)
    elif func[0] == 'multiply':
        return multiplyHandler(func)
    else:
        raise Exception("Error: Unsupported function")

def calc(input):
    operationsCount = input.count(')')
    # if a simple number is entered
    # EXPR = INTEGER
    if operationsCount == 0:
        try:
            return int(input)
        except ValueError as error:
            print(error.args)
            raise
    res = 0
    # There are some func left...
    while operationsCount > 0:
        # get bounds
        right = input.index(")")
        left = input.rindex("(", 0 , right)
        # extract func
        func = input[left+1 : right].split()
        # handle all func
        res = handleFunc(func)
        # update input string
        input = input[0 : left] + str(res) + input[right+1 : len(input)] 
        operationsCount -= 1
    return res

def main():
    if len(sys.argv) == 2:
        print(calc(sys.argv[1]))
    else:
        print("USAGE: ./calc.py FUNC")


if __name__ == "__main__":
    main()
