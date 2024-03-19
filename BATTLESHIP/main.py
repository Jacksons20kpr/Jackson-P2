#Made by: Jackson Shangraw
#Date: February 7th 2024
#Purpose: 1 Player Battleship

#Grid Values
squares=["1a","1b","1c","1d","1e","2a","2b","2c","2d","2e","3a","3b","3c","3d","3e","4a","4b","4c","4d","4e","5a","5b","5c","5d","5e"]

answers=["□"] * len(squares)
hits=["3c","3d","5a","5b","5c","1a","2a"]
num_hits_left=len(hits)

#Battleship Grid
def print_board(squares):
       print(f"hits left:{num_hits_left}")
       for i in range(0, len(squares), 5):
           print(" | ".join(squares[i:i+5]))    
          




while True:
    print_board(squares)
    spot = input("Pick a collumn and row: ")

    if spot in hits:
        print("Hit!!!")
        num_hits_left-=1  
        squares[squares.index(spot)] = "☑"
    else:
        print("Miss!!!")
        squares[squares.index(spot)] = "☒"  

    if num_hits_left ==0:
     print ("You Win!!!")
     break

#else:
#squares[spot]=answer[ spot]
#if answer[spot]=="N":
#misses=1 else:
#hits+=1
#else:
#print ("bad input")

