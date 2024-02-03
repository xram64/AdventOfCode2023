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
#            |  `-----------'   Part 2: 51399228        |            #
#            `------------------------------------------'            #
#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#

# Maps: (Destination range start, Source range start, Range length)


import time
from math import inf as INFINITY
from collections import OrderedDict
import multiprocessing

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

# [SeedPair] Represents the start and length of a seed range. (Part 2)
class SeedPair:
    def __init__(self, seed_range_start, seed_range_length):
        self.start: int = int(seed_range_start)
        self.length: int = int(seed_range_length)


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
    return min(seeds_to_locations.values())


#╷----------.
#│  Part 2  │
#╵----------'
# Worker function for parallelization
def process_seeds(seeds_range: range, mapsets: OrderedDict[str, Mapset]) -> int:
    # Process seeds in this range
    lowest_location = INFINITY
    for seed in seeds_range:
        location = seed
        for mapset in mapsets.values():
            location = mapset.apply_mappings(location)
        # Check if the location derived from this seed has a lower number than the current lowest
        if location < lowest_location:
            lowest_location = location
    
    # Check the number of seeds processed in this batch and increment the counter to match
    with m.get_lock():
        m.value += len(seeds_range)
    
    # Return the lowest location number found in this batch, along with the number of seeds in the batch for counting
    return lowest_location
        
# Callback function for parallelization
def process_seeds_callback(batch_min_location_value: int) -> None:
    m_total = 1_753_244_662
    
    # Print timing info
    t_e = time.time() - t_s
    t_hrs, rem = divmod(t_e, 3600)
    t_mins, t_secs = divmod(rem, 60)
    m_rate = m.value / t_e
    m_rate_hrs, rem = divmod(m_total / m_rate, 3600)
    m_rate_mins, m_rate_secs = divmod(rem, 60)
    print(
        f'Mapping seed {m.value:>13,} of {m_total:,} || ',
        f'Time elapsed: {int(t_hrs):>1}:{int(t_mins):0>2}:{int(t_secs):0>2} || ',
        f'Average map rate: {round(m_rate, 2):>12,.2f} maps/sec || ',
        f'Projected total run time: {int(m_rate_hrs):>2}:{int(m_rate_mins):0>2}:{int(m_rate_secs):0>2}',
        flush=True
    )
    
    # Add the min location value that was returned for this batch to the list of minimums
    min_location_values.append(batch_min_location_value)

# Function to initialize shared global variables at the start of each new process
# (Ref: https://stackoverflow.com/questions/73767606/how-do-i-uses-pythons-multiprocessing-value-method-with-map)
def process_init_values(shared_m: int) -> None:
    # Create a global variable named `m` within the process
    global m
    m = shared_m

def Part2(input):
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
    
    # Seed pairs: [seed_range_start, seed_range_length]
    seed_numbers = [int(s) for s in input[0].split(':')[1].split()]  # Get seeds from input file
    seed_pairs: list[SeedPair] = [SeedPair(seed_numbers[2*n], seed_numbers[2*n+1]) for n in range(len(seed_numbers) // 2)]
    
    # Set up multiprocessing pool to parallelize seed checking
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count(), initializer=process_init_values, initargs=(m,))
    
    for seed_pair in seed_pairs:  # Total seeds to map: 1,753,244,662
        
        # Collect all seeds in the range for this pair and map them through each mapset.
        seeds_range = range(seed_pair.start, seed_pair.start + seed_pair.length)
        
        # Put each range into the process pool
        pool.apply_async(process_seeds, args=(seeds_range, mapsets), callback=process_seeds_callback)

    # Close the pool and wait for the work to finish
    pool.close()
    pool.join()

    # Determine the lowest location number out of all the batch minimums that were found.
    return min(min_location_values)


if __name__ == "__main__":
    input = Setup('day05_input.txt')
    
    print(f"[Part 1] Lowest location number found: {Part1(input)}")
    
    # Global variables for Part 2
    manager = multiprocessing.Manager()
    min_location_values = manager.list()    # Minimum location values returned from each batch
    m = multiprocessing.Value('i', 0)       # Number of processed seeds
    t_s = time.time()                       # Start time
    
    print(f"[Part 2] Lowest location number found: {Part2(input)}")
