import random
def play():
   x = random.randint(1,6)
   y = random.randint(1,6)
   print(f'({x},{y})')
       

def intro():
    while True :
         i = input("Roll the dice ? (y/n):")
         if i == 'y' or i == "Y":
            play()
         elif i == 'n' or i == 'N':
           print("Thanks for Playing :)")
           break

         else:
           print("Invalid Choice !!")
 
intro()