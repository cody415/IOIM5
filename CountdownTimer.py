def countdown(number):
    if number == 0:
        print("Time is up!")
        return
    print(number)
    countdown(number - 1)

def build_and_unwind(level):
    if level == 0:
        print("Base case reached")
        return
    print(f"Build level {level}")
    build_and_unwind(level - 1)
    print(f"Unwind level {level}")

def count_up(number):
    if number > 10:
        return
    print(number)
    count_up(number + 1)

def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)

def unsafe_countdown(number):
    print("This function has no base case and would cause a stack overflow if executed.")

print("Countdown from 5:")
countdown(5)

print("\nBuild and Unwind (level 3):")
build_and_unwind(3)

print("\nCount Up from 1:")
count_up(1)

print("\nFactorial of 5:")
print("Result:", factorial(5))

print("\nUnsafe Countdown Demo:")
unsafe_countdown(5)
