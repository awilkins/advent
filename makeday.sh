#!/bin/bash

DAYPAD="0$1"
DAY="${DAYPAD: -2}"

NAME=$2

mkdir {resources,python/{advent,tests}}/day_${DAY}
touch python/{advent,tests}/day_${DAY}/__init__.py

cp templates/python/test_code_head.py "python/tests/day_$DAY/test_$2.py"

{
  echo "DAY=\"$DAY\""
  printf "\nfrom advent.day_%s.%s import *\n" "$DAY" "$NAME"
} >> "python/tests/day_$DAY/test_$2.py"

cat templates/python/test_code_foot.py >> "python/tests/day_$DAY/test_$2.py"


cp templates/python/code.py "python/advent/day_$DAY/$2.py"

code "python/advent/day_$DAY/$2.py" "python/tests/day_$DAY/test_$NAME.py"
