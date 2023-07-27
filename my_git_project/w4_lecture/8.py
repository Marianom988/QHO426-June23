def steps():
    likelihoods = [("step 1",50),("step 2",38),("step 3",27),("step 4",99),("step 5",4)]
    return likelihoods


def run():
    x = steps()
    good_steps = []
    bad_steps = []

    for f in x:
        if f[1] >= 50:
         bad_steps.append(f)
        else :
         good_steps.append(f)
    print(f"Good steps:",len(good_steps), "Bad steps:",len(bad_steps))

run()