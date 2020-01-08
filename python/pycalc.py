help = input("PythonCalc V 1.3 by Sam Langer; Say 'help' for available commands, and to start the calculator. ")#Prompt for command help
if help== "help" or "Help": #If response help or Help, 
  print("Signs: '+', '-', '*', '/', 'sqr', 'sqrt', 'cube', '!', 'power'. ") #Print available operations
  sign = input("What operation should I use? ") #Prommpt for operation to use
  if sign== "+": #If prompt answered by "+":
    num1 = int(input("What is the first number? "))#Ask for first and second numbers
    num2 = int(input("What is the second number? "))
    print("Processing...") #Print processing...
    print (num1+num2) #Print the mathematical result
  elif sign== "-": #If user said "-"
    num1 = int(input("What is the first number? "))#Ask for first and second numbers
    num2 = int(input("What is the second number? "))
    print("Processing...") #Print processing...
    print (num1-num2) #Print the mathematical result
    #The program continues to ask for operations and numbers, and calculates them as shown above.
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
  else: #if user does not enter valid operation
    print("I am sorry, but I am unable to process your request.") #Print an error
else: #if user does not enter a valid command, 
  print("I am sorry, but that is not a valid command.") #Print and error.
