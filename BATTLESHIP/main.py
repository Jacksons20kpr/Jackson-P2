#Made by: Jackson Shangraw
#Date: February 7th 2024
#Purpose: 1 Player Battleship

#Grid Values
squares=["1a","1b","1c","1d","1e","2a","2b","2c","2d","2e","3a","3b","3c","3d","3e","4a","4b","4c","4d","4e","5a","5b","5c","5d","5e"]

answers=["□"] * len(squares)
ships=["Ship1","Ship2","Ship3"]
hits=["3c","3d","5a","5b","5c","1a","2a"]


#Battleship Grid
def print_board(squares):
       for i in range(0, len(squares), 5):
           print(" | ".join(squares[i:i+5]))    
          
          

spot = input("Pick a collumn and row")
if spot in hits:
       print("Hit!!!")  
       squares[squares.index(spot)] = "☑" 
#def print_board():       
        #print(f"{squares[0]} |  {squares[1]} | {squares[2]} | {squares[3]} | {squares[4]}")
        #print(f"{squares[5]} |  {squares[6]} | {squares[7]} | {squares[8]} | {squares[9]}")
        #print(f"{squares[10]} |  {squares[11]} | {squares[12]} | {squares[13]} | {squares[14]}")
       #print(f"{squares[15]} |  {squares[16]} | {squares[17]} | {squares[18]} | {squares[19]}")
        #print(f"{squares[20]} |  {squares[21]} | {squares[22]} | {squares[23]} | {squares[24]}")
      
print_board(squares)
if spot == hits or squares:
     print_board()


       
else:
        print("Miss!!!")
print_board(squares)
#if spot == "3c" or "3d" or "5a" or "5b" or "5c" or "1a" or "2a":
        #run=True
#else:
        #int(spot)== "3c" or "3d" or "5a" or "5b" or "5c" or "1a" or "2a":
    
 
   


#else:
#squares[spot]=answer[ spot]
#if answer[spot]=="N":
#misses=1 else:
#hits+=1
#else:
#print ("bad input")
