print("it is late. do you go to SLEEP, or stay AWAKE.")
choice = input()
if choice == 'sleep':
    print("you wake up the next morning")
elif choice == 'awake':
    print("you stay awake as it gets darker. you eventually fall asleep")
else:
    print(choice, "wasn't a valid choice")

print("after you wake up, will you go STUDY or play GAMES?")
choice = input()
if choice == 'study':
    print("you study python and gain more knowledge")
elif choice == 'GAMES':
    print("you play videogames for a few hours")
else:
    print(choice, "wasn't a valid choice")

print("you are hungry. will you eat something HEALTHY or something UNHEALTHY but good?")
choice = input()
if choice == 'healthy':
    print("you eat something healthy and gain strenght")
elif choice == 'unhealthy':
    print("you eat something unhealthy and gain weight")
else:
    print(choice, "wasn't a valid choice")

print("do you want to go OUTSIDE or stay INSIDE?")
choice = input()
if choice == 'outside':
    print("you go outside, but it starts raining")
elif choice == 'inside':
    print("you stay inside")
else:
    print(choice, "wasn't a valid choice")

print("its getting late, do you go to BED, or eat DINNER?")
choice = input()
if choice == 'BED':
    print("you go to bed and fall asleep")
elif choice == 'dinner':
    print("you eat dinner and go to bed very late")
else:
    print(choice, "wasn't a valid choice")