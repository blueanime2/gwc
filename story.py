start = '''
You are walking down the street you see a small box at the end of the street you were intrested on opening the box
but it was locked?'''


keepplaying = "yes"
print(start)

while keepplaying == "yes" or keepplaying == "Yes":
    userChoice = input("What should you do? type 1 to look for the key. type 2 to breake the box.")
    if userChoice == "1":
        print("You find the key in a near by bush it was a beautiful key with a gold finish")
        print("Congrats you got a gold key yayyyyyyy")
        print("")
        keepplaying = "no"
    elif userChoice == "2":
        print("You threw the box on the ground and it bounced into a river which made you want an esspresso to cure your depression") 
        print("YOU FAILED!!!!!!!!!!!!!!!!") 
        keepplaying = input("would you like to try again? type yes or no")
    else:
        print("please use the choices......... boi 1 or 2")
        if keepplaying == "no":
            quit()
        else:print(start)    
      
keepplaying = "yes"
while keepplaying == "yes" or keepplaying == "Yes":
    userChoice == input("You looked at the key and its shiney beauty you go entranced by it that you dropped the box. type 1 to pick it up type 2 to leave it alone and take the key")
    if userChoice == "1":
        print(" you quickly pick the box up and opened it. you found a debit card and a note the note said the card had infinit amount of money till you give it to some one else")
        print(" you is rich boi congrats please pay my bills i need help")
        keepplaying = input(" thanks for playing would you like to play again? type yes or no")
    elif userChoice == "2":
        print(" you left the box where it was but then a curse was put on you now you live your day regreting on not opening that box")
        print(" you had your chance but noooooooooooooooooooo")
        keepplaying = input(" thanks for playing would you like to play again? type yes or no")
    if keepplaying == "no":
             quit()
   






































