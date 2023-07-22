def steps():
    likelihoods = [("step 1",50),("step 2",38),("step 3",27),("step 4",99),("step 5",4)]
    return likelihoods


def run():
    x = steps()
    good_steps = []
    bad_steps = []
    g = x[0]
    d = x[3]

    for f in x:
        if f == g or f ==d:
         good_steps.append(f)
        else :
         bad_steps.append(f)
    print(f"Good steps:",len(good_steps), "Bad steps:",len(bad_steps))

run()