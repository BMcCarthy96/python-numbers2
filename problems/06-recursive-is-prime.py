# Create a function called `is_prime` that takes in a number and a variable that
# equates to 2. The function should return True/False if the number is a prime
# number. Bonus: Try to do this recursively.

# Write your solution here.
def is_prime(num, divisor=2):
    # Base case: If num is less than 2, it's not prime
    if num <= 1:
        return False
    # Base case: If divisor is greater than the square root of num, it's prime
    if divisor * divisor > num:
        return True
    # If num is divisible by divisor, it's not prime
    if num % divisor == 0:
        return False
    # Recursive case: check the next divisor
    return is_prime(num, divisor + 1)

print(is_prime(1))  #> False
print(is_prime(2))  #> True
print(is_prime(3))  #> True
print(is_prime(5))  #> True
print(is_prime(9))  #> False
print(is_prime(15)) #> False
