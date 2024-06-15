# Lottery Number Checker

This Python script simulates a simple lottery number checking system. It generates random lottery numbers and asks the user to input their guesses. It then compares the user's guesses with the lottery numbers and determines the prize based on the number of correct guesses.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the `Lottery Number Checker.py` file.
2. Run the script using Python:

    ```
    python Lottery Number Checker.py
    ```

3. Follow the prompts to input your guesses.

## Functionality

- `generate_numbers()`: Generates 6 random numbers between 1 and 49 and returns them in a list.
- `user_input_check(user_numbers, guess_order)`: Takes input from the user for their guesses. Ensures the input is a number between 1 and 49.
- `compare_lottery_results(lottery_result, user_numbers)`: Compares the user's guesses with the lottery results and returns the number of correct guesses.
- `check_prize(correct_count, prize)`: Determines the prize based on the number of correct guesses.
- `main()`: Main function that orchestrates the entire process.

## Prize Structure

The prize is determined based on the number of correct guesses:

- 0 correct guesses: SORRY, YOU DIDN'T GET ANYTHING...
- 1 correct guess: 5% of the jackpot prize
- 2 correct guesses: 10% of the jackpot prize
- 3 correct guesses: 15% of the jackpot prize
- 4 correct guesses: 20% of the jackpot prize
- 5 correct guesses: 25% of the jackpot prize
- 6 correct guesses: JACKPOT - the full jackpot prize!

## Example

Here's an example of how the script works:

Enter your 1. guess: 12
Enter your 2. guess: 28
Enter your 3. guess: 35
Enter your 4. guess: 3
Enter your 5. guess: 17
Enter your 6. guess: 49
37500.0
IF ONLY YOU GOT TWO MORE...
Lottery Result: [12, 28, 35, 3, 17, 49]

In this example, the user had 1 correct guess and won 5% of the jackpot prize.
