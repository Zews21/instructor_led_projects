#Calculator
import art

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
print(art.logo)

def calculator():
  

  
  running = True
  num1 = float(input("What is the first number?: "))
  
  for symbol in operations:
    print(symbol)
  
  while running:
  
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?:"))
    calculation_func = operations[operation_symbol]
    answer = calculation_func(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      running = False
      calculator()

calculator()
