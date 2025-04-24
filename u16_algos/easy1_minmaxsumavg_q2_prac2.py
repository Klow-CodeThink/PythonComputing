######################################################
# Question 2:
# The school's swimming coach has recorded the 50m freestyle 
# swim times (in seconds) for 15 swimmers. 
# Using the list provided, find and display the fastest and slowest swim times, 
# along with their swim lane position in the list.

# Assume that the first item in the list is swim lane position 1.

swim_times = [32.5, 30.1, 33.8, 29.6, 31.2, 34.0, 28.9, 
              30.4, 38.1, 27.5, 35.6, 31.8, 29.2, 33.0, 30.5]


fast_time = swim_times[0]
slow_time = swim_times[0]
fast_lane = 0
slow_lane = 0

for i in range(len(swim_times)):
    if swim_times[i] < fast_time:
        fast_time = swim_times[i]
        fast_lane = i + 1
    
    if swim_times[i] > slow_time:
        slow_time = swim_times[i]
        slow_lane = i + 1

print(f"Lane {fast_lane} has the fastest swim time of {fast_time} seconds.")
print(f"Lane {slow_lane} has the slowest swim time of {slow_time} seconds.")
