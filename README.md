# Advent of Code

## General

### `makeday.sh`

Why bother with all that tedious writing of boilerplate? The Advent format is
pretty predictable and hasn't changed in years.

- You'll have to write two functions
- You'll be working with an input file

So this script creates some code from templates and grabs the input for you.

For this you'll need your session token for Advent of Code, which you can grab
from your browser session - after you've logged in, it will be in your cookies
each time you make a page request, so bash F12 and go to the network tab and
find it.

You need to export this to your environment as `AOC_TOKEN` ; I've put it in 

Note that it's very rude to grab the input EVERY TIME you run your code.
