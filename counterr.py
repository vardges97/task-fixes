def create_counter(initial_value=0):
    counter = initial_value

    def increment(amount=1):
        nonlocal counter
        counter += amount

    def decrement(amount=1):
        nonlocal counter
        counter -= amount

    def get_counter_value():
        return counter

    return increment, decrement, get_counter_value


increment, decrement, get_value = create_counter(10)


print("Initial Counter Value:", get_value())

increment()
print("After Increment:", get_value())

increment(10)
print("After Increment by 10:", get_value())

decrement(4)
print("After Decrement by 4:", get_value())


increment2, decrement2, get_value2 = create_counter()

print("Counter 2 Initial Value:", get_value2())

increment2()
print("Counter 2 After Increment:", get_value2())