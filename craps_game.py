import random

point_set = False
bet = 10
bankroll = 1000
sim_win = 0
sim_lose = 0

print """
         Welcome to the 'Seven Star' casino!
         You are playing craps now,
         your started bankroll is '$1000',
         the started bet is '$10',
         command: 
              play(): "Rolling the dices"
              check_bankroll(): "Checking your current balance"
              all_in(): Showing "hand"
              set_bet(): "Setting a new bet"
              game(): "Check your game status"
"""

def roll():
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)
    print "You rolled", d1, "+", d2, "=", d1+d2
    return d1 + d2
    
def play():
    
    global point_set, bankroll, point
    global sim_win, sim_lose
    
    if bankroll < bet:
        print "Sorry, you can't play since you don't have enough money!"
        print """Do you wanna get more money?
                1: Yes
                2: No
              """
        choice = raw_input(">>")
        if choice == str(1):
            money = raw_input("How much do you wanna get?")
            bankroll += int(money)
            print "Your current bankroll is: ", bankroll
        if choice == str(2):
            print "Thanks for playing! See you next time!"
    else:
        if not point_set:
            print
            print "New game. Your bet is: ", bet
        
        # for the first roll
        r = roll()
        if not point_set:
            if r in (7, 11):
                bankroll += bet
                sim_win += 1
                print "Congratz! You Won! Your bankroll is: ", bankroll
            elif r in (2, 3, 12):
                bankroll -= bet
                sim_lose += 1
                print "Oops! You lost! Your bankroll is: ", bankroll
            else:
                point = r
                point_set = True
                print "Your point is", "[", point, "]"
        # for subsequence rolls
        elif r == 7:
            bankroll -= bet
            sim_lose += 1
            point_set = False
            print "You crapped out! Your bankroll is: ", bankroll 
        elif r == point:
            bankroll += bet
            sim_win += 1
            point_set = False
            print "You made your point! Your bankroll is: ", bankroll
                                   
def set_bet(inp):
    global bet, bankroll, point_set
    print
    if point_set:
        point_set = False
        bankroll -= bet
        print "Forfeiting current bet. Your bankroll is: ", bankroll
    bet = int(inp)
    print "New bet size is: ", bet

def all_in():
        set_bet(bankroll)
        
def check_bankroll():
    global bet
    print "Your current balance is: ", bankroll
    
def game():
    total = sim_win + sim_lose
    percent = float(sim_win)/total * 100
    print "So far, the games that you have been playing are: ", total 
    print "Won ", sim_win
    print "Lost ", sim_lose
    print "Overall, you have %d%% to win!" %percent
    
                                                          
