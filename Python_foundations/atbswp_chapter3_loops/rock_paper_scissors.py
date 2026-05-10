import random

wins = 0
losses = 0
ties = 0
valid_moves = ["r","p","s","q"]
pc_valid_moves = ["r","p","s"]

def your_move():
    while True:
        move = input("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit\n")
        if move not in valid_moves:
           print("Please enter a valid move")
        else: 
            if move == "s": print("SCISSORS VS...\n")
            if move == "r": print("ROCK VS...\n")
            if move == "p": print("PAPER VS...\n")                  
            break
    return move

def ai_move():
    pc_move = random.choice(pc_valid_moves)
    if pc_move == "s": print("SCISSORS!\n")
    if pc_move == "r": print("ROCK VS!\n")
    if pc_move == "p": print("PAPER VS!\n")
    return pc_move

def compare(move, pc_move, wins, losses, ties):
    if move == "r" and pc_move == "r" or move == "s" and pc_move == "s" or move == "p" and pc_move == "p": 
        ties += 1 
        print("It's a tie!")
    if move == "r" and pc_move == "s" or move == "s" and pc_move == "p" or move == "p" and pc_move == "r":
        wins += 1 
        print("You win!")
    if move == "r" and pc_move == "p" or move == "s" and pc_move == "r" or move == "p" and pc_move == "s": 
        losses += 1 
        print("You lost!")
    return wins, losses, ties

def main ():
    global wins, losses, ties
    print("ROCK, PAPER, SCISSORS")
    while True:
        move = your_move()
        if move != "q":
            pc_move = ai_move()
            wins, losses, ties = compare(move, pc_move, wins, losses, ties)
            print(f"{wins} Wins, {losses} Losses, {ties} Ties")
        else: break

main()