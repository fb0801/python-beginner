
secret_word=""
hidden_word =["Follow", "Peter", "Mike", "Ashley", "Giraffe"]
guess=""
guess_count = 0
guess_limit = 3
out_of_guess = False



while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter your guess human: ")
        guess_count +=1
    else:
        out_of_guess = True

    
if out_of_guess:
    print("You lose human! your out of guesses")
else:
    print("You win this time human!")
