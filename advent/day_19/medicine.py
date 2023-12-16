from __future__ import annotations

from typing import Sequence, List


def mutations(molecule: str, replacements: tuple[tuple[str, ...], ...]):
    for r in replacements:
        left_ix = 0
        while r[0] in molecule[left_ix:]:
            r_index = molecule.index(r[0], left_ix)
            yield molecule[0:r_index] + r[1] + molecule[r_index + len(r[0]):]
            left_ix = r_index + 1


def replacement_count(molecule: str, replacements: tuple[tuple[str, str], ...]) -> int:

    count = 0
    for r in replacements:
        submolecule = molecule
        left_ix = 0
        while r[0] in submolecule[left_ix:]:
            left_ix = submolecule[left_ix:].index(r[0]) + 1
            submolecule = submolecule[left_ix:]
            count += 1

    return count

def mutation_count(molecule, replacements):
    return len(set(mutations(molecule, replacements)))


def answer_1(lines: Sequence[str]):

    replacements = tuple(
        tuple(line.split(' => ')[0:2]) for line in lines if ' => ' in line
    )

    molecule = lines[-1]
    return mutation_count(molecule, replacements)



def answer_2(lines: Sequence[str]):
    replacements = tuple(
        tuple(line.split(' => ')[0:2]) for line in lines if ' => ' in line
    )
    replacements = tuple(
        [(r[1], r[0]) for r in replacements]
    )

    replacements = sorted(replacements, key=lambda x: len(x[0]))
    replacements = tuple(reversed(replacements))

    molecule = lines[-1]

    steps = 0
    while molecule != 'e':
        m = mutations(molecule, replacements)
        molecule = next(m)
        steps += 1
    return steps


