import pytest

from ..util import get_resource_lines


from advent.day_15.ingredients import *

DAY = "15"

EXAMPLE_ONE = """\
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
""".splitlines()


class TestPartOne:
    pass

    def test_score(self):
        ingredients = [parse_ingredient(line) for line in EXAMPLE_ONE]
        assert (cookie_score(ingredients, [44, 56])) == 62842880

    def test_recipe_generator(self):
        ingredients = [parse_ingredient(line) for line in EXAMPLE_ONE]
        recipes = recipe_generator(ingredients)

        print()
        while recipe := next(recipes, None):
            assert len(recipe) == 2
            assert sum(recipe) == 100

        ingredients.append(Ingredient(
            'Coal Tar', 3, 1, -1, 1, 0
        ))
        recipes = recipe_generator(ingredients)
        while recipe := next(recipes, None):
            assert len(recipe) == 3
            assert sum(recipe) == 100



    def test_example_1(self):
        lines = EXAMPLE_ONE
        expected = 62842880
        actual = answer_1(lines)
        assert expected == actual

    def test_answer_1(self):
        lines = get_resource_lines(DAY)
        answer = answer_1(lines)
        print(f'\nAnswer 1 : {answer}\n')
        # expected =
        # assert expected == answer


EXAMPLE_TWO = EXAMPLE_ONE


class TestPartTwo:
    pass

    # def test_example_2(self):
    #     lines = EXAMPLE_TWO
    #     expected =
    #     actual = answer_2(lines)
    #     assert expected == actual

    def test_answer_2(self):
        lines = get_resource_lines(DAY)
        answer = answer_2(lines)
        print(f'\nAnswer 2 : {answer}\n')
        # expected =
        # assert expected == answer
