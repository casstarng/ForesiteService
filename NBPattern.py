# Credit to lejafar from https://gist.github.com/lejafar/da2c95b671df6cb1597fc44a07f312be

#!/usr/bin/env python3
"""
Example implementation of https://stats.stackexchange.com/q/322943/190938
Determine the most likely value that is about to follow based on binary sequence using Naive Bayes
Test should output:
Predicted 1 CORRECTLY for [0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0] , pattern: [0, 1]
Predicted 1 CORRECTLY for [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0] , pattern: [0, 1]
Predicted 0 CORRECTLY for [1, 1, 0, 1, 0, 0, 1] , pattern: [0, 1, 0]
Predicted 1 CORRECTLY for [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0] , pattern: [0, 1]
"""


def parse(history, n):
    """
    Generate list of (pattern, followed_by) tuples with patterns
    of lenght n found in inside `history` for [0,1,1,0,1,0,1,1,0,1] this gives:
        [([0, 1, 1], 0),
         ([1, 1, 0], 1),
         ([1, 0, 1], 0),
         ([0, 1, 0], 1),
         ([1, 0, 1], 1),
         ([0, 1, 1], 0),
         ([1, 1, 0], 1)]
    """
    for i in range(len(history) - n):
        yield (history[i:i + n], history[i + n])


def hash(pattern):
    """
    It's just convinient to store 1,0-pattern at their binary value in `counts`
    """
    return sum([d * pow(2, i) for i, d in enumerate(reversed(pattern))])


def learn(example, n):
    """
    Count how many times a certain pattern occurs followed by a 1 or 0
    """
    occurences = parse(example, n)
    # counts[followed_by][pattern]
    counts = [[0] * pow(2, n), [0] * pow(2, n)]
    # loop over all occurences
    for occurence in occurences:
        pattern, followed_by = occurence
        pattern_hash = hash(pattern)
        counts[followed_by][pattern_hash] += 1
    return counts


def probability(example, n):
    """
    Determine `counts` array in order to infer `followed_by` using `example`
    """
    counts = learn(example, n)
    # determine probability that 1 will follow after `previous`
    # (last n values), using what we know about past values
    previous = example[-n:]
    previous_hash = hash(previous)
    # Determine probability of `followed_by`=1 using Naive Bayes
    total_count = (counts[1][previous_hash] + counts[0][previous_hash])
    # if pattern was never (`total_count` == 0) seen return None
    return counts[1][previous_hash] / total_count if total_count else None

def prediction(example):
    """
    Determine probability of the next value being 1
    """
    max_n = len(example) - 1
    # Determine probability of `followed_by`=1 over different pattern lengths
    probabilities = [(probability(example, n), n) for n in range(1, max_n) if probability(example, n) is not None]
    # If min equals 0, there is a pattern that is inconsistent with next being 1
    p = min(probabilities)[0] and max(probabilities)[0]
    n = [n for pp, n in probabilities if pp==p][0]
    most_informative = example[-n:] + [int(p)]
    return p


if __name__ == "__main__":
    tests = [([0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0], 1),
             ([1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0], 1),
             ([1, 1, 0, 1, 0, 0, 1], 0),
             ([1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0], 1)]
    print(prediction([0,1,1,1,1,1,1]))