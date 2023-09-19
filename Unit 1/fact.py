def fact(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact(n - 1)


number = int(input("Enter any number to find factorial:".title()))
rec = fact(number)
print(f"The factorial of {number} is {rec}.".title())
