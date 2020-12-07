

from typing import Dict, List

SHINY_GOLD = 'shiny gold'

class Bag(object):

    def __init__(self, rule: str, container=None):
        colour, ruleset = rule.rstrip('.').split(' bags contain ')
        self.colour = colour
        self.contents: Dict[str, int] = {}

        if ruleset == "no other bags":
            return

        for rule in ruleset.split(', '):
            rule_words = rule.split(' ')
            count, colour = rule_words[0], ' '.join(rule_words[1:3])
            self.contents[colour] = int(count)

    def can_contain(self, colour: str) -> bool:
        return colour in self.contents.keys()

bags: Dict[str, Bag] = {}

def construct_rules(rules: List[str]):
    global bags
    bags = {}
    for rule in rules:
        new_bag = Bag(rule)
        bags[new_bag.colour] = new_bag

def bags_of_gold(rules: List[str]) -> int:
    construct_rules(rules)

    shiny_gold = bags[SHINY_GOLD]

    golden_bags: Dict[str, Bag] = { shiny_gold.colour: shiny_gold }

    bag_count = 0
    while bag_count != len(golden_bags):
        bag_count = len(golden_bags)
        new_bags = {}
        for bag in golden_bags.values():
            for other in bags.values():
                if other.can_contain(bag.colour):
                    new_bags[other.colour] = other
        golden_bags.update(new_bags)

    del golden_bags[SHINY_GOLD]
    return len(golden_bags)

def count_sub_bags(bag: Bag) -> int:
    bag_count = 0
    for colour, count in bag.contents.items():
        sub_bag = bags[colour]
        bag_count += (count_sub_bags(sub_bag) + 1) * count

    return bag_count

def bags_in_gold(rules: List[str]) -> int:
    construct_rules(rules)

    shiny_gold = bags[SHINY_GOLD]

    return count_sub_bags(shiny_gold)


