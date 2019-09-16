import random

"""
For i = 0, we would've picked uniformly from [0, 0].
For i > 0, before the loop began, any element K in [0, i - 1] had 1 / i chance of being chosen as the random element. 
We want K to have 1 / (i + 1) chance of being chosen after the iteration. This is the case since the chance of having being chosen 
already but not getting swapped with the ith element is 1 / i * (1 - (1 / (i + 1))) which is 1 / i * i / (i + 1) or 1 / (i + 1)
"""
def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if i == 0:
            random_element = e
        # update the random_element 
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element
