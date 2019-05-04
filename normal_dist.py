
import math


def normal_diff_prob(x, mean, std_dev):
    """
    Calculate the probability of an event given a normal distribution and
    mean, std_dev.
    """

    first_term = 1 / math.sqrt(2 * math.pi * std_dev**2)
    second_term = math.exp(-(x - mean)**2 / (2 * std_dev**2))
    return first_term * second_term


if __name__ == "__main__":
    x = 185
    mean = 180
    std_dev = 34

    prob_x = normal_diff_prob(x, mean, std_dev)
    print(f"Prob of x: {prob_x}")
