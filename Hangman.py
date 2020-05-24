"""The Hangman Game!"""
print("Welcome to Hangman\nPlayer 1 Are you ready??")

user_word1 = input("Enter the word to be guessed: ")
user_word2 = list(user_word1.lower())

print("\n"*50,"\nPlayer 2 Are you ready??\nYour word is:")


vowels = ["a","e","i","o","u"]
word = []
for letter in user_word2:
    if letter in vowels:
        
        word.append("*")

    elif letter == " ":
        word.append("/")


    else:
        word.append("_")
word_print = ' '.join(str(e) for e in word)
print("\n", word_print, "\nYou have 10 lives left")


   

lives = 10
while lives > 0:
    guess = (input("Enter your guess: ")).lower()

    if len(guess) > 1:
        print("Enter only one letter")
        break
	
    if guess in user_word2:
        for i in range(len(user_word1)):
            if guess == user_word1[i]:
                word.pop(i)
                word.insert(i, user_word2[i])
                word_print = ' '.join(str(i) for i in word)
                print(word_print)
                print("You have ", lives, " lives left")	

    else:
        lives = lives - 1
        print("Incorrect guess")
        word_print = ' '.join(str(i) for i in word)
        print(word_print)
        print("You have ", lives, " lives left")

    if lives == 0:
        print("\n You Lose\n The word was ", user_word1)
        break

    if word_print == word_user1:
        print("You win!")
        break




