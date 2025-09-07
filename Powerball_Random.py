import random

def generate_powerball_numbers():
    # Main grid: pick 5 unique numbers from 1–50
    main_numbers = random.sample(range(1, 51), 5)
    main_numbers.sort()

    # Secondary grid: pick 1 number from 1–20
    powerball = random.randint(1, 20)

    return main_numbers, powerball

# Generate 10 possible sets
for i in range(10):
    main, pb = generate_powerball_numbers()
    print(f"Set {i+1}: Main numbers {main} | PowerBall {pb}")

