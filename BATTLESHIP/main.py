#Made by: Jackson Shangraw
#Date: February 7th 2024
#Purpose: 1 Player Battleship

#Grid Values
squares=["1a","1b","1c","1d","1e","2a","2b","2c","2d","2e","3a","3b","3c","3d","3e","4a","4b","4c","4d","4e","5a","5b","5c","5d","5e"]
squares2=["1a","1b","1c","1d","1e","2a","2b","2c","2d","2e","3a","3b","3c","3d","3e","4a","4b","4c","4d","4e","5a","5b","5c","5d","5e"]

answers=["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
ships=["Ship1","Ship2","Ship3"]
hit=["3c","3d","5a","5b","5c","1a","2a"]
hit=["☒","☒","☒"]

#Battleship Grid
print(f"{squares[0]} |  {squares[1]} | {squares[2]} | {squares[3]} | {squares[4]}")
print(f"{squares[5]} |  {squares[6]} | {squares[7]} | {squares[8]} | {squares[9]}")
print(f"{squares[10]} |  {squares[11]} | {squares[12]} | {squares[13]} | {squares[14]}")
print(f"{squares[15]} |  {squares[16]} | {squares[17]} | {squares[18]} | {squares[19]}")
(f"{squares[20]} |  {squares[21]} | {squares[22]} | {squares[23]} | {squares[24]}")

spot = input("Pick a collumn")
if spot == "3c" or "3d" or "5a" or "5b" or "5c" or "1a" or "2a" or spot == "3c" or "3d" or "5a" or "5b" or "5c" or "1a" or "2a":
        run=False
else:
        if int(spot)==1:
            print("you picked 1")
 
print("Which Collumn?:")
while True: 
    try:
        print("Which Row?:")
    except:
        print("Coordinates Only")

    break 

#while True:

choice = input ("What is your choice:").upper()
#if choice in #options:
spot = squares.index(choice)
#if spot ==-1:
#print ("spot already guessed")
#else:
#squares[spot]=answer[ spot]
#if answer[spot]=="N":
#misses=1 else:
#hits+=1
#else:
#print ("bad input")
