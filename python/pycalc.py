help = input("PythonCalc V 1.3 by Sam Langer; Say 'help' for available commands, and to start the calculator. ")
if help== "help" or "Help":
  print("Signs: '+', '-', '*', '/', 'sqr', 'sqrt', 'cube', '!', 'power'. ")
  sign = input("What operation should I use? ")
  if sign== "+":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("Processing...")
    print (num1+num2)
  elif sign== "-":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("Processing...")
    print (num1-num2)
  elif sign== "*":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("Processing...")
    print (num1*num2)
  elif sign== "/":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("Processing...")
    print (num1/num2)
  elif sign== "sqr":
    num1 = int(input("What is the number you wish to be squared? "))
    print("Processing...")
    print (num1**2)
  elif sign== "cube":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("Processing...")
    print (num1**3)
  elif sign== "power":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("Processing...")
    print (num1**num2)
  elif sign== "sqrt":
    num1 = int(input("What is the number you seek the square root of? "))
    print("Processing...")
    print (sqrt(num1))
  elif sign== "!":
    num1 = int(input("What is the number you seek the factorial of? "))
    print("Processing...")
    print (factorial(num1))
  else:
    print("I am sorry, but I am unable to process your request.")
elif help== "ready" or "Ready":
  sign = input("What operation should I use? ")
  if sign== "+":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("Processing...")
    print (num1+num2)
  elif sign== "-":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("Processing...")
    print (num1-num2)
  elif sign== "*":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("Processing...")
    print (num1*num2)
  elif sign== "/":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("Processing...")
    print (num1/num2)
  elif sign== "^2":
    num1 = int(input("What is the number you wish to be squared? "))
    print("Processing...")
    print (num1**2)
  elif sign== "^3":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("Processing...")
    print (num1**3)
  elif sign== "power":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    print("Processing...")
    print (num1**num2)
  elif sign== "sqrt":
    num1 = int(input("What is the number you seek the square root of? "))
    print("Processing...")
    print (sqrt(num1))
  elif sign== "!":
    num1 = int(input("What is the number you seek the factorial of? "))
    print("Processing...")
    print (factorial(num1))
  else:
    print("I am sorry, but I am unable to process your request.")
else:
  print("I am sorry, but that is not a valid command.")
