
from random import choice
from time import sleep

points=0

def main():
    print_title()
    start_loop()

    
def print_title():
    print('')
    print("---- WELCOME TO ----------------------------")
    print("--------------------- PANDA SURVIVAL -------")
    print("")
    print("Try to collect 100 bamboo for Panda as fast as you can and win the main prize!")
    print("")

def start_loop():
    global points
    
    while True:      

        if points < 100:

            cmd=input('\n From where you want to get the bamboo?\n A- from another animal \n B- from the forest \n C- work for it \n [A,B or C]: ')
            cmd=cmd.lower()
            
            if cmd == "a":
                from_another_animal()
            elif cmd == "b":
                from_the_forest()
            elif cmd == "c":
                work_for_it()
            else:
                print('Unknown command. Try again')
        
        else:
            print("Congrats! You won a big bamboo tree for you and the Panda! \n")
            panda_picture()
            break

    return points

    

def from_another_animal():
    global points
    animals=['snake', 'turtle', 'monkey', 'rabbit', 'other panda']
    answers=[ "Hi! yes I have bamboo for you!", 
    "I have but I cannot share it. I keep it for later.", 
    "I can give you some if you guess my name. It's John, Julia or Jessie?"]
    
    the_animal=choice(animals)
    the_answer=choice(answers)

    print('Panda met a {} and it said: {}'.format(the_animal, the_answer))

    if the_answer== answers[0]:
        points += 20
        sleep(4)
        print('The nice animal gave you 20 bamboo and went away. Now you have {}.'.format(points))
    elif the_answer== answers[1]:
        points -= 10
        sleep(4)
        print ("The animal didn't share with you and you only wasted time and 10 bamboo. Now you have {}".format(points))
    elif the_answer== answers[2]:
        guess_name=input("Enter the name: ")
        sleep(4)
        guess_name=guess_name.lower().strip()

        if guess_name== "john" or guess_name== "julia":
            points -= 15
            print("Animal said: 'Sorry you didn't guess. I will not share with you this time.' Then it went away and you lost 15 bamboo. Now you have {}.".format(points))
        elif guess_name== "jessie":
            points += 20
            print("Animal said: 'Yes! That's right! I will give with you 20 bamboo.' Then it went away and you have 20 bamboo more so in general it's {}.".format(points))
        else:
            ("Hmm...I don't know that name.")


def from_the_forest():
    global points
    Times=["8 o'clock in the morning", "1 o'clock in the afternoon", "5 o'clock in the afternoon", "10 o'clock in the evening"]
    random_time=choice(Times)
    print("It's {}. Are you sure you want to go now to the forest?".format(random_time))
    decision=input("yes/no: ")

    if decision == "yes":
        if random_time == Times[0]:
            points -= 15
            print("8 in the morning? Surely it's not time for pandas. Your Panda also didn't find any bamboo in the forest and you lost 15 bamboo. Now you have {}.".format(points))
        elif random_time== Times[1]:
            points -= 15
            print("Hmm afternoon...beautiful sunshines... Panda decided to use that great weather and sunbathe instead of going to forest. You lost 15 bamboo and now you have {}.".format(points))
        elif random_time== Times[2]:
            points += 25
            print("That's the perfect time to take a walk into forest! Panda found 25 bamboo! Now you have {}.".format(points))
        elif random_time== Times[3]:
            points -= 35
            print("Oh no! Panda was lost in the forest and barely found the way back home! You lost 35 bamboo and now have {}".format(points))
        else:
            print("Error")
    
    elif decision == "no":
        None

    

def work_for_it():
    global points
    jobs= ['on cleaning a park', 'working in factory', 'in a library', 'as a postman']
    current_job= choice(jobs)
    print(" Panda spent almost a whole day {}. ".format(current_job))

    if current_job== jobs[0]:
        points += 25
        print('Great job! Panda earns 25 bamboo! Now you have {} bamboo. Not bad! \n'.format(points))
        
        print()
    elif current_job == jobs[1]:
        print('Panda was working hard many hours and is exhausted.')
        points -= 30
        sleep(4)
        print("For hard work you earn 50 bamboo but lose 20. Now you have {} bamboo.".format(points))
    elif current_job == jobs[2]:
        print('Panda was working in a library...if sleeping for the last 6h we can call "working".')
        points=points+ 50
        sleep(4)
        print("Panda said it's the favourite job. You earn 50 bamboo! Now you have {} bamboo.".format(points))
    elif current_job== jobs[3]:
        print("Panda did a loooot of kilometers on the bicycle and is barely alive.")
        points=points- 10
        sleep(4)
        print("It looks like Panda likes cycling but only to the nearest park. You lose 10 bamboo and now you have {}.".format(points))
    else:
        print("usp! some error!")

     
def panda_picture():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$**$$$$$$$$$**$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$'   ^$$$$$$F    *$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$     z$$$$$$L    ^$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$    e$$$$$$$$$e  J$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$eee$$$$$$$$$$$$$e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$b$$$$$$$$$$$$$$$$$$*$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$)$$$$P'e^$$$F$r*$$$$F'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$d$$$$  'z$$$$'  $$$$%  $3$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$*'''*$$$  .$$$$$$ z$$$*   ^$e*$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$'     *$$ee$$$$$$$$$$*'     $$$C$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$.      '***$$'''$$''        $$$$e*$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$b          '$b.$$'          $$$$$b'$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$c.         '''            $$$$$$$^$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$e..                     $$$$$$$$^$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$eeee..            J$$$$$$$$b'$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$r          z$$$$$$$$$$r$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'         z$$$$$**$$$$$^$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$*'          z$$$P'   ^*$$$ $$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$*'           .d$$$$       $$$ $$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$'           .e$$$$$F       3$$ $$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$.         .d$$$$$$$         $PJ$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$eeeeeeed$*''''**''         $\$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                  $d$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.                 $$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$e.              d$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$eeeeeee$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


main()
