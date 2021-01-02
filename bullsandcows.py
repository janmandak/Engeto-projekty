'''
Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number
>>> 1234
0 bulls, 2 cows
>>> 6147
1 bull, 1 cow
>>> 2417
3 bulls, 0 cows
>>> 2017
Correct, you've guessed the right number in 4 guesses!
That's {amazing, average, not so good, ...}
'''
def bulls_and_cows():

    # generate random 4-digit number
    import random
    number = random.sample(range(0, 10), 4)
    #number = [8,2,0,3]

    # make sure 0 is not at the beginning
    if number[0] == 0:
      number[0] = random.randint(1,9)
    print(number)  

    # variable to count number of guesses
    counter = 1

    # welcome to the game
    print("Hi there!")
    print("I have generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")

    # let the game begin!
    while True:

      guess = input('Guess a 4-digit number!')

      if guess.isdigit() == False:
        print('-' * 40)
        print('This is not a number! Again, please.')
        print('-' * 40)
        counter += 1
        continue

      guess_list = [int(x) for x in str(guess)]
      print('-' * 40)

      if len(guess_list) != 4:
        print('This is not a 4-digits number! Again, please.')
        print('-' * 40)
        counter += 1
        continue

        #guess = int(input('Guess a 4-digit number!'))
        #guess_list = [int(x) for x in str(guess)]

      # logic for 4 equal numbers
      if guess_list[0] == guess_list[1] == guess_list[2] == guess_list[3]:
        print('Numbers cannot be the same! Again, please.')
        print('-' * 40)
        counter += 1
        continue
        

        #guess = int(input('Guess a 4-digit number!'))
        #guess_list = [int(x) for x in str(guess)]
 

      if number == guess_list:
        if counter <= 5:
          print('-' * 60)
          print('Congratulations, you won! You needed only', counter, 'guesses.', 'Outstanding performance!')
          print('-' * 60)
        elif counter > 5 and counter <= 10:
          print('-' * 60)
          print('Congratulations, you won! You needed', counter, 'guesses.', 'Good performance.')
          print('-' * 60)
        else:
          print('-' * 60)
          print('Congratulations, you won! You needed', counter, 'guesses.', 'Can be better, but you won, so what? :)')
          print('-' * 60)

        break
      
      else:
        counter += 1

        bulls = 0
        cows = 0
        for i in range(len(guess_list)):
          if guess_list[i] == number[i]:
            bulls += 1
            continue
          if guess_list[i] in number:
              cows += 1
        
        if bulls == 1:
          print('You have 1 bull.')
        else:
          print('You have', bulls, 'bulls.')

        if cows == 1:
          print('You have 1 cow.')
        else:
          print('You have', cows, 'cows.')

        print('-' * 40)

bulls_and_cows()