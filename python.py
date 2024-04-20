# We iterate through each leg of the journey using a loop (for leg in legs).
# At each step, we check if the battery's energy level falls below 0. If it does, we return -1 because it's not possible to reach the destination.
# If the battery's energy level is less than or equal to the energy required for the next leg, we charge the battery to full capacity.
# We continue this process until we reach the destination or determine that it's not possible to reach the destination without letting the battery's level fall below 0.

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
print(num_charging_stops([25], 30))         # Output: 0
print(num_charging_stops([25, 25], 30))     # Output: 1
print(num_charging_stops([50], 30))         # Output: -1
print(num_charging_stops([15, 15, 30], 30)) # Output: 1
print(num_charging_stops([15, 30, 15], 30)) # Output: 2
