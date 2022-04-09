print("********* GUSSING NUMBER GAME *********")
print("     YOU HAVE ONLY 6 CHANCE TO WIN...!\n ")
from itertools import count
from os import times
import random


guess_number=random.randint(1,100)
count=0
while count<6:
    count+=1
    print("count :",count)
    no=int(input("Enter Your Guess Number :"))
    
    if no>guess_number:
        print("Gussing.....")
        print("Your Guessing Number Is Big " )
        print("Please Guess Another Number")
        print("\n")
        
        
    if no<guess_number: 
        print("Gussing.....")
        print("Your Guessing Number Is Small " ) 
        print("Please Guess Another Number")
        print("\n")
      
        
        
    if no==guess_number:
        print("Guessing.....")
        print("Congratulation Your Guessing Number Is Correct")  
        print("        ~~~~~~~* YOU WIN *~~~~~~~") 
        break
    if count==6:
        print("      You Try 6 Times") 
        print("******** GAME OVER ********") 
        