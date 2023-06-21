import time
import random

def print_pause(a, T):
    print(a)
    time.sleep(T)
    return a

total_score = 0 
materials = 0 
cont = 0 
foods = 0
ft = 0
misd=False #knowing if the mission in the player's tool is donr or not
weapon = False
health = 100
yn = True #a variable for players tools to check if the player chosed y or n
endvl = 0 #the choice of end variable
nums= 0#for counting number of games played

def main():
    global total_score,materials,cont,foods,ft,misd,weapon,health,yn,endvl
    ###description of the game start
    """
    print("  ")
    print_pause (" Good morning , dear passengers!" , 1.5)
    print_pause(" Welcome to our cruise number 613." , 2)
    print_pause(" Have a nice trip." , 3.5)
    print("  ")
    print_pause("You are sitting watching the sea." , 3)
    print_pause("Suddenly the ship crash into some rocks." , 1)
    print_pause("And about to sink in the middle of the ocean!" , 2.5)
    print("   ")
    print_pause("Now you have to escape !!" , 2)
    print_pause("You escaped succesfuly with someother people." , 2 )
    print("   ")
    print_pause("NOW",2.5)
    print_pause("you are on an island and You are the leader." , 1.5)
    print("   ")
    """
    def cho (g , h) :
        global total_score,cont
        while True:
            choice = input("Choose 1 or 2: ")
            if choice == "1":
                chos1 = g
                print_pause(chos1 , 1.5)
                cont = 1
                break
            elif choice == "2":
                chos2 = h
                print_pause(chos2 , 1.5)
                cont = 2
                break
            else:
                print("Invalid input. Please choose 1 or 2.")

    def plant():
        global foods
        foods = foods - 10
        return "You planted some Food"

    def food (stat):
        global total_score,foods,health
        if stat == "collect" :
            total_score = total_score + 5
            foods = foods + 5
            health = health + 5
            return "You collected some food."
        elif stat == "wolfs" :
            total_score = total_score - 5
            foods = foods - 5
            return "The wolfs eat most of your food."
        elif stat == "Eat" :
            total_score =total_score + 3
            health = health + 5
            return "You eat some food and got some energy."

    def ship() : # printing function
        global total_score,materials,misd
        vr = matr_check(materials,150)
        if vr == 1:
            print_pause("You can build the ship now\nBuilding the ship...",3.5)
            print_pause("You made one of three things required for plan (1)",2)
            misd = True
        elif vr == 2:
            print_pause("You need more materials to go on",1.6)
            misd = False

    def wolfs () :
        global total_score,health,materials,misd,weapon
        if weapon == True :
            if health >= 60:
                fu = "you see wolfs and you have"
                "weapons so you could kill some of them."
                time.sleep(2)
                total_score += 5
                misd = True
                return fu
            elif health < 60:
                fu = "You see wolfs and you have weapons but you are weak"
                "\nSo you just run away\nbut you have some loses in materials"
                time.sleep(2)
                total_score -= 3
                materials -= 5
                misd = True
                return fu 
        elif weapon == False :
            fu = "you see wolfs but you dont have weapons so"
            "they chase you and kill someone."
            print("   ")
            time.sleep(2)
            health = health - 7
            total_score -= 5
            misd = False
            return fu

    def gift() : # printing function
        global total_score,materials,foods,health
        if total_score >= 15 :
            print_pause("congrates! You have got a gift." , 1.6)
            #random gifts
            gifts = { "wood" , "materials" , "food" , "score" , "health" }
            gf = random.choice(gifts)
            print_pause(("You won " , gf) , 1.5)
            if gifts == "wood":
                materials = materials + 7
            elif gifts == "materials":
                materials = materials + 10
            elif gifts == "food":
                foods = foods +15
            elif gifts == "score":
                total_score += 20
            elif gifts == "health":
                health += 10
            #clear old score
            total_score = total_score - 15
            print("Score: ",total_score)
            time.sleep(1.5)

    def won_lose() : # printing function
        if (materials>= 300) and (ship()== 1) and (health>= 70) and (foods>=100):
            print_pause("You are now ready to leave." , 1.5)
            print_pause("You now left the island, you can see a ship." , 2)
            print_pause("you are rescued!" , 2)
            print_pause("___You win___" , 4)
        elif (health <= 0) or (foods <= 0):
            print_pause("You lose the game",3)
        else:
            print_pause("You are not ready yet",2)

    def camp (st , type_attack) :# printing function
        global total_score,materials,health,misd
        if st == "improve" :
            print_pause("You need 20 materials to improve your camp",1.5)
            print_pause("Checking materials...",2.5)
            jo = matr_check(materials,20)
            if jo == 1:
                print_pause("Your camp has been improved.",1.5)
                total_score = total_score + 5
                health = health + 5
                misd = True
            elif jo == 2:
                print_pause("You can't improve your camp",1.5)
                total_score -= 2
                misd = False
        elif st == "attack" :
            if type_attack == "strong":
                print_pause("Your camp has been damaged.",1.5)
                total_score = total_score - 5
                health = health -3
            elif type_attack == "weak":
                print_pause("You have some loses in your camp.",1.5)
                total_score -= 2
                health = health -1

    def discover_island (time) :
        global total_score,materials,health,disc,misd
        if time == "day" :
            if health >= 70 :
                vs1="You discovered a new place and found important items."
                materials = materials + 7
                total_score = total_score + 7
                misd = True
                return vs1 
            elif health < 70 :
                vs2 = "You couldn't walk a lot in the island, so you go back."
                total_score =total_score - 1
                misd = False
                return vs2 
        elif time == "night" :
            vs3 = "You meet wolfs"
            if health >= 70 :
                vs4 = wolfs()
                total_score =total_score + 7
                misd = True
            elif health < 70 :
                vs4 = wolfs()
                total_score =total_score - 3
                misd = False
            return vs3 , vs4

    def collect_matr(type) :
        global materials
        if type == "wood" :
            rt1 = "You collected some wood!"
            materials = materials +7
            return rt1
        elif type == "lost":
            rt2 = "you could collect some of your lost things in the sea."
            materials = materials +10
            return rt2
        elif type == "other":
            rt3 = "You collected some important items."
            materials = materials +8
            return rt3

    def player_tools():# printing function
        global total_score,materials,foods,health,yn, ft,misd,weapon
        print("Do you want player's tools?")
        while True:
            fg = input("Enter y or n : ")
            if fg == "y":
                print("\n1) Collect materials   2) Make guns/weapons",
                            "   3) Feed your group   4) Improve your camp",
                            "\n5) Discover island  6)Build a ship  7) Random Gift",
                            "\n8)Check if you won or lose   9)Plant Food",
                            "    10)Increase health")
                time.sleep(2)
                print("    ")
                print("    ")
                while True :
                    choss = input("Enter a number : ")
                    print("   ")
                    if choss == '1' :
                        while True:
                            tr = input("Write:\n*wood\n*lost\n*other\n")
                            if (tr == "wood")or(tr == "lost")or(tr == "imp"):
                                fk = collect_matr(tr)
                                print_pause(fk,2)
                                print("   ")
                                misd = True
                                break
                            else :
                                print("try again")
                        ft=1
                        break
                    elif choss == '2':
                        print_pause("You need 12 material to make weapons",1.5)
                        while True:
                            kl = matr_check(materials,12)
                            if kl == 1:
                                print_pause("Making Guns....",3)
                                materials = materials - 12
                                print_pause("You now have guns to"
                                            "defend your group against wolfs",2)
                                print("Your materials: ",materials)
                                weapon = True
                                misd = True
                                print("Score: ",total_score)
                                time.sleep(1.5)
                                break
                            elif kl == 2:
                                print("    ")
                                lucky_wheel(1,12,12)
                                print("    ")
                                print("Score: ",total_score)
                                time.sleep(1.5)
                        ft=2
                        break
                    elif choss == '3':
                        food("Eat")
                        ft=3
                        misd = True
                        break
                    elif choss == '4':
                        camp("improve","m")
                        print("Score: ",total_score)
                        time.sleep(1.5)
                        ft=4
                        break
                    elif choss == '5':
                        fd = input("Time 'day or night' :")
                        if fd == "day":
                            if health >= 50 :
                                print(discover_island("day"))
                            elif health < 50 :
                                print(discover_island("day"))
                            else:
                                print("try again")
                        elif fd == "night":
                            if health >= 50 :
                                print(discover_island("night"))
                            elif health < 50 :
                                print(discover_island("night"))
                            else:
                                print("Try again")
                        else:
                            print("Try again")
                        ft=5
                        break
                    elif choss == '6':
                        print_pause("Checking materials..." , 3)
                        ship()
                        ft=6
                        break
                    elif choss == '7':
                        gift()
                        ft=7
                        break
                    elif choss == '8':
                        won_lose()
                        print("Score: ",total_score)
                        time.sleep(1.5)
                        ft=8
                        break
                    elif choss == '9':
                        plant()
                        ft=9
                        break
                    elif choss == '10':
                       print_pause("You will lose 5 score for each 1 health",2)
                       if health == 100:
                           print_pause("Your health is 100",1.7)
                       elif health < 100:
                           while True:
                               kj = input("Enter the number of",
                                       " health points you want: ")
                               if kj.isdigit() :
                                   kj = int(kj)
                                   print_pause("Recharging health ...",3)
                                   health += kj
                                   materials -= kj*5
                                   print("your health: ",health)
                                   misd = True
                               else:
                                   print("invalid input input")
                               break
                       print("Score: ",total_score)
                       time.sleep(1.5)
                       ft=10
                    else:
                        print("invalid input try again")
                yn = True
                break       
            elif fg == "n":
                print_pause("OK",1.5)
                print("Score: ",total_score)
                time.sleep(1.5)
                yn = False
                break
            else :
                print("Invalid input try again")

    def matr_check(fu,num):# printing function
        global materials,foods,total_score,health
        print("Yours : ",fu) 
        if fu >= num :
            print_pause("They are enough ",1.8)
            return 1
        elif fu < num:
            print_pause("You don't have enough ",1.5)
            return 2

    def lucky_wheel(start,end,target):# printing function
        global health, materials , cont
        print_pause("Let's play the lucky wheel!",1.5)
        print("   ")
        print("Warning! \nEach time you spin the"
                " wheel You will lose 1 health")
        time.sleep(1.5)
        print("   ")
        print_pause("Do you want to coninue?\n1 fo yes,2 for no",1.5)
        cho("","Find other way to do your mission")

        if cont == 1:
            while True :
                if materials >= target:
                    print("   ")
                    print_pause("You reached your target",1.8)
                    print("Helath: ",health)
                    time.sleep(1.5)
                    break
                elif materials < target:
                    iu = input("Press Enter")
                    health = health -1
                    fg = list(range(start,int(end)))
                    fd = random.choice(fg)
                    materials = materials + fd
                    print("Your materials : ", materials)
        return materials
    
    #first choices(different from rest)
    """
    print_pause("If you want to discover island, Enter (1) " , 1)
    print("If you want to collect some food and other things"
           " from the near bags in the sea, Enter (2)")
    time.sleep(1)

    cho ((discover_island("day")) , (collect_matr("lost")))

    print("   ")
    print_pause(("The night is near and you have"
                " to find a place to sleep."), 2.5)
    print("   ")
    print_pause("if you want to sleep in the near cave, Enter (1)" , 1)
    print_pause("if you want to build a camp, Enter (2)" , 1)
    
    while True :
        choz = input("Enter 1 or 2 : ")
        if choz == '1' :
            print("You find old things it looks like someone lived here!")
            time.sleep(1.5)
            print_pause(collect_matr("imp") , 1.5)
            print_pause("You sleep there until sunrise.", 1.5)
            total_score += 5
            print("Score : ", total_score)
            cont1 = 1
            break
        elif choz == '2':
            print("You are so weak but you're trying."
                  " While building your camp ")
            time.sleep(1.5)
            print_pause(wolfs() , 1.5)
            print_pause(("You will have to make guns later to protect you."
                         "\nNow You have to escape"),1.5)
            print("You runs away until you find a huge tree",
                " so you all climbed it to hide until sunrise.")
            time.sleep(1.5)
            total_score -= 3
            print("Score : ", total_score)
            cont1 = 2
            break
        else:
            print("Invalid input, Please choose 1 or 2 ")
    
    print_pause("   " , 1.5)
    print("****")
    print_pause("time:day\nMission : Feed your group",2)
    print("   ")

    if cont1 == 1:
        print_pause("If you want to go out to forest"
                     "and get some food, Enter 1",1)
        if cont == 1:
            print("If you want to go to the sea to search for food"
                 "from the sunk ship, Enter 2")
            time.sleep(1.5)
            cho(food('collect'), 'You collected some food')
            print_pause('you can eat now',1.5)
        elif cont == 2:
            print("If you want to eat some of the food you collected"
                 "before and save some energy, Enter 2")
            time.sleep(1.5)
            cho((food("collect"), "You can eat now"),
                ('You can eat now, and you saved some energy!'))
        print("Score: ",total_score)
    elif cont1 == 2:
        print_pause("You can see trees full of fruits around you", 1.5)
        print_pause("If you want to collect some fruit, Enter 1", 1.5)
        if cont == 1:
            print("If you want to go to the sea to",
                "search for food from the sunk ship, Enter 2")
            time.sleep(1.5)
            cho(food('collect'),'You collected some food')
            print("You can eat now")
        elif cont == 2:
            print("If you want to go back to the beach and search",
                "for the food you collected, Enter 2")
            time.sleep(1.5)
            t1 = food('collect'), 'You can eat now'
            t2 = food('wolfs'),"You are very hungry and starving,so you had"
            " to eat any thing\n some of you got ill and one died."
            cho(t1,t2)
    
    print(' ')
    print("****")
    print("Now we want to discover the island for materials to build our camp")
    time.sleep(1.5)
    print("   ")
    print_pause("You need 30 materials to build " , 1.5)
    print("Your materials are : ", materials)
    print("    ")

    while True:
        if materials >= 30 :
            print_pause("Building the camp....",4)
            print_pause("You build an amazing camp in the beach!",1.5)
            materials = materials - 30
            print("Your materials: ",materials)
            time.sleep(1.5)
            break
        elif materials < 30 :
            print_pause("You don't have enough materials,"
                         "collect materials" , 1.5)
            print("    ")
            lucky_wheel(1,20,30)
            if cont == 2:
                print_pause("Mission failed",1.8)
                break
    
    print("   ")
    print("***")
    print_pause("Next mission : Make guns",2.1)
    print("Score: ",total_score)
    time.sleep(1.5)
    print_pause("You should have 12 materials to make enough guns ",2)
    print("  ")
    
    while True:
        kl = matr_check(materials,12)
        if kl == 1:
            print_pause("Making Guns....",3)
            materials = materials - 12
            print_pause("You now have guns to defend"
                            "your group against wolfs",2)
            print("Your materials: ",materials)
            weapon = True
            print("Score: ",total_score)
            time.sleep(1.5)
            break
        elif cont == 2:
            print("    ")
            print_pause("Mission failed",1.5)
            break
    """         
    print("    ")

    #Random missions for one day in a function
    def days ():
        global total_score,weapon,misd,yn
        n = 1 # variable for determinig the time based on
        #the number of activities done through the day
        mis1 = "Food for group"
        mis2 = "Improve your camp"
        mis3 = "collect materilas"
        mis4 = "Discover island"
        mis5 = "Wolfs attack"
        missions = [ mis1,mis2,mis3,mis4,mis5 ]    
        for tr in list(range(1,6)):
            print("    \n****\n   ")        
            if n <= 3:
                print_pause("Time : day",1.5)
            elif n > 3:
                print_pause("Time : night",1.5)
            time.sleep(1.5)
            choicel = random.choice(missions)
            print("Mission : ", choicel)
            print("Tip : Use player's tools")
            print("    ")
            if choicel == mis5:
                print_pause(wolfs(),2)
            else:
                player_tools()
            missions.remove(choicel)
            if yn == True :
                if mis1 == choicel:
                    if ft == 3:
                        if misd == True:
                            print_pause("Mission completed",1.8)
                            total_score += 7
                        elif misd == False:
                            print_pause("Mission Failed",1.8)
                            total_score -= 3
                        else:
                            print_pause("Uncorrect choose",2)
                            total_score -= 3
                elif mis2 == choicel:
                    if ft == 4:
                        if misd == True:
                            print_pause("Mission completed",1.8)
                            total_score += 7
                        elif misd == False:
                            print_pause("Mission Failed",1.8)
                            total_score -= 3
                    else:
                        print_pause("Uncorrect choose",1.5)
                        total_score -= 3
                elif mis3 == choicel:
                    if ft == 1:
                        if misd == True:
                            print_pause("Mission completed",1.8)
                            total_score += 7
                        elif misd == False:
                            print_pause("Mission Failed",1.8)
                            total_score -= 3
                            print_pause("Uncorrect choose")
                        total_score -= 3
                elif mis4 == choicel:
                    if ft == 5:
                        if misd == True:
                            print_pause("Mission completed",1.8)
                            total_score += 7
                        elif misd == False:
                            print_pause("Mission Failed",1.8)
                            total_score -= 3
                    else:
                        print_pause("Uncorrect choose")
                        total_score -= 3
            elif mis5 == choicel:
                if misd == False:
                    print_pause("Mission failed",1.8)
                    total_score -=2
                elif misd == True:
                    print_pause("Mission completed",1.9)
                    total_score += 5
            elif yn == False :
                print_pause("Mission Failed",2)
                total_score -= 5
            misd = False
            yn = False
            n += 1

    while True:
        print("    ")
        print_pause("Do you want to do daily messions or plan to leave island ?",2)
        print_pause("-It will increase your score-",2)
        jh = input("1 for missions\n2 for planing\n")
        print("    ")
        if jh == '1':
            days()
        elif jh == '2':
            break
        else:
            print("try again")

    "The End situations"
    print("***")
    print_pause("You study a plan to survive",2)
    print("   ")
    #tell the story 
    print_pause("You need:\n1) 100 Food\n2)300 Materials"
                 "\n3)Health more than or equal to 70\n4)A ship",3.6)
    print("   ")
    print("Score: ",total_score)
    time.sleep(1.5)
    for te in list(range(1,5)):
        print_pause("\nTo check food, Enter 1\nTo check Materials, Enter 2"
                    "\nTo check Health, Enter 3\nTo Build the ship,Enter 4",3.5)
        print("   ")

        while True:
            gh = input("Enter a number: ")
            if gh == '1':
                #food
                if matr_check(foods,100) == 2:
                    print_pause("Collect some food\n i.e "
                                "From forest or plant some",2)
                    while foods < 100:
                        print_pause("Choose 1 for forest and 2 for plant",1.7)
                        cho(food("collect"),plant())
                        if cont == '1':
                            foods = foods + 5
                            total_score = total_score - 3
                            print("Score: ",total_score)
                            break
                        elif cont == '2':
                            foods = foods + 10
                            materials = materials - 3
                            print("Score: ",total_score)
                            break
                        matr_check(foods,100)
                    print_pause("Your food is ready",2)
                    print("    ")
                    print("Food: ",foods)
                    print("Score: ",total_score)
                    print("materials: ",materials)
                elif matr_check(foods,100) == 1: 
                    print_pause("Your food is ready",2)
                    print("    ")
                    print("Food: ",foods)
                    print("Score: ",total_score)
                    print("materials: ",materials)
                break
            elif gh == '2':
                #materials
                hg = matr_check(materials,300)
                if hg == 2:
                    print_pause("Collect some materilas"
                                "\ni.e From forest,sea or cave",2)
                    while materials < 300:
                        print_pause("Choose 1 for forest,"
                                    "2 for sea and 3 for cave",1.7)
                        while True:
                            yu = input("Choose 1 or 2 or 3: ")
                            if yu == '1':
                                f1 = collect_matr("wood")
                                print_pause(f1,2)
                                total_score -= 3
                                print("Score: ",total_score)
                                break
                            elif yu == '2':
                                f2 = collect_matr("lost")
                                print_pause(f2 , 2)
                                health -= 2
                                print("Health: ",health)
                                break
                            elif yu == '3':
                                f3 = collect_matr("imp")
                                print_pause(f3,2)
                                total_score -= 2
                                print("Score: ",total_score)
                                break
                            else:
                                print("invalid input try again")
                        matr_check(materials,100)
                    print_pause("Your materials are ready",2)
                    print("materials: ",materials)
                    print("Score: ",total_score)
                elif hg == 1:
                    print_pause("Your materials are ready",2)
                    print("materials: ",materials)
                    print("Score: ",total_score)
                break
            elif gh == '3':
                #Health
                if matr_check(health,70) == 2:
                    print_pause("Increase health",2)
                    while health < 70:
                        print_pause("You will lose 5 score for each 1 health",2)
                        lk = 70 - health
                        health += lk
                        total_score -= lk*5
                    print_pause("Your health is ready",2)
                    print("Score: ",total_score)
                elif matr_check(health,70) == 1:
                    print_pause("Your health is ready",2)
                    print("Health: ",health)
                break
            elif gh == '4':
                #ship
                ship()
                break
            else:
                print("try again")

    won_lose()
    print("       ")
    print("       ")
    print_pause("___The End___",5)
    print("Congrates you finished the game succesfully")
    print("    ")
    print("Score: ",total_score)
    time.sleep(1.5)
    print("   \n   ")
    time.sleep(2.5)

main()
    
while True:
    rt = input("Do you want to play again ?\n Enter y or n: ")
    if rt.lower() == 'y':
        main()
        nums += 1
        print("Number of played games: ",nums)
    elif rt.lower() == 'n':
        print("You exited the game")
        print("Number of played games: ",nums)
        break
    else:
        print("Invalide input try again")

#test player's tools and days()