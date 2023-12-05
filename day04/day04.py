#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#
#   ______________________________________________________________   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   |  <<  <<  <>  <|   Advent  of  Code  2023   |>  <>  >>  >>  |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   | + ::|  Day  4  |:: + ::|  Jesse Williams  ∕  xram64  |:: + |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾   #
#             __.-----------.___________________________             #
#            |  |  Answers  |   Part 1: 22897           |            #
#            |  `-----------'   Part 2:                 |            #
#            `------------------------------------------'            #
#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#

import re


def Setup(filename):
    with open(filename) as f:
        input = f.readlines()
    return [line.strip() for line in input]


#╷----------.
#│  Part 1  │
#╵----------'
def Part1(input):
    total_points = 0
    
    # Check each card and calculate its points
    for card in input:
        card_fields = [field.strip() for field in re.split(r'[\:\|]', card)]
        
        card_number: int           = int(re.findall(r'(\d+)', card_fields[0])[0])
        winning_nums: list[int]    = list(map(int, card_fields[1].split()))
        scratched_nums: list[int]  = list(map(int, card_fields[2].split()))
        
        # Determine which numbers appear in both the winning and scratched fields
        numbers_matched = set(winning_nums).intersection(set(scratched_nums))
        if len(numbers_matched) == 0: continue  # Skip points if no numbers match on this card
        
        # Calculate the points for this card and add it to the total
        card_points = 2 ** (len(numbers_matched) - 1)
        total_points += card_points
    
    return total_points


#╷----------.
#│  Part 2  │
#╵----------'
def Part2(input):
    ...


if __name__ == "__main__":
    input = Setup('day04_input.txt')
    
    print(f"[Part 1] Total points across all scratchcards: {Part1(input)}")
    
    # print(f"[Part 2] : {Part2(input)}")