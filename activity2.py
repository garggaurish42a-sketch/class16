#cube of the cube
def cube(number):
    return number*number*number
#define a function which will excute cube function only if the user entered the number is divisible by 3
def by_three(number):
    if (number %3)==0:
        return cube (number)
    else:
        return False
print(by_three(9))
print(by_three(4))
