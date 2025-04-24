######################################################
# Question 2:
# The school's swimming coach has recorded the 50m freestyle 
# swim times (in seconds) for 15 swimmers. 
# Using the list provided, find and display the fastest and slowest swim times, 
# along with their swim lane position in the list.

# Assume that the first item in the list is swim lane position 1.

swim_times = [32.5, 30.1, 33.8, 29.6, 31.2, 34.0, 28.9, 
              30.4, 38.1, 27.5, 35.6, 31.8, 29.2, 33.0, 30.5]


fasttime = swim_times[0]                # Initialize fastest and slowest values
slowtime = swim_times[0]
fastposition = 0
slowposition = 0

for i in range(len(swim_times)):        # Loop through the swim times to find min and max
	if swim_times[i] < fasttime:
		fasttime = swim_times[i]
		fastposition = i

	if swim_times[i] > slowtime:
		slowtime = swim_times[i]
		slowposition = i

print(f"Fastest: Lane {fastposition + 1}, Time: {fasttime}s")   # Add 1 because lanes start from 1
print(f"Slowest: Lane {slowposition + 1}, Time: {slowtime}s")


# or

"""
fastest_time = swim_times[0]            # Initialize fastest and slowest values
slowest_time = swim_times[0]
fastest_lane = 1
slowest_lane = 1

for i in range(len(swim_times)):        # Loop through the swim times to find min and max
    if swim_times[i] < fastest_time:
        fastest_time = swim_times[i]
        fastest_lane = i + 1            # Add 1 because lanes start from 1
    
    if swim_times[i] > slowest_time:
        slowest_time = swim_times[i]
        slowest_lane = i + 1

print("Fastest time: {:.1f} seconds (Lane {})".format(fastest_time, fastest_lane))
print("Slowest time: {:.1f} seconds (Lane {})".format(slowest_time, slowest_lane))


"""
########################################################