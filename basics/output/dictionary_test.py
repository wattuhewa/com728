def short_pattern():
    pattern ={"sequence":"101", "occurences":5, "test": 20}
    return pattern

def medium_pattern():
    pattern ={"sequence":"111000", "occurences":25}
    return pattern

def long_pattern():
    pattern ={"sequence":"110011001100", "occurences":50}
    return pattern

def run():
    print("Analysing patterns......")
    patterns = {"short sequence": short_pattern(),"medium sequence":medium_pattern(), "long sequence": long_pattern()}

    for key, value in patterns.items():
        print(f"{key}: {value}")

run()
