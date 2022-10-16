

def deterministic_die():
    while True:
        for i in range(100):
            yield i + 1


def pos_score(position) -> int:
    s = position % 10
    return s if s > 0 else 10


def play(position, score, die):
    for _ in range(3):
        position += next(die)
    score += pos_score(position)
    return position, score


def answer_1(p1: int, p2: int):

    die = deterministic_die()

    p1s, p2s = 0, 0

    rolls = 0

    while p1s < 1000 or p2s < 1000:

        p1, p1s = play(p1, p1s, die)
        rolls += 3
        if p1s >= 1000:
            return p2s * rolls

        p2, p2s = play(p2, p2s, die)
        rolls += 3
        if p2s >= 1000:
            return p1s * rolls

