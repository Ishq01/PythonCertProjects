def arithmetic_arranger(problems, b=False):
  #Checks number of problems (not to exceed 5)
  if len(problems) > 5:
      return("Error: Too many problems.")
  #Iterates through problems
  for problem in problems:
      parts = problem.split()
      #Checks if numbers are ints
      if parts[0].isdigit() and parts[2].isdigit():
          x=1
      else:
          return("Error: Numbers must only contain digits.")
      #Checks length of each part (not to exceed 4)
      if len(parts[0]) > 4 or len(parts[2]) > 4:
          return("Error: Numbers cannot be more than four digits.")
      else:
          x=1
      #Checks if operation signs are +/-
      if parts[1] == "+" or parts[1] == "-":
          x=1
      else:
          return("Error: Operator must be '+' or '-'.")

  #Declaring lists and variables
  one = []
  two = []
  sign = []
  three = []
  dashes = []
  space = 0

  #If there are no errors, then starts printing the problems
  for problem in problems:
      #Separates each part into a different list
      parts = problem.split()
      one.append(parts[0])
      sign.append(parts[1])
      two.append(parts[2])
      #If user requests answer, then calculate and append to list
      if b == True:
          if parts[1] == "+":
              ans = int(parts[0]) + int(parts[2])
          elif parts[1] == "-":
              ans = int(parts[0]) - int(parts[2])
          three.append(ans)

  output = ""
  #Prints first line of arithmetic problems: Calculates difference between two lengths of two operands, including the sign, for the bottom one
  for x in range (0, len(one)):
      if len(two[x]) >= len(one[x]):
          space = len(two[x]) - len(one[x]) 
      else:
          space = 0
      #In order to get the proper number of characters (length of number + spaces), adds characters to the beginning of the number 
      output += ('{:>{width}}'.format(one[x], width=space + len(one[x]) + 2)) + "    "
  output = output.rstrip() + "\n"
  #Prints second line of arithmetic problems: Calculates difference between two lengths of two operands, including the sign, for the bottom one
  for x in range (0, len(two)):
      if len(one[x]) > len(two[x]):
          space = len(one[x]) - len(two[x])
      else:
          space = 0
      output += sign[x] + " " + two[x].rjust(space + len(two[x]), " ") + "    "
  output = output.rstrip() + "\n"
  #Prints the line of dashes: Calculates the number of dashes required and appends to list for optional answers
  for x in range (0, len(two)):
      if len(one[x]) >= len(two[x]):
          dash = len(one[x]) + 2
          dashes.append(dash)
      else:
          dash = len(two[x]) + 2
          dashes.append(dash)
      output += ("-" * dash) + "    " 
  output = output.rstrip() + "\n"
  #Prints line of optional answers based on dashes list
  if b == True:
      for x in range (0, len(three)):
          ans = str(three[x])
          output += ('{:>{width}}'.format(ans, width=dashes[x])) + "    "
  return output.rstrip()
  
print(arithmetic_arranger(["32 - 698", "3801 - 2", "45 + 43", "123 + 49"], True))