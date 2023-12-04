#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#
#   ______________________________________________________________   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   |  <<  <<  <>  <|   Advent  of  Code  2023   |>  <>  >>  >>  |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   | + ::|  Day  2  |:: + ::|  Jesse Williams  ∕  xram64  |:: + |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾   #
#             __.-----------.___________________________             #
#            |  |  Answers  |   Part 1: 2061            |            #
#            |  `-----------'   Part 2: 72596           |            #
#            `------------------------------------------'            #
#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#

import re
from functools import reduce
from collections import namedtuple


Cube = namedtuple('Cube', ['amount', 'color'])

class Game:
    def __init__(self, id: str|int, reveals: list[tuple[Cube, ...]]):
        self.id = int(id)
        self.reveals = reveals
        self.is_possible = True
        self.minimal_bag = dict()
        self.minimal_power = 0
    
    def calculate_minimal_bag(self):
        # Determine the minimum amount of each color necessary for this game to be possible
        for reveal in self.reveals:
            for cube in reveal:
                if cube.color not in self.minimal_bag.keys() or cube.amount > self.minimal_bag[cube.color]:
                    self.minimal_bag[cube.color] = cube.amount
    
    def calculate_minimal_power(self):
        # Calculate the power of the set of cubes in the minimal bag (multiply amounts together)
        if len(self.minimal_bag) > 0:
            self.minimal_power = reduce(lambda x,y: x*y, self.minimal_bag.values())

def Setup(filename):
    with open(filename) as f:
        input = f.readlines()
    return [line.strip() for line in input]


#╷----------.
#│  Part 1  │
#╵----------'
def Part1(input, games):
    patt_id = r'(\d+)'
    patt_cube = r'(\d+) (\w+)'
    
    # Parse each line to make a list of Game objects
    for line in input:
        game_sections = list(map(str.strip, line.split(':')))
        game_id = re.findall(patt_id, game_sections[0])[0]
        reveal_sections = list(map(str.strip, game_sections[1].split(';')))
        
        cube_list = []
        for reveal in reveal_sections:
            cubes = re.findall(patt_cube, reveal)
            cubes = tuple(map(lambda c: Cube(int(c[0]), c[1]), cubes))
            cube_list.append(cubes)
            
        games.append(Game(game_id, cube_list))
    
    # Determine which games are possible if the bag contains: `12 red, 13 green, 14 blue`
    bag_contents = {'red': 12, 'green': 13, 'blue': 14}
    possible_games = 0
    
    for game in games:
        for reveal in game.reveals:
            for cube in reveal:
                # If the revealed amount of a given cube exceeds the amount in the bag, flag the game as not possible
                if cube.amount > bag_contents[cube.color]:
                    game.is_possible = False
                    break
        # If the game wasn't flagged, increment the count of possible games by this game's ID
        if game.is_possible:
            possible_games += game.id
    
    return possible_games


#╷----------.
#│  Part 2  │
#╵----------'
def Part2(input, games):
    sum_of_minimal_powers = 0
    
    for game in games:
        game.calculate_minimal_bag()
        game.calculate_minimal_power()
        sum_of_minimal_powers += game.minimal_power
        
    return sum_of_minimal_powers


if __name__ == "__main__":
    input = Setup('day02_input.txt')
    
    games = []
    
    print(f"[Part 1] Sum of IDs of all games that are possible from this bag: {Part1(input, games)}")
    
    print(f"[Part 2] Sum of all powers of minimal cube sets for each game: {Part2(input, games)}")