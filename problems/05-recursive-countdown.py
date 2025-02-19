# Create a function that recursively prints a countdown from 5 to 1.

# Write your function here.
def recursive_countdown(n):
    if n == 0:
        return
    else:
        print(n, end=" ")  # Print the current number without a newline
        recursive_countdown(n - 1)  # Recursively call with n-1

recursive_countdown(5) #> 5 4 3 2 1
