def intro():
    # Prints out the intro to the game.

        print('*******************************')
        print('*                             *')
        print('* 1. New Single Player Game   *')
        print('* 2. New Two Player Game      *')
        print('* 3. Dota 2 Quiz              *')
        print('* 4. User Guide               *')
        print('* 5. Quit                     *')
        print('*                             *')
        print('*******************************')

def quit_program():
    # Code to terminate the program.

    print('Thanks for trying me out! Have a great day!')
    quit()

def stats():
    # Stats for the single player game
    # Changes grammar when needed.

    if wins == 1 and loss == 1 and tie == 1:
        print('You currently have:', wins, 'win,', loss, 'loss,', tie, 'tie.')
        return('')
    elif wins == 1 and loss == 1:
        print('You currently have:', wins, 'win,', loss, 'loss,', tie, 'ties.')
        return('')
    elif wins == 1 and tie == 1:
        print('You currently have:', wins, 'win,', loss, 'losses,', tie, 'tie.')
        return('')
    elif loss == 1 and tie == 1:
        print('You currently have:', wins, 'wins,', loss, 'loss,', tie, 'tie.')
        return('')

    elif wins == 1:
        print('You currently have:', wins, 'win,', loss, 'losses,', tie, 'ties.')
        return('')
    elif loss == 1:
        print('You currently have:', wins, 'wins,', loss, 'loss,', tie, 'ties.')
        return('')
    elif tie == 1:
        print('You currently have:', wins, 'wins,', loss, 'losses,', tie, 'tie.')
        return('')

    else:
        print('You currently have:', wins, 'wins,', loss, 'losses,', tie, 'ties.')
        return('')


def stats_twoplayer():
    # Stats for the single player game
    # Changes grammar when needed.

    if wins == 1 and loss == 1 and tie == 1:
        print('Player 1 currently have:', wins, 'win,', loss, 'loss,', tie, 'tie over player 2.')
        return('')
    elif wins == 1 and loss == 1:
        print('Player 1 currently have:', wins, 'win,', loss, 'loss,', tie, 'ties over player 2.')
        return('')
    elif wins == 1 and tie == 1:
        print('Player 1 currently have:', wins, 'win,', loss, 'losses,', tie, 'tie over player 2.')
        return('')
    elif loss == 1 and tie == 1:
        print('Player 1 currently have:', wins, 'wins,', loss, 'loss,', tie, 'tie over player 2.')
        return('')

    elif wins == 1:
        print('Player 1 currently have:', wins, 'win,', loss, 'losses,', tie, 'ties over player 2.')
        return('')
    elif loss == 1:
        print('Player 1 currently have:', wins, 'wins,', loss, 'loss,', tie, 'ties over player 2.')
        return('')
    elif tie == 1:
        print('Player 1 currently have:', wins, 'wins,', loss, 'losses,', tie, 'tie over player 2.')
        return('')

    else:
        print('Player 1 currently have:', wins, 'wins,', loss, 'losses,', tie, 'ties over player 2.')
        return('')

def ask_question():
    #We use this for our Dota 2 quiz program, where we ask a question.

    item = random.choice(list(questions.items()))
    # Gets a random element from questions.

    question = item[0]
    # Makes the first part a question

    (varients, answer) = item[1]
    # Makes the part before "," varients and part after "," the answer.

    print(question, varients)
    # Prints the question and varients that we specified above to the user.

    print('')
    print('You can end this game at anytime by typing "end" or "menu".')
    guess = input('Please type your answer: a, b, c or d.')

    return (guess,answer)
    # Returns guess and answer so they can be used in the code.

intro()
# Runs the intro to the program

print('')
print('You can go back to the menu at anytime by typing "menu"')
while True:
    answer = input('Type a number for your option: ')

    if answer == '1':

        # Resets the stats to 0 at the start of a new game
        wins = 0
        loss = 0
        tie = 0

        # Importing random to generate options for the computer
        from random import randint

        # The options the computer can generate.
        options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

        # The option that the computer gets.
        computer_choice = options[randint(0, 4)]

        print('')
        print('You can go back to the menu at anytime by typing "menu"')
        print('To start a new single player game, what is your first move?')
        print('')

        while True:
            player_choice = input('Rock, Paper, Scissors, Lizard, Spock?')
            print('')
            if player_choice.lower() == computer_choice.lower():
                tie += 1
                print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                print('You tie!')
                print(stats())
            elif player_choice.lower() == 'rock':
                if computer_choice == 'Paper':
                    loss += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print('You lose!', computer_choice, 'covers', player_choice)
                    print(stats())
                if computer_choice == 'Spock':
                    loss += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print('You lose!', computer_choice, 'vaporizes', player_choice)
                    print(stats())
                if computer_choice == 'Lizard':
                    wins += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print("You win!", player_choice, 'crushes', computer_choice)
                    print(stats())
                if computer_choice == 'Scissors':
                    wins += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print("You win!", player_choice, 'crushes', computer_choice)
                    print(stats())
            elif player_choice.lower() == 'paper':
                if computer_choice == 'Scissors':
                    loss += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print('You lose!', computer_choice, 'cuts', player_choice)
                    print(stats())
                if computer_choice == 'Lizard':
                    loss += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print('You lose!', computer_choice, 'eats', player_choice)
                    print(stats())
                if computer_choice == 'Rock':
                    wins += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print("You win!", player_choice, 'covers', computer_choice)
                    print(stats())
                if computer_choice == 'Spock':
                    wins += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print("You win!", player_choice, 'disproves', computer_choice)
                    print(stats())
            elif player_choice.lower() == 'scissors':
                if computer_choice == 'Spock':
                    loss += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print('You lose!', computer_choice, 'smashes', player_choice)
                    print(stats())
                if computer_choice == 'Rock':
                    loss += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print('You lose!', computer_choice, 'crushes', player_choice)
                    print(stats())
                if computer_choice == 'Paper':
                    wins += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print("You win!", player_choice, 'cuts', computer_choice)
                    print(stats())
                if computer_choice == 'Lizard':
                    wins += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print("You win!", player_choice, 'decapitates', computer_choice)
                    print(stats())
            elif player_choice.lower() == 'lizard':
                if computer_choice == 'Rock':
                    loss += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print('You lose!', computer_choice, 'crushes', player_choice)
                    print(stats())
                if computer_choice == 'Scissors':
                    loss += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print('You lose!', computer_choice, 'decapitates', player_choice)
                    print(stats())
                if computer_choice == 'Spock':
                    wins += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print("You win!", player_choice, 'poisons', computer_choice)
                    print(stats())
                if computer_choice == 'Paper':
                    wins += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print("You win!", player_choice, 'eats', computer_choice)
                    print(stats())
            elif player_choice.lower() == 'spock':
                if computer_choice == 'Lizard':
                    loss += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print('You lose!', computer_choice, 'poisons', player_choice)
                    print(stats())
                if computer_choice == 'Paper':
                    loss += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print('You lose!', computer_choice, 'disproves', player_choice)
                    print(stats())
                if computer_choice == 'Scissors':
                    wins += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print("You win!", player_choice, 'smashes', computer_choice)
                    print(stats())
                if computer_choice == 'Rock':
                    wins += 1
                    print('You chose:', player_choice, 'and the computer chose:', computer_choice)
                    print("You win!", player_choice, 'vaporizes', computer_choice)
                    print(stats())
            elif player_choice.lower() == 'menu':
                intro()
                break
                # Goes back to main menu and asks for new input.

            elif player_choice.lower() == 'quit':
                quit_program()

            else:
                print("That's not a valid play. Check your spelling!")

            computer_choice = options[randint(0, 4)]
            # Computer generates a new option

    elif answer == '2':

        wins = 0
        loss = 0
        tie = 0
        # Resets the stats to 0 at the start of a new game

        options_lowercase = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        # The options that is valid for the user to input.

        print('')
        print('You can go back to the menu at anytime by typing "menu"')
        print('To start a new two player game, what is your first move player 1?')
        print('')

        while True:
            # Keeps the loop going no matter what the user types.

            player1_choice = input('Player 1: Rock, Paper, Scissors, Lizard, Spock?')

            if player1_choice.lower() == 'menu':
                intro()
                break
            elif player1_choice.lower() == 'quit':
                quit_program()
            elif player1_choice.lower() in options_lowercase:
                print("\n" * 100)

            while not player1_choice.lower() in options_lowercase:
                # Checks players 1 input towards the options to see if the input is valid or not before moving on to player 2

                print("That's not a valid play player 1. Check your spelling!")

            player2_choice = input('Player 2: Rock, Paper, Scissors, Lizard, Spock?')
            print('')

            if player2_choice.lower() == 'menu':
                intro()
                break

            elif player2_choice.lower() == 'quit':
                quit_program()

            if not player2_choice.lower() in options_lowercase:
                # Checks players 2 input towards the options to see if the input is valid or not before moving on to the game.

                print("That's not a valid play player 2. Check your spelling!")


            # Checking each answers from both towards each other
            elif player1_choice.lower() == 'rock':
                if player2_choice.lower() == 'rock':
                    tie += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print('You tie!')
                    print(stats_twoplayer())
                if player2_choice.lower() == 'paper':
                    loss += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print('Player 2 wins! ', player2_choice, 'covers', player1_choice)
                    print(stats_twoplayer())
                if player2_choice.lower() == 'spock':
                    loss += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print('Player 2 wins! ', player2_choice, 'vaporizes', player1_choice)
                    print(stats_twoplayer())
                if player2_choice.lower() == 'lizard':
                    wins += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print("Player 1 wins! ", player1_choice, 'crushes', player2_choice)
                    print(stats_twoplayer())
                if player2_choice.lower() == 'scissors':
                    wins += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print("Player 1 wins! ", player1_choice, 'crushes', player2_choice)
                    print(stats_twoplayer())
            elif player1_choice.lower() == 'paper':
                if player2_choice.lower() == 'paper':
                    tie += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print('You tie!')
                    print(stats_twoplayer())
                if player2_choice.lower() == 'scissors':
                    loss += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print('Player 2 wins! ', player2_choice, 'cuts', player1_choice)
                    print(stats_twoplayer())
                if player2_choice.lower() == 'lizard':
                    loss += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print('Player 2 wins! ', player2_choice, 'eats', player1_choice)
                    print(stats_twoplayer())
                if player2_choice.lower() == 'rock':
                    wins += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print("Player 1 wins! ", player1_choice, 'covers', player2_choice)
                    print(stats_twoplayer())
                if player2_choice.lower() == 'spock':
                    wins += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print("Player 1 wins! ", player1_choice, 'disproves', player2_choice)
                    print(stats_twoplayer())
            elif player1_choice.lower() == 'scissors':
                if player2_choice.lower() == 'scissors':
                    tie += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print('You tie!')
                    print(stats_twoplayer())
                if player2_choice.lower() == 'spock':
                    loss += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print('Player 2 wins! ', player2_choice, 'smashes', player1_choice)
                    print(stats_twoplayer())
                if player2_choice.lower() == 'rock':
                    loss += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print('Player 2 wins! ', player2_choice, 'crushes', player1_choice)
                    print(stats_twoplayer())
                if player2_choice.lower() == 'paper':
                    wins += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print("Player 1 wins! ", player1_choice, 'cuts', player2_choice)
                    print(stats_twoplayer())
                if player2_choice.lower() == 'lizard':
                    wins += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print("Player 1 wins! ", player1_choice, 'decapitates', player2_choice)
                    print(stats_twoplayer())
            elif player1_choice.lower() == 'lizard':
                if player2_choice.lower() == 'lizard':
                    tie += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print('You tie!')
                    print(stats_twoplayer())
                if player2_choice.lower() == 'rock':
                    loss += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print('Player 2 wins! ', player2_choice, 'crushes', player1_choice)
                    print(stats_twoplayer())
                if player2_choice.lower() == 'scissors':
                    loss += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print('Player 2 wins! ', player2_choice, 'decapitates', player1_choice)
                    print(stats_twoplayer())
                if player2_choice.lower() == 'spock':
                    wins += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print("Player 1 wins! ", player1_choice, 'poisons', player2_choice)
                    print(stats_twoplayer())
                if player2_choice.lower() == 'paper':
                    wins += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print("Player 1 wins! ", player1_choice, 'eats', player2_choice)
                    print(stats_twoplayer())
            elif player1_choice.lower() == 'spock':
                if player2_choice.lower() == 'spock':
                    tie += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print('You tie!')
                    print(stats_twoplayer())
                if player2_choice.lower() == 'lizard':
                    loss += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print('Player 2 wins! ', player2_choice, 'poisons', player1_choice)
                    print(stats_twoplayer())
                if player2_choice.lower() == 'paper':
                    loss += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print('Player 2 wins! ', player2_choice, 'disproves', player1_choice)
                    print(stats_twoplayer())
                if player2_choice.lower() == 'scissors':
                    wins += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print("Player 1 wins! ", player1_choice, 'smashes', player2_choice)
                    print(stats_twoplayer())
                if player2_choice.lower() == 'rock':
                    wins += 1
                    print('Player 1 chose:', player1_choice, 'and player 2 chose:', player2_choice)
                    print("Player 1 wins! ", player1_choice, 'vaporizes', player2_choice)
                    print(stats_twoplayer())

    elif answer == '3':

        import random
        # Need random for random.choice to work from def ask_question():

        # The questions with answers that we're going to random from.
        questions = {
            '\nWhen does the first night start?\n':
                (
                '\na. At minute 4:00\nb. At minute 5:00\nc. At minute 6:00\nd. At minute 10:00\n', 'a. At minute 4:00'),
            '\nHow many melee and ranged creeps spawn in the first wave, for only one lane? Not counting the enemy creeps in that lane!\n':
                (
                '\na. 4 melee creeps, 1 ranged creep''\nb. 3 melee creeps, 1 ranged creep''\nc. 4 melee creeps, 2 ranged creeps''\nd. 3 melee creeps, 2 ranged creeps',
                'b. 3 melee creeps'),
            '\nHow many neutral camps are in the Radiant jungle, not counting the Ancients?\n':
                (
                '\na. 5; - 1 small camp, 2 medium camps and 2 large camps\nb. 5; - 2 small camps, 2 medium camps and 1 large camp\nc. 6; - 2 small camps, 2 medium camps and 2 large camps\nd. 6; - 1 small camp, 3 medium camps and 2 large camps\n',
                'a. 5; - 1 small camp, 2 medium camps and 2 large camps'),
            '\nPick one set of the neutral creeps that cant spawn in the medium camp.\n':
                ('\na. Centaur camp''\nb. Mud Golems''\nc. Hellbear camp''\nd. Wolf camp', 'c. Hellbear camp'),
            '\nAt the start of the game, only Bounty runes can spawn.\n':
                ('\na. True\nb. False\nc. Sometimes\nd. Mixed runes\n', 'a. True'),
            '\nOnce placed, Observer Ward will last for how long?\n':
                ('\na. 8 minutes''\nb. 6 minutes''\nc. 5 minutes''\nd. 7 minutes', 'd. 7 minutes'),
            '\nYou can reveal the Wards (Observer and Sentry Wards) with Dust.\n':
                ('\na. True\nb. False\nc. If you use 2x Dust\nd. Only with some heroes\n', 'b. False'),
            '\nWhen can you upgrade the Courier?\n':
                ('\na. At minute 2:00''\nb. At minute 3:00''\nc. At minute 4:00''\nd. At the start of the game',
                 'b. At minute 3:00'),
            '\nWhat is the correct amount of experience a Hero has to gain to advance from Level 1 to Level 2?\n':
                ('\na. 200''\nb. 400''\nc. 600''\nd. 800', 'a. 200'),
            '\nDestroying a Tier 1 Tower refreshes the Glyph of Fortification.\n':
                ('\na. True\nb. False\nc. Sometimes\nd. If certain heroes gets last hit\n', 'a. True'),
            '\nFirst Roshan spawns with how much HP?\n':
                ('\na. 2500''\nb. 5000''\nc. 7500''\nd. 10000', 'c. 7500'),
            '\n Once you activate a Haste rune, your movement speed is set to\n':
                ('\na. 550 MS\nb. 522 MS\nc. 322 MS\nd. 650 MS\n', 'b. 522 MS'),
            '\nWhat is the day and night vision for most Heroes?\n':
                (
                '\na. 1600 during the day, 800 during the night''\nb. 2000 during the day, 800 during the night''\nc. 1600 during the day, 1000 during the night''\nd. 1800 during the day, 800 during the night',
                'd. 1800 during the day, 800 during the night'),
            '\nMost of the Heroes start with how much Magical Resistance?\n':
                ('\na. 20%\nb. 25%\nc. 30%\nd. 35%\n', 'b. 25%'),
            '\nAncients (main buildings) regenerate how much HP per second?\n':
                ('\na. 2 HP/s''\nb. 3 HP/s''\nc. 4 HP/s''\nd. 5 HP/s', 'b. 3 HP/s'),
            '\nAt 20 minutes into the game, Roshan will have how much maximum HP? \n':
                ('\na. 8000 HP\nb. 9000 HP\nc. 10000 HP\nd. 15000 HP\n', 'c. 10000 HP'),
            '\nWith additional 28 Agility, your Hero gains how much Armor?\n':
                ('\na. Close to 2''\nb. Close to 3''\nc. Close to 4''\nd. Close to 5', 'c. Close to 4'),
            '\nWhich Strength Hero has the highest Strength gain per level?\n':
                ('\na. Centaur\nb. Treant\nc. Doom\nd. Pudge\n', 'a. Centaur'),
            '\nWhen are you able to deny your Tier 1 Tower?\n':
                ('\na. Once it has 220 HP''\nb. Once it has 190 HP''\nc. Once it has 160 HP''\nd. Once it has 130 HP',
                 'd. Once it has 130 HP'),
            '\nWhich summoned unit lasts for the longest time before expiring? \n':
                (
                '\na. Plague Ward (Venomancer)\nb. Serpent Ward (Shadow Shaman)\nc. Lycan Wolf\nd. Hawk (Beastmaster)\n',
                'd. Hawk (Beastmaster)'),
                }

        answers = ['a', 'b', 'c', 'd']
        total_points = 0
        total_questions = 0

        while True:

            guess, answer = ask_question()

            if guess.lower() == 'end':
                print('You got:', total_points, 'out of', total_questions, 'questions correct.')
                print('')
                intro()
                break

            elif guess.lower() == 'menu':
                intro()
                break

            elif guess.lower() == 'quit':
                quit_program()

            elif guess not in answers:
                print('')
                print('Invalid, try again!')

            elif guess == answer:
                total_points += 1
                # Gives 1 point for correct answer.

                total_questions += 1
                # Adds 1 to the total_questions counter

                print('')
                print('Correct!')
                print('You currently have', total_points, 'correct answers out of', total_questions)

            else:
                total_questions += 1
                # Adds 1 to the total_questions counter

                print('')
                print('Incorrect! The correct answer was:', answer)
                print('You currently have', total_points, 'correct answers out of', total_questions, 'points')

    elif answer == '4':
            print('Welcome to my program, this user guide will tell you what is possible to do within the program.')
            print('')
            print('At anytime can you type "menu" to get back to the main menu.')
            print('At anytime can you type "quit" to terminate the program.')
            print('')
            print('With that said, this game is mainly about Rock-Paper-Scissors-Lizard-Spock.')
            print('This game is an expansion on the game Rock, Paper and Scissors.')
            print('If you want to know the rules of this game just type "rules".')
            print('')
            print('Choosing option 1 in the main menu, you will face off against the computer.')
            print('Choosing option 2 in the main menu, you will face off against another person, using the same computer.')
            print('Choosing option 3 in the main menu, you will be taken to the Dota 2 quiz.')
            print('You will get a random question out of a pool of 21 questions')
            print('Choosing option 4 in the main menu, you will be taken to this menu.')
            print('Choosing option 5 in the main menu, you will quit the program, but you can also type "quit" at anytime.')
            print('')

            while True:
                user_guide_answer = input('What would you like to do ? Valid inputs are: rules, menu and quit. ')

                if user_guide_answer.lower() == 'rules':
                    print('')
                    print('Scissors cuts paper')
                    print('Paper covers Rock')
                    print('Rock crushes Lizard')
                    print('Lizard poisons Spock')
                    print('Spock smashes Scissors ')
                    print('Scissors decapitates Lizard ')
                    print('Lizard eats Paper ')
                    print('Paper disproves Spock ')
                    print('Spock vaporizes Rock ')
                    print('Rock crushes Scissors')
                    print('')

                elif user_guide_answer.lower() == 'menu':
                    intro()
                    break

                elif user_guide_answer.lower() == 'quit':
                    quit_program()

                else:
                    print('Invalid input, please try again! ')

    elif answer == '5':
                quit_program()

    elif answer.lower() == 'quit':
                quit_program()
    else:
        print('')
        print('Invalid input, please try again! ')
        # Checks what input the user gave, if not between 1-5, they get an error.