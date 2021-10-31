def exchange_first_last(seq):
    return seq[-1:]+seq[1:-1]+seq[:1]


def every_other_removed(seq):
    return seq[::2]


def first4_last4_every_other_removed(seq):
    return seq[4:-4:2]


def seq_reversed(seq):
    return seq[::-1]


def last_third_first_third_mid_third(seq):
    first_third = seq[:(len(seq)//3)]
    mid_third = seq[(len(seq)//3):-(len(seq)//3)]
    last_third = seq[-(len(seq)//3):]
    return last_third + first_third + mid_third
