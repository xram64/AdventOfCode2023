#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#
#   ______________________________________________________________   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   |  <<  <<  <>  <|   Advent  of  Code  2023   |>  <>  >>  >>  |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   | + ::|  Day  3  |:: + ::|  Jesse Williams  ∕  xram64  |:: + |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾   #
#             __.-----------.___________________________             #
#            |  |  Answers  |   Part 1: 553079          |            #
#            |  `-----------'   Part 2:                 |            #
#            `------------------------------------------'            #
#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#

# Note: Part numbers in the matrix are not unique

import re
import numpy as np
from numpy.typing import NDArray


def Setup(filename):
    with open(filename) as f:
        input = f.readlines()
    return [line.strip() for line in input]


# Returns all part numbers that are adjacent to a symbol with the given `coords`
def find_adjacent_partnums(coords: tuple[int, int], schematic: NDArray) -> dict[tuple, int]:
    partnums: dict[tuple, int] = {}
    partnum_coords: list[NDArray] = []
    
    # Convert current coords into a (row, col) vector
    symbol_coords = np.array(coords, dtype=int)
    
    # Construct a set of coordinate offset masks for generating adjacent coord pairs
    masks = [np.array((i,j)) for i in [-1,0,1] for j in [-1,0,1] if (i,j) != (0,0)]
    
    # Apply each mask to the current coords
    for mask in masks:
        adj_coords = symbol_coords + mask
        # Check that masked coords are within matrix bounds
        if 0 <= adj_coords[0] < schematic.shape[0] and 0 <= adj_coords[1] < schematic.shape[1]:
            # Check if the matrix contains a digit at these coords
            if re.match(r'\d+', str(schematic[tuple(adj_coords)])):
                partnum_coords.append(adj_coords)
    
    # Look around the coords of the found digit to get the full part number in that location
    for row, col in partnum_coords:
        # Compress the row into a string and split on non-digit chars to isolate the surrounding number
        partnum_row = ''.join(schematic[row])
        partnum = re.split(r'[^\d]', partnum_row[:col])[-1] + re.split(r'[^\d]', partnum_row[col:])[0]
        
        # Store each partnum in a dict, with an "ID" corresponding to the (row, col) coords
        #   of the first digit of the number as the key, and the part number as the value.
        # This way, we can keep track of which partnums in the matrix have been seen before.
        partnum_id = (row, col - len(re.split(r'[^\d]', partnum_row[:col])[-1]))
        
        partnums[partnum_id] = int(partnum)
    
    return partnums

#╷----------.
#│  Part 1  │
#╵----------'
def Part1(input):
    all_partnums: dict[tuple, int] = {}
    
    # Convert each line string into a list of characters, making each a row in the 'schematic' matrix
    schematic = np.array([list(line) for line in input])
    
    # Populate a list of the coords of each symbol in the entire matrix
    schematic_symbol_coords: list[tuple] = []
    for i in range(schematic.shape[0]):
        for j in range(schematic.shape[1]):
            if re.match(r'([^\w\s\.])', schematic[i, j]):
                schematic_symbol_coords.append((i, j))
    
    # For each symbol, check for any adjacent part numbers and merge them into the full dict
    # If any duplicate part numbers are found adjacent to different symbols, their entries
    #   will be overwritten so that they won't be overcounted.
    for coords in schematic_symbol_coords:
        all_partnums.update(find_adjacent_partnums(coords, schematic))
    
    return sum(all_partnums.values())


#╷----------.
#│  Part 2  │
#╵----------'
def Part2(input):
    ...


if __name__ == "__main__":
    input = Setup('day03_input.txt')
    
    print(f"[Part 1] Sum of all part numbers in the schematic: {Part1(input)}")
    
    # print(f"[Part 2] : {Part2(input)}")