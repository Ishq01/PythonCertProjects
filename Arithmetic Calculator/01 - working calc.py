def arithmetic_arranger(problems, ans=False):
  #define variables used later
  ones = ''
  twos = ''
  dashes = ''
  answers = ''
  space = '    '
  #Checks number of problems (not to exceed 5)
  if (len(problems) > 5):
    return 'Error: Too many problems.'
  #Iterates through problems, splitting them
  for problem in problems:
    parts = (problem.split(' '))
    one = parts[0]
    sign = parts[1]
    two = parts[2]
    #Checks if lengths of operands are not greater than 4
    if (len(one) > 4) or (len(two) > 4):
      return 'Error: Numbers cannot be more than four digits.'
    #Checks if operands are ints
    if (not one.isnumeric()) or (not two.isnumeric()):
      return 'Error: Numbers must only contain digits.'
    #Checks if operators are + or -
    if (not sign == '+') and (not sign == '-'):
      return "Error: Operator must be '+' or '-'."
    #Set max length of each line, adding 2 bc of operator
    length = max(len(one), len(two)) + 2
    #Adds appropriate spaces to each line (length is how many spaces should be filled, starts with (one)/(two) and the remaining space is filled to the right)
    first = str(one).rjust(length) #Need new vars bc use one/two to calculate ans later
    second = sign + str(two).rjust(length - 1) #Subtracting one bc of sign
    if sign == '+':
      answer = str(int(one) + int(two)).rjust(length) #Need to convert to str bc of rjust
    elif sign == '-':
      answer = str(int(one) - int(two)).rjust(length) #Ans will never be longer than longer operand + 2
    dash = ''
    #Creates line of dashes
    for s in range(length):
      dash += '-'
    #To each string, appends new ones/twos + the 4 spaces
    ones += first + space
    twos += second + space
    dashes += dash + space
    answers += answer + space
  #Remove additional spaces to the right 
  #ones = ones.rstrip()
  #twos = twos.rstrip()
  #dashes = dashes.rstrip()
  #answers = answers.rstrip()
  #Checks value of answer to determine whether to include answers
  if not ans:
    arranged_problems = ones + '\n' + twos + '\n' + dashes
    return arranged_problems
  else: 
    arranged_problems = ones + '\n' + twos + '\n' + dashes + '\n' + answers
    return arranged_problems

print(arithmetic_arranger(["32 - 698", "3801 - 2", "45 + 43", "123 + 49"]))