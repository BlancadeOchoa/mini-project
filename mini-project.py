import random
import string #Predetermined function: from where we extract the alphabet in upper case
from hangman_drawing import display_hangman

#I create a list of different flowers that later will be the words used during the game
flowers = ['daisy','lily','orchid','rose','sunflower','tulip','marguerite','jasmine','violet','poppy']

#this funtion will chose randomly a word from the list
def choose_word(flowers):
    word = random.choice(flowers)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(flowers)

    return word.upper() #All in caps because lower and upper gives problems when mixed

#Now I define the function for the user
def game():

    lives = 6

    word = choose_word(flowers) #counting all the hangman stages, it allows the user 6 tries
    letter_in_word = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    letter_already_used = set()  # what the user has guessed already

    
    # getting user input
    #the while is created so that the user can keep trying letter until they finnish
    while len(letter_in_word) and lives > 0:
        #this functions joins letter used so they can be display for the user
        print('You have used these letters: ', ' '.join(letter_already_used))
        print(display_hangman(lives)) #graphic way to check how you're doing
        print('You have', lives, 'lives left.\n')

        #Here we show the user letter if guessed and _ if not
        word_list = [letter if letter in letter_already_used else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper() #All in caps because lower and upper gives problems when mixed
        #if its a valid letter from the alphabet that hasnt been used yet
        if user_letter in alphabet - letter_already_used:
            letter_already_used.add(user_letter)# when guessed a letter it's add to the used letter
            if user_letter in letter_in_word:
                #if i guess a letter from the word i remove that letter
                letter_in_word.remove(user_letter)
                
            else:
                lives = lives - 1  # substract a life if letter not in word
                print('\nYour letter,', user_letter, 'is not in the word.')
        
        #if the letter I guess has already been used
        elif user_letter in letter_already_used:
            print('\nThat letter has already been used. Try again.')

        else:
            print('\nNot a valid letter, try again.')

    # Once len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You lost!!. The word was', word)
    else:
        print('You win!!. You guessed the word', word, 'correctly !!')

#This function allows the user to play again once the game is over
def main():
    word = choose_word(flowers)
    game()
    while input("Do you want to play again? (Y/N) ").upper() == "Y":
        word = choose_word(flowers)
        game()

if __name__ == "__main__":
    main()