
def fizzbuzz(input_num: int) -> str : 
    if (input_num % 3 == 0 and input_num % 5 == 0):
        return "FizzBuzz"
    elif (input_num % 3 == 0):
        return "Fizz"
    elif (input_num % 5 == 0):
        return "Buzz"
    else:
        return str(input_num)
    
if __name__ == '__main__':
    print(map(fizzbuzz, range(1,101)))