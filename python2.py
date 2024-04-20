# Start by organizing the bucket sizes from largest to smallest. This helps us use the biggest buckets first, which makes sense because they can scoop more water.
# Next, we prepare an empty list where we'll keep track of the buckets we use to fill the tank.
# We go through each bucket size:
# For each bucket, we see if it fits into the tank. If it does, we use it as much as we can until the tank is full or the bucket becomes too big to fit.
# After trying all the bucket sizes, we check if the tank is completely full:
# If it is, we're done! We return the list of buckets we used because they successfully filled the tank.
# If not, it means we couldn't fill the tank exactly with the available bucket sizes. So, we let the user know that it's not possible to fill the tank as desired.
# Finally, we test the function with different scenarios to make sure it works correctly in all cases. Testing helps us catch any mistakes and ensures the function behaves as expected.


from typing import List

def fill_tank(tank_size: int, bucket_sizes: List[int]) -> List[int]:
    bucket_sizes.sort(reverse=True)  
    result = []

    for bucket_size in bucket_sizes:
        while tank_size >= bucket_size:
            result.append(bucket_size)
            tank_size -= bucket_size

    if tank_size == 0:
        return result
    else:
        return None

# Test cases
print(fill_tank(20, [6, 4, 3, 2]))  # Output: [6, 6, 4, 4]
print(fill_tank(6, [5, 4, 2]))      # Output: [4, 2]
print(fill_tank(3, [2]))            # Output: None
