import random


def win(computer_number,guess):
    return computer_number==guess


def get_a_guess():
    res=input("whats your guess?")
    return int(res)

def answer(computer_number,guess):
    if computer_number > guess:
        return "my number is higher than your guess"
    if computer_number < guess:
        return "my number is lower than your guess"
    return "Woow! you won! Good Guess!"

def finish(computer_number,count):
    print("good game dude!")
    print(f"my number was {computer_number}!")
    print(f"you can won this game with {count} try.")
    ans=input("do you want to try it again ;) ?! (Y/N)")
    if ans.upper() in ["Y","YES"," YEAH","BALE","OK", "I WANT"]:
        return True
    else:
        return False

        


continue_playing=True


while (continue_playing):

    computer_number=random.randint(1,20)

    guess=0 

    count=0
    while (not win(computer_number,guess)):
      
        guess=get_a_guess()
        count+=1

        print(answer(computer_number,guess))

    continue_playing=finish(computer_number,count)    