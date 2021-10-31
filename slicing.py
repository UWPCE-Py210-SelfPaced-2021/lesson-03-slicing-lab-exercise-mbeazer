def exchange_first_last(seq):
    return seq[-1:]+seq[1:-1]+seq[:1]


def every_other_removed(seq):
    return seq[::2]


def first4_last4_every_other_removed(seq):
    return seq[4:-4:2]


def seq_reversed(seq):
    pass


def last_third_first_third_mid_third(seq):
    pass


test_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
print(first4_last4_every_other_removed('testing one two three four five'))
print(first4_last4_every_other_removed(test_list))
