comp = ("Computer's Turn to choose Rock, Paper, Scissor ")
print(comp)
def game(comp, You ):
   if comp == You:
       return None 
   elif comp == 'r':
      if You == 's':
        return False
      elif You == 'p':
        return True
   elif comp == 's':
       if You == 'p':
         return False
       elif You == 'r':
         return True
   elif comp == 'p':
       if You == 'r':
         return False
       elif You == 's':
         return True   

import random
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'   
elif randNo == 3:
    comp = 's'  
print("Computer have chosen\n ")           
You = (input("Your Turn to choose : Rock(Press: r) - Paper(Press: p) - Scissor(Press: s)\n"))
print (f"Computer chose {comp}")
print (f"You have chosen {You}")
a = game(comp, You )
if a == None:
    print("The Game is a Tie!")
elif a == True:
    print ("You Win!")
else:
    print ("You Lost!")      
