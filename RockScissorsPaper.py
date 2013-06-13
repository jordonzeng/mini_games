import random

def number_to_name(num):
    if num == 0:
        return "rock"
    elif num == 1:
        return "scissors"
    elif num == 2:
        return "paper"
        
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "scissors":
        return 1
    elif name == "paper":
        return 2
        
def game():
    player = raw_input("Enter your choice >>")
    computer = random.randrange(0,3)
    print "Player chooses: ", player
    print "Computer chooses: ", number_to_name(computer)
    
    if (name_to_number(player)+1)%3 < computer:
        print "Player win"
    elif name_to_number(player) == computer:
        print "Tie"
    else:
        print "Computer win"
