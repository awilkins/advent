

MOD = 20201227

def loop(subject, count):

    value = 1
    ii = 0

    while ii < count:
        ii+=1
        value *= subject
        value = value % MOD
    
    return value


def find_loop_size(target):

    value = 1
    ii = 0

    while value != target:
        ii += 1
        value *= 7
        value = value % MOD

    return ii


def find_encryption_key(door_key, card_key):

    door_loop = find_loop_size(door_key)
    card_loop = find_loop_size(card_key)

    key = loop(door_key, card_loop)

    return key
