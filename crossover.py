from random import randint

"""
Add your crossover functions on this file
"""

def one_point(father, mother):
    point = randint(1, 7)
    real_point = point * 3

    father_mask = (2 ** real_point) - 1
    mother_mask = ((2 ** 24)-1) - father_mask

    child1 = (father&father_mask) | (mother&mother_mask)
    child2 = (father&mother_mask) | (mother&father_mask)
    
    child1 = flip_bit(child1)
    child2 = flip_bit(child2)

    return [child1, child2]

def flip_bit(child):
    pos = randint(0,23)
    mask = 1 << pos
    child ^= mask
    return child