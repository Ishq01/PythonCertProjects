class Category:
    cate = ""
    #Initializes each categories name and ledger
    def __init__(self, name):
        self.cate = name
        self.ledger = []

    #Deposits amount into categories ledger with desc
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    #Withdraws amount (if greater than current balance) into categories ledger with desc

    def withdraw(self, amount, description=""):
      if self.check_funds(amount):
        amount = float("-" + str(amount))
        self.ledger.append({"amount": amount, "description": description})
        return True
      else: return False

    #Gets balance by going thru amounts in ledger
    def get_balance(self):
        bal = 0.0
        for item in self.ledger:
            bal += float(item["amount"]) 
        return bal  

    #Transfer money from self to other category if enough funds
    def transfer(self, amount, otherCat):
      if self.check_funds(amount):
        description = "Transfer from " + self.cate
        otherCat.ledger.append({"amount": amount, "description": description})
        amount = float("-" + str(amount))
        description = "Transfer to " + otherCat.cate
        self.ledger.append({"amount": amount, "description": description})
        return True
      else: return False

    #Checks if amount is greater than or less than current balance
    def check_funds(self, amount):
      currentBalance = self.get_balance()
      if amount <= currentBalance: return True
      elif amount > currentBalance: return False

    #Prints the ledger into a grocery list
    def __str__(self):
      output = (self.cate).center(30, "*")  + "\n"
      for item in self.ledger:
        if len(item["description"]) > 22:
          desc = (item["description"])[:23]
        else:
          desc = (item["description"]).ljust(23)
        amt = str('{:.2f}'.format(item["amount"])).rjust(7)
        line = desc + amt + "\n"
        output += line
      total = "Total: " + str(self.get_balance())
      output += total
      return(output)

def create_spend_chart(categories):
  cates = []
  spending = []
  spent = 0
  #Creates a list of category names + spending per category
  for category in categories:
    cates.append(category.cate)
    for item in category.ledger:
      spent = 0
      if item["amount"] < 0:
        spent += int(item["amount"])
    spending.append(spent)
  total = sum(spending)
  #Changes amounts in spending to percents
  for num in spending:
    spending[spending.index(num)] = int((num / total) * 10) * 10
  #Length of longest string in cates
  longest = len(max(cates, key=len))  
  #Starts putting together output strings
  title = "Percentage spent by category" + "\n"
  #Sets length of each category to max
  for cate in cates:
    cates[cates.index(cate)] = cate.ljust(longest)
  #Prints all categories in a vertical line
  cateString = "     "
  for i in range(0, longest):
    for cate in cates:
      cateString += cate[i] + "  " #Two spaces between each category
    cateString += "\n     " #Categories start 5 spaces away from edge
  graph = ""
  for i in range(100, -10, -10):
    bar = " "
    line = str(i).rjust(3) + "|" #Want numbers to be right aligned
    #Add o if percent spending reaches there, spaces otherwise
    for percent in spending:
      if percent >= i:
        bar += "o  "
      else:
        bar += "   "
    line += bar
    graph += line + "\n"
    dashes = "    " + (len(cates) * 3) * "-" + "-" +  "\n"
    output = title + graph + dashes + cateString
  return output.strip() + "  "
