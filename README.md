# Python Prime Number Checker

## Description
The Python Prime Number Checker is a simple command-line application that allows users to check if a given integer between 1 and 5000 is a prime number. If the number is not prime, the program will also display its factors.

## Features
- **Prime Number Check**: Determines if the entered number is a prime number.
- **Factor Display**: If the number is not prime, displays all its factors.
- **Retry Option**: Allows the user to check multiple numbers in a single session.

## Usage
1. **Clone the Repository**: Clone the repository to your local machine.
    ```sh
    git clone https://github.com/manjindersa/Python-Prime-Num-Checker.git
    ```
2. **Navigate to the Directory**: Change to the directory containing the `PrimeNumChecker.py` file.
    ```sh
    cd Python-Prime-Num-Checker
    ```
3. **Run the Program**: Execute the Python script.
    ```sh
    python PrimeNumChecker.py
    ```
4. **Enter a Number**: Follow the prompt to enter an integer between 1 and 5000.
5. **Check Result**: The program will indicate whether the number is prime and, if not, display its factors.
6. **Try Again**: The program will prompt if you want to check another number. Enter 'y' to continue or 'n' to exit.

## Example
```
Prime Number Checker

Please enter an integer between 1 and 5000: 29
29 is a prime number.

Try again? (y/n): y

Please enter an integer between 1 and 5000: 30
30 is NOT a prime number.
It has 8 factors: 1 2 3 5 6 10 15 30

Try again? (y/n): n
Bye!
```

## Code Structure

### Main Program
- **Input Validation**: Ensures the entered number is an integer between 1 and 5000.
- **Prime Check**: Determines if the entered number is a prime number.
- **Factor Calculation**: If the number is not prime, calculates and displays its factors.
- **Retry Option**: Allows the user to try again or exit the program.

### Functions
- **Prime Check**: Uses a simple algorithm to determine if a number is prime by checking divisibility up to the square root of the number.
- **Factor Calculation**: Iterates through all integers from 1 to the number itself to find and display all factors.

## Author
- **Manjinder Singh**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute, report issues, or suggest features by opening a pull request or issue on the [GitHub repository](https://github.com/manjindersa/Python-Prime-Num-Checker).
