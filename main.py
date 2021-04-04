name = "CHOOSE_NAME"
age = 0
nameNew = "UNKNOWNUSER"
ageNew = 0

flx = input("Who are you?: ")
if flx == "CHOOSE_NAME":
  full = input("What's your full name?: ")
  if full == "CHOOSE_NAME":
    print("Hey, " + name + " you are " + str(age) + " years old.")
  print("-----------------------------")
  print("In 6 years you are " + str(age + 6))

elif flx != "CHOOSE_NAME":
 full = input("What's your full name?: ")
if full != "CHOOSE_NAME":
  print("-----------------------------")
  print("An error occured.") 
  print("You are not ..... and the right information will NOT be handed out.")
  print("-----------------------------")


while flx != "CHOOSE_NAME":
  print("Do you wanna try again?")
  again = input("Yes or No: ")
  if again == "Yes":  
    flx = input("Who are you?: ")
    if flx == "CHOOSE_NAME":
      full = input("What's your full name?: ")
      if full == "CHOOSE_NAME":
        print("----------------------------------------------")
        print("Hey, " + name + " you are " + str(age) + " years old.")
        print("-----------------------------")
        print("In 6 years you are " + str(age + 6))
        print("--------------------")
        print("Bye, " + name + "! Have a great time!")
        break;

    if flx != "CHOOSE_NAME":
      full = input("What's your full name?: ")
      if full != "CHOOSE_NAME":
        print("-----------------------------")
        print("An error occured.") 
        print("You are not ..... and the right information will NOT be handed out.")
        print("-----------------------------")
      elif full == "CHOOSE_NAME":
        break;
  elif again == "No":
    print("----------------------")
    print("Do you wanna quit??")
    stop = input("Yes or No?: ")
    print("-------------------")
    if stop == "Yes":
      print("Bye!")
      break;
