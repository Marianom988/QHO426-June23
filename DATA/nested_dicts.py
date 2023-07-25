def short_pattern():
    pattern = {"sequence":"101", "occurrences":5}
    return pattern

def medium_pattern():
    pattern = {"sequence":"111000", "occurences":25}
    return pattern

def long_pattern():
    pattern = {"sequence":"1100110011001100", "occurances":50}
    return pattern

def pattern(s,p):
    return {"sequence":s, "occurances":p}


def run():
    print("Analysing Patterns...")
    d = {"short pattern": short_pattern(), "medium pattern":medium_pattern(), "long pattern":long_pattern()}
    for k,v in d.items():#  . items e' fondamentale per visualizzare entrambi
        print(f"{k}:{v}")


run()
