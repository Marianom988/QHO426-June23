def short_pattern():
    pattern = {"sequence":"101","occurrences": 5}
    return pattern

def medium_pattern():
    pattern = {"sequence":"111000","occurrences":25}
    return pattern

def long_pattern():
    pattern = {"sequence":"1100110011001100","occurrences":50}
    return pattern

def run():
    print(f"Analyzing patterns...\nShort sequence:{short_pattern()}\nMedium sequence: {medium_pattern()}\nLong sequence: {long_pattern()} ")

run()