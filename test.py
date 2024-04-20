from typing import List

def num_charging_stops(legs: List[int], capacity: int) -> int:
    current_energy = capacity
    stops = 0
    
    for leg in legs:
        current_energy -= leg
        
        if current_energy < 0:
            return -1
        
        if current_energy < leg:
            stops += 1
            current_energy = capacity
    
    return stops

# Test cases
print(num_charging_stops([25], 30))       # Output: 0
print(num_charging_stops([25, 25], 30))   # Output: 1
print(num_charging_stops([50], 30))       # Output: -1
print(num_charging_stops([15, 15, 30], 30))# Output: 1
print(num_charging_stops([15, 30, 15], 30))# Output: 2

