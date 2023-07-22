def likelihoods():
    likelihood = (58,38,27,99,4)
    return min(likelihood)

def run():
    x = likelihoods()
    print(f"Minimum likehood of falling: {x}%")

run()
