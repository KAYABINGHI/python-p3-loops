#!/usr/bin/env python3

def happy_new_year():
    # Start at 10 and count down to 1
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # Create a new list of squared integers using a for loop
    squared = []
    for num in int_list:
        squared.append(num ** 2)
    return squared

def fizzbuzz():
    # Print numbers from 1 to 100 with FizzBuzz logic
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


happy_new_year()
print(square_integers([1, 2, 3, 4, 5]))
fizzbuzz()
