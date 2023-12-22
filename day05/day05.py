#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#
#   ______________________________________________________________   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   |  <<  <<  <>  <|   Advent  of  Code  2023   |>  <>  >>  >>  |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   | + ::|  Day  5  |:: + ::|  Jesse Williams  ∕  xram64  |:: + |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾   #
#             __.-----------.___________________________             #
#            |  |  Answers  |   Part 1: 535088217       |            #
#            |  `-----------'   Part 2:                 |            #
#            `------------------------------------------'            #
#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#

# Maps: (Destination range start, Source range start, Range length)


from collections import OrderedDict

MAP_HEADERS = OrderedDict({
    "seed->soil": "seed-to-soil map:",
    "soil->fertilizer": "soil-to-fertilizer map:",
    "fertilizer->water": "fertilizer-to-water map:",
    "water->light": "water-to-light map:",
    "light->temperature": "light-to-temperature map:",
    "temperature->humidity": "temperature-to-humidity map:",
    "humidity->location": "humidity-to-location map:"
})


# [Mapping] Represents a single mapping range.
class Mapping:
    def __init__(self, dest_range_start, source_range_start, range_length, maptype):
        self.dest_range_start: int = int(dest_range_start)
        self.source_range_start: int = int(source_range_start)
        self.dest_range_end: int = int(dest_range_start) + int(range_length) - 1
        self.source_range_end: int = int(source_range_start) + int(range_length) - 1
        self.range_length: int = int(range_length)
        self.offset: int = int(dest_range_start) - int(source_range_start)
        self.maptype: str = maptype
    
    # Returns the destination for the given source based on this mapping.
    def source_to_dest(self, source):
        if self.source_range_start <= source <= self.source_range_end:
            dest = source + self.offset
        else:
            dest = source
        return dest


# [Mapset] Represents a set of maps for a given mapping category.
class Mapset:
    def __init__(self, maps, maptype):
        self.maptype: str = maptype
        self.maps: list[Mapping] = maps
    
    # Returns the result of mapping the source through this mapset.
    def apply_mappings(self, source):
        mapped_source = source
        for mapping in self.maps:
            mapped_source = mapping.source_to_dest(mapped_source)
            if mapped_source != source: break  # If the source has changed, a mapping has been used, so stop checking here.
        return mapped_source


def Setup(filename):
    with open(filename) as f:
        input = f.readlines()
    return [line.strip() for line in input]


#╷----------.
#│  Part 1  │
#╵----------'
def Part1(input):
    mapsets: OrderedDict[str, Mapset] = OrderedDict()
    
    # For each mapping header string, locate the header and read the items below it into a Mapset.
    for maptype, header in MAP_HEADERS.items():
        header_index = input.index(header)  # Index of this header
        end_index = input[header_index:].index('') + header_index  # Index of the first empty line after this header
        
        # Capture each line in this mapping section as a Mapping in a Mapset.
        maps = []
        
        for map_line in range(header_index+1, end_index):
            maps.append(Mapping(*input[map_line].split(), maptype))
        mapsets[maptype] = Mapset(maps, maptype)
    
    # Convert each seed to its corresponding location, after passing through all mappings.
    seeds_to_locations: dict[int, int] = {}
    
    seeds = [int(s) for s in input[0].split(':')[1].split()]  # Get seeds from input file
    
    for seed in seeds:
        seed_dest = seed
        for mapset in mapsets.values():
            seed_dest = mapset.apply_mappings(seed_dest)
        seeds_to_locations[seed] = seed_dest
    
    # Determine the lowest location number that results from any of the starting seeds.
    print(seeds_to_locations)
    return min(seeds_to_locations.values())


#╷----------.
#│  Part 2  │
#╵----------'
def Part2(input):
    ...


if __name__ == "__main__":
    input = Setup('day05_input.txt')
    
    print(f"[Part 1] Lowest location number found: {Part1(input)}")
    
    # print(f"[Part 2] : {Part2(input)}")