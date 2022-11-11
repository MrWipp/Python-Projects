import keyboard
import sys
print("To exit the calculator, type 'exit'\n")
listening = True
def quit():

    sys.exit()


def start_app():

    number_list = []
    
    nums_amount = int(input("How many numbers you want to calculate? eg: 2\n"))
    nums_amount-=1
    while int(len(number_list)) <= nums_amount:
        number = int(input(f"Number{len(number_list) + 1}: "))
        if number == 'exit':
            quit()
        elif type(number) != int:
            print("You can only add numbers!")
        else:
            number_list.append(number)
    print("\nChoose your calculation method:\n 1. Sum\n 2. Multiply\n 3. Divide")
    get_method(number_list)

def get_method(numbers):
    while listening:
        if keyboard.is_pressed('1'):
            sum(numbers)
            break
        elif keyboard.is_pressed('2'):
            multiply(numbers)
            break
        else:
            pass

def sum(numbers):
    total = 0

    for i in numbers:
        total = total + i
    print(f"the sum of your numbers are: {total}")


def multiply(numbers):
    listening = False
    total = 1

    for i in numbers:
        total = total * i
    print(f"the multiply of your numbers are: {total}")

# def divide(a,b):
#     return a / b

start_app()