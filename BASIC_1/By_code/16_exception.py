

        # Exception Handling

# Handles unexpected events (like invalid input or missing files) without crashing.

a=5
b=2

try:
    result=a/b
    print("Result:", result)
except Exception as e:
    print("Error:", e)
finally:
    print("Execution completed.")