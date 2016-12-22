"""Test of the Central Limit Theorem"""

import random
import pandas as pd
import numpy as np


def generate_population(pop_size=100, num_digits=3):
    """Returns a series of random numbers with num_digits before decimal"""
    return pd.Series(map(
        lambda x: abs(round(x * (10**(num_digits - 1)), 2)),
        np.random.randn(pop_size)
    ))


def calc_parameters(series, sample=False):
    """Returns the mean and standard deviation of population"""

    stdev = series.std(ddof=0)

    # calculate sample stdev if applicable
    if sample == True:
        stdev = series.std(ddof=1)

    return series.mean(), stdev


def take_sample(population, samp_size=25):
    """Takes a sample of a given population, returns sample"""

    sample = population.sample(samp_size)
    mean, stdev = calc_parameters(sample, sample=True)

    return sample, mean, stdev


def run_test(pop_size=100, num_digits=3, samp_size=25, trials=100, diag=False):
    """Performs experiment and returns result

    Takes a number of samples and returns the frequency of sample
    means within one standard deviation of the population mean.
    """

    print('generating population')
    population = generate_population(pop_size=pop_size, num_digits=num_digits)
    mean_p, stdev_p = calc_parameters(population)
    confidence_upper = mean_p + float(stdev_p / np.sqrt(samp_size))
    confidence_lower = mean_p - float(stdev_p / np.sqrt(samp_size))
    print('running trials')

    accurate = 0

    trials_completed = 0
    print_count = 0

    for item in range(trials):

        trials_completed += 1
        sample, mean, stdev_s = take_sample(population, samp_size=samp_size)

        if mean < confidence_upper and mean > confidence_lower:
            accurate += 1

        print_count += 1

        if print_count == 1000:
            print_count = 0

            print('accuracy: %s' % (accurate / trials_completed))
            print('number of trials: %s' % (trials_completed))

            with open('output.csv', 'a') as intm:
                intm.write('%s,\n' % (accurate / trials_completed))
