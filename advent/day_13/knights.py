from __future__ import annotations

from itertools import permutations, chain, pairwise

from typing import Sequence, Iterable, List

class Relationship:

    person: str
    score: int
    other_person: str

    def __init__(self, line: str):
        parts = line.split()
        #   0    1     2    3    4        5    6   7      8   9   10
        # Alice would gain 54 happiness units by sitting next to Bob.
        person, operation, amount, other_person = [parts[index] for index in [0, 2, 3, 10]]

        self.person = person
        self.other_person = other_person.rstrip('.')
        self.score = - int(amount) if operation == 'lose' else int(amount)

    def __repr__(self):
        return f'{self.person} -[{self.score}]-> {self.other_person}'

def score(relations, arrangement: Iterable[str]) -> int:

    arrangement = list(arrangement)
    pairs = list(chain(
        [(arrangement[-1], arrangement[0])],
        pairwise(arrangement),
    ))
    table_rels = []
    table_rels.extend(relations[pair[0] + pair[1]] for pair in pairs)
    table_rels.extend(relations[pair[1] + pair[0]] for pair in pairs)
    return sum(rel.score for rel in table_rels)

def answer_1(lines: Sequence[str], arrangements=None):
    relations = [Relationship(line) for line in lines]
    people = set(relation.person for relation in relations)
    relations = {
        rel.person + rel.other_person: rel for rel in relations
    }
    arrangements = arrangements or permutations(people)
    scores = [score(relations, arrangement) for arrangement in arrangements]
    return max(scores)




def answer_2(lines: Sequence[str], arrangements=None):
    relations = [Relationship(line) for line in lines]
    people = set(relation.person for relation in relations)

    # insert myself
    apathy = []
    apathy.extend(Relationship(
        f'Adrian would give 0 f**ks about sitting with that git {person}'
    ) for person in people)
    apathy.extend(Relationship(
        f'{person} also gives 0 f**ks about sitting with that prat Adrian'
    ) for person in people)
    people.add('Adrian')

    relations.extend(apathy)

    relations = {
        rel.person + rel.other_person: rel for rel in relations
    }
    arrangements = arrangements or permutations(people)
    scores = [score(relations, arrangement) for arrangement in arrangements]
    return max(scores)
