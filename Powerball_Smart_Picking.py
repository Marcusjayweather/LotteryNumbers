import random

def smart_powerball_numbers():
    # Divide the 1–50 range into 5 groups (10 numbers each)
    groups = [range(1, 11), range(11, 21), range(21, 31), range(31, 41), range(41, 51)]
    
    # Pick one number from each group for spread
    main_numbers = [random.choice(group) for group in groups]
    
    # Balance odd/even if possible
    odd_count = sum(1 for n in main_numbers if n % 2 != 0)
    if odd_count < 2:  # Too few odds, replace one even with a random odd
        evens = [n for n in main_numbers if n % 2 == 0]
        if evens:
            replace = random.choice(evens)
            new_odd = random.choice([x for x in range(1, 51) if x % 2 != 0 and x not in main_numbers])
            main_numbers[main_numbers.index(replace)] = new_odd
    elif odd_count > 3:  # Too many odds, replace one odd with a random even
        odds = [n for n in main_numbers if n % 2 != 0]
        if odds:
            replace = random.choice(odds)
            new_even = random.choice([x for x in range(1, 51) if x % 2 == 0 and x not in main_numbers])
            main_numbers[main_numbers.index(replace)] = new_even
    
    # Sort final main numbers
    main_numbers.sort()
    
    # Pick PowerBall from 1–20 with equal chance across ranges
    powerball_groups = [range(1, 11), range(11, 21)]
    powerball = random.choice(random.choice(powerball_groups))
    
    return main_numbers, powerball

# Generate 10 "smart" sets
for i in range(10):
    main, pb = smart_powerball_numbers()
    print(f"Set {i+1}: Main numbers {main} | PowerBall {pb}")
