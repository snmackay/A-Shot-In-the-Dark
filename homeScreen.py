from termcolor import colored, cprint

def homeScreen():
    name=colored('A Shot In the Dark','red',attrs=['reverse', 'blink'])

    #input("Press S to start or C for credits")
    print("Press S to enter the game or C for credits")
    while True:
        try:
            if keyboard.is_pressed('S'):
                print('Entering Game')
                return 0
            elif keyboard.is_pressed('C'):
                print('Entering Credits')
                return 1
            else:
                print('')
        except:
            break
