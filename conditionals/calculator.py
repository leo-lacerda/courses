def main():
  x = int(input("What's x? "))
  y = int(input("What's y? "))
  op = input("What's the operator (/, *, +, -)? ")
  print(calculator(x, y, op))


def calculator(n, m, op):
  if op == "/":
    return n / m
  elif op == "*":
    return n * m
  elif op == "+":
    return n + m
  elif op == "-":
    return n - m
  else:
    print("This is not a valid number or operator.")


main()
