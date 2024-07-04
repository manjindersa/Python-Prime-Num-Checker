print("\nPrime Number Checker\n")
while True:
    try:
        num = int(input("Please enter an integer between 1 and 5000: "))
        if num < 1 or num > 5000:
            print("Error: The number must be between 1 and 5000.")
            continue
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        continue

    # Check if the number is prime
    n = num
    is_prime = True
    if n <= 1:
        is_prime = False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        # Get factors of the number
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        print(f"{num} is NOT a prime number.")
        print(f"It has {len(factors)} factors: {' '.join(map(str, factors))}")

    try_again = input("\nTry again? (y/n): ").lower()
    print()
    if try_again != 'y':
        print("Bye!\n")
        break