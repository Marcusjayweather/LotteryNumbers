import random

# 1. Define frequency-based weights (example values—update with real data)
main_freq = {
    # number: weight based on frequency
    12: 17,
    16: 15,
    21: 16,
    23: 20,
    39: 45,  # and so on
    # fill in other numbers; you could also invert for cold numbers
}

powerball_freq = {
    24: 50,
    17: 45,
    # etc.
}

def weighted_choice(numbers, weights, k=1):
    return random.choices(numbers, weights=[weights.get(n, 1) for n in numbers], k=k)

def smart_powerball_with_frequency():
    # MAIN GRID: choose 5 unique numbers, with weighted preference
    all_main = list(range(1, 51))
    picks = []
    while len(picks) < 5:
        pick = weighted_choice(all_main, main_freq)[0]
        if pick not in picks:
            picks.append(pick)
    
    picks.sort()
    
    # Heuristic adjustments: balance odd/even
    odd = [n for n in picks if n % 2 != 0]
    even = [n for n in picks if n % 2 == 0]
    if len(odd) < 2:
        # replace one even with a random odd not already picked
        ev = even and random.choice(even)
        rep = random.choice([x for x in range(1,51) if x % 2 != 0 and x not in picks])
        picks[picks.index(ev)] = rep
    elif len(odd) > 3:
        od = odd and random.choice(odd)
        rep = random.choice([x for x in range(1,51) if x % 2 == 0 and x not in picks])
        picks[picks.index(od)] = rep
    
    picks.sort()
    
    # Avoid too many consecutive numbers
    for i in range(len(picks)-2):
        if picks[i+1] == picks[i] + 1 and picks[i+2] == picks[i+1] + 1:
            # nudge the middle one
            new = random.choice([x for x in range(1,51) if x not in picks])
            picks[i+1] = new
            picks.sort()
    
    # SECONDARY GRID: powerball pick
    all_pb = list(range(1, 21))
    pb = weighted_choice(all_pb, powerball_freq, k=1)[0]
    
    return picks, pb

# Generate a few sets
for i in range(10):
    main, pb = smart_powerball_with_frequency()
    print(f"Set {i+1}: Main {main} | PowerBall {pb}")
