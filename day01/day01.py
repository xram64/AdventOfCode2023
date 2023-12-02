#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#
#   ______________________________________________________________   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   |  <<  <<  <>  <|   Advent  of  Code  2023   |>  <>  >>  >>  |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   | + ::|  Day  1  |:: + ::|  Jesse Williams  ∕  xram64  |:: + |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾   #
#             __.-----------.___________________________             #
#            |  |  Answers  |   Part 1: 55002           |            #
#            |  `-----------'   Part 2: 55093           |            #
#            `------------------------------------------'            #
#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#


def Setup(filename):
    with open(filename) as f:
        input = f.readlines()
    return [line.strip() for line in input]


#╷----------.
#│  Part 1  │
#╵----------'
def Part1(input):
    INTS = [str(i) for i in range(10)]
    
    calibration_values = []
    
    for line in input:
        digits = [d for d in line if d in INTS]
        calibration_values.append(int(digits[0] + digits[-1]))

    return sum(calibration_values)


#╷----------.
#│  Part 2  │
#╵----------'
def Part2(input):
    INTS = [str(i) for i in range(10)]
    WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    WORD_TO_INT = {k:v for (k, v) in zip(WORDS, INTS)}

    calibration_values = []
    
    for line in input:
        first_num = (len(line), '')   # (index, number)
        last_num = (-1, '')           # (index, number)
        
        # Check for each int/word in the string and record its position (index of first character)
        for num in (INTS + WORDS):
            # First, check that number is found in line
            if num in line:
                
                # Get first index from left
                if (left := line.find(num)) < first_num[0]:
                    first_num = (left, num)
            
                # Get first index from right
                if (right := line.rfind(num)) > last_num[0]:
                    last_num = (right, num)
            
            # If the current first/last numbers are both at the start/end of the line, end loop early
            if (first_num[0] == 0) and (last_num[0] + len(last_num[1]) == len(line)):
                break
            
        # Convert final digit values into integers and add combined number to list
        first_digit = WORD_TO_INT[first_num[1]] if (first_num[1] in WORDS) else first_num[1]
        last_digit = WORD_TO_INT[last_num[1]] if (last_num[1] in WORDS) else last_num[1]
            
        calibration_values.append(int(first_digit + last_digit))
        
    return sum(calibration_values)


if __name__ == "__main__":
    input = Setup('day01_input.txt')
    
    print(f"[Part 1] Sum of calibration values: {Part1(input)}")
    
    print(f"[Part 2] Sum of corrected calibration values: {Part2(input)}")