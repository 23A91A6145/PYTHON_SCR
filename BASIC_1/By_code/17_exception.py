

    # Exception Handling (multiple except blocks)

a=5
b=2

try:
    print(a/b)
    k=int(input("Enter a number: "))
    print(k)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
except ValueError as e:
    print("Error: Invalid input. Please enter a valid integer.")
except Exception as e:
    print("Error:", e)
finally:
    print("Execution completed.")