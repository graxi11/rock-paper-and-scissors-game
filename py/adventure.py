name = input('Type in your name: ')
print('welcome', name, 'to this Adventure!')

answer = input(
    'you are on a dirt road, it has come to an end and you can go (left/right). which way would you like to go? ').lower()

if answer == 'left':
    #LEFT
    answer = input('you come to a river, you can walk around it or swim accross?(walk/swim) ').lower()

    if answer == 'swim':
        print('you swam acrross and where eaten by an alligator. ')
    elif answer == 'walk':
        print('you walked for many miles, ran out of water and you lost the game')
    else:
        print('not a valid option. you lose.')

elif answer == 'right':
    #RIGHT
    answer = input('you come to a bridge, it looks unstable, do you want to cross it or head back (cross/back)? ').lower()

    if answer == 'back':
        print('you go back to the dirt road and lose. ')
    elif answer == 'cross':
        answer = input('you cross the bridge and meet a stranger. do you want to talk to them (yes/no)? ').lower()

        if answer == 'yes':
            #yes
            answer = input('you talk to the stranger and they gave you a map to the GOLD mine (move/rest)? ').lower()

            if answer == 'move':
                #move
                answer = input(
                    'good job!, you are on the part to the tresure and you found 3 fler fire, there is a dark tunnel ahead and a field of very tall grass, which will choses (tunnel/field)? ').lower()
                if answer == 'tunnel':
                    print('now you are able to pass the dark tunnel with the use of the fler fire and got to the other side and you were saved, there are two part (right/left)')
                elif answer == 'right':
                


                    #WAITNG ON THIS......
                elif answer == 'field':
                    print('you passed the field filled with tall grasses and got lost and you LOSE!')
                else:
                    print('not a valid option. you lose. ')
            elif answer == 'rest':
                #rest
                answer = input('how many min do you want to rest for (5min/10min)? ').lower()

                if answer == '10min':
                    print('you rested for too long and you got eaten by a wild beast. ')
                elif answer == '5min':
                    answer = input('you escaped the wild beast and found a small village to find food (find food/continue)? ').lower()
                    if answer == 'find food':
                        answer = input('you found food from a stranger, do you want to eat it or not (accept)? ').lower()
                        if answer == 'accept':
                            print('the food was poisoned, and you LOSE! ')
                    elif answer == 'continue':
                        answer = input('you continued your jonney and you are on the part to find the GOLD MINE, and on way you found a wild cat do you (run/fight)? ').lower()
                        if answer == 'run':
                            print('you were out runed by the wild cat, and you LOSE')
                        elif answer == 'fight':
                            answer = input('you were able to kill the cat cause you had the skill, GOOD JOB!, after a long walk you found a dark cave do you want to (enter/leave)? ').lower()
                            if answer == 'leave':
                                print('you left and you LOSE! ')
                            elif answer == 'enter':
                                print('you entered the cave and found the GOLD MINE, GREAT JOB! ')
                            
        elif answer == 'no':
            #no
            print('you ignore the stranger and you lost the map and you LOSE!')

        else:
            print('not a valid option. you lose.')

    else:
        print('not a valid option. you lose.')

    
else:
    print('not a valid option. you lose.')

print('THANK YOU FOR TRYING', name)
