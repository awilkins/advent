from __future__ import annotations

from typing import Dict, List, NewType, Set, Tuple, cast


Product = NewType('Product', Tuple[List[str], List[str]])
ProductList = NewType('ProductList', List[Product])

def parse_input(lines: List[str]) -> ProductList:

    output: ProductList = ProductList([])
    for line in lines:
        ingredients, allergens = line.split(' (contains ')
        allergens = allergens[:-1].split(', ')
        ingredients = ingredients.split(' ')
        product: Product = Product((ingredients, allergens))
        output.append(product)

    # List of tuples of list of food comma list of allergens
    return output


def find_non_allergenic_ingredients(products: ProductList) -> Tuple[Set[str], Dict[str, str]]:

    all_allergens: Set[str] = set([])
    all_ingredients: Set[str] = set([])

    for ingredients, allergens in products:
        all_allergens.update(allergens)
        all_ingredients.update(ingredients)

    possible_allergens: Dict[str, Set[str]] = {}
    for allergen in all_allergens:
        possible_allergens[allergen] = all_ingredients.copy()

    for ingredients, allergens in products:
        for allergen in allergens:
            possible_allergens[allergen].intersection_update(ingredients)

    more_than_1 = { a: i for a, i in possible_allergens.items() if len(i) > 1 }
    while len(more_than_1) != 0:
        only_1 = { a: i for a, i in possible_allergens.items() if len(i) == 1 }
        for iset in only_1.values():
            for ingredient in iset:
                for big_iset in more_than_1.values():
                    big_iset.discard(ingredient)
        more_than_1 = { a: i for a, i in possible_allergens.items() if len(i) > 1 }

    allergenic_ingredients = set([])
    for iset in possible_allergens.values():
        allergenic_ingredients.update(iset)

    allergen_output: Dict[str, str] = {}
    only_1 = { a: i for a, i in possible_allergens.items() if len(i) == 1 }
    for allergen, iset in only_1.items():
        for i in iset:
            allergen_output[allergen] = i

    return all_ingredients.difference(allergenic_ingredients), allergen_output


