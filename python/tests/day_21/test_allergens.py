from unittest import TestCase

from ..util import get_resource

DAY="21"

from advent.day_21.allergens import *

EXAMPLE_INPUT = """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""

class TestThing(TestCase):


    def test_parse_example_1(self):
        lines = EXAMPLE_INPUT.splitlines()
        actual = parse_input(lines)

        self.assertIn("kfcds", actual[0][0])
        self.assertIn("fish", actual[3][1])


    def test_non_allergens(self):
        lines = EXAMPLE_INPUT.splitlines()
        products = parse_input(lines)
        non_allergenic, _ = find_non_allergenic_ingredients(products)
        expected = set([
            "kfcds", "nhms", "sbzzf", "trh"
        ])
        self.assertSetEqual(expected, non_allergenic)


    def test_answer_1(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        products = parse_input(lines)
        non_allergenic, _ = find_non_allergenic_ingredients(products)

        count = 0
        for ingredients, _ in products:
            for ingredient in ingredients:
                if ingredient in non_allergenic:
                    count += 1

        answer = count
        print(f'\nAnswer 1 : {answer}\n')

        expected = 2075
        self.assertEqual(expected, answer)

    def test_answer_2(self):
        lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()
        products = parse_input(lines)
        _, allergens = find_non_allergenic_ingredients(products)

        allergen_names = list(allergens.keys())
        allergen_names.sort()
        ingredient_names = []
        for name in allergen_names:
            ingredient_names.append(allergens[name])

        answer = ",".join(ingredient_names)
        print(f'\nAnswer 2 : {answer}\n')

        # expected =
        # self.assertEqual(expected, answer)

