import random

# Generate 6 numbers between 1 and 49 and return them in a list
def generate_numbers():
    numbers = []
    i = 0
    while i < 6:
        number = random.randint(1, 49)
        numbers.append(number)
        i += 1
    return numbers

# Take input from the user
def user_input_check(user_numbers, guess_order):
    while True:
        try:
            number = int(input(f"Enter your {guess_order + 1}. guess: "))
            # Check if the number is between 1 and 49
            if 1 <= number <= 49:
                user_numbers.append(number)
                break
            else:
                print("Please enter a number between 1 and 49")
        except:
            print("Please enter a number")

    return user_numbers

# Compare the indexes of both lists and write the number of correct guesses
def compare_lottery_results(lottery_result, user_numbers):
    correct_count = 0

    i = 0
    while i < 6:
        # If a number in the user's list is in the lottery result, increment the correct count
        if user_numbers[i] in lottery_result:
            correct_count +=1

        i+=1

    return correct_count

# Determine the prize based on the number of correct guesses
def check_prize(correct_count, prize):
    if correct_count == 0:
        print("SORRY, YOU DIDN'T GET ANYTHING...")

    elif correct_count == 1:
        print(prize * 0.05)
        print("IF ONLY YOU GOT FIVE MORE...")

    elif correct_count == 2:
        print(prize * 0.1)
        print("IF ONLY YOU GOT FOUR MORE...")

    elif correct_count == 3:
        print(prize * 0.15)
        print("IF ONLY YOU GOT THREE MORE...")

    elif correct_count == 4:
        print(prize * 0.2)
        print("IF ONLY YOU GOT TWO MORE...")

    elif correct_count == 5:
        print(prize * 0.25)
        print("IF ONLY YOU GOT ONE MORE...")

    elif correct_count == 6:
        print(prize)
        print("!!!!CONGRATULATIONS, YOU'VE WON THE JACKPOT!!!")

# Main function
def main():
    # Get the lottery results
    lottery_result = generate_numbers()

    # Get the user's guesses
    user_numbers = []
    i = 0
    while i < 6:
        user_input_check(user_numbers, i)
        i += 1

    # Calculate the jackpot prize based on the user's guesses
    jackpot_prize = 100000
    check_prize(compare_lottery_results(lottery_result, user_numbers), jackpot_prize)

    # Print the lottery result
    print("Lottery Result: ", lottery_result)

main()
