import numpy

def make_lotto_number(**kwargs):
    rand_number = numpy.random.choice(range(1, 46), 6, replace=False)