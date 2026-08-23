#input : Rock, paper, or scissors ? (r/p/s):
#you chose (choice with emoji) computer chose (choice with emoji) (who) Wins!!
#Continue ? (y/n)
import random
options = ("r","s","p")
#a dictionary can be used to map out the emojis
emojis = {"r":'🪨',"s":'✂️',"p":'📄'}

def get_user_choice():
    while True:
      choice = input("Rock, Paper or Scissors ? (r/p/s) : ")
      if choice in options:
         return choice
      else:
         print("Enter Valid Choice")
         

def display_choice(user_choice,computer_choice):
    print(f'You Chose : {emojis[user_choice]}')
    print(f'Computer Chose : {emojis[computer_choice]}')

def determine_winner(user_choice,computer_choice):
   wins_against = {'r':'s', 's':'p', 'p':'r'}
   if user_choice == computer_choice:
      print('TIE !')
   elif wins_against[user_choice] == computer_choice:
      print("YOU WIN!!!")
   else:
      print("YOU LOSE")

      
def play_again():
    while True:
        choice = input("Wanna Play Again (y/n) : ").lower()
        if choice == 'y':
            return True   # return destroyes the very loop it is in
        elif choice == 'n':
            print("Thanks For Playing")
            return False  # tells the main loop to stop 
        else:
            print("Invalid Choice. Please enter 'y' or 'n'.")
      
def game():
   while True:
      user_choice = get_user_choice()

      computer_choice = random.choice(options)

      display_choice(user_choice,computer_choice)

      print()

      determine_winner(user_choice,computer_choice)

      print()

      if play_again() == False:
         break

game()
