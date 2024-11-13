
"""Car Fleet
Solved 
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

Example 1:
Input: target = 10, position = [1,4], speed = [3,2]
Output: 1

Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

Example 2:
Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
Output: 3

Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.
"""

def carFleet(target, position, speed):

    # Combine position and speed into a list of tuples with a priority based on the time to reach the target
    cars = [(pos, sp) for pos, sp in zip(position, speed)]
    
    # Sort the list of tuples by the time to reach the target (in descending order)
    cars.sort(reverse=True)

    # Initialize a set to keep track of unique car positions and speeds at any point
    fleets = []

    print("Cars:", cars)

    for pos, sp in cars:
        print(f"Car position: {pos}, Speed: {sp}")
        fleets.append((target - pos) / sp) # Append the time to reach the target divided by the car's speed to the fleets
        print("Fleets:", fleets)
        if len(fleets) > 1 and fleets[-1] <= fleets[-2]:
            fleets.pop()

    print("Fleets:", fleets)

    return len(fleets)

target = 10
position = [4,1,0,7]
speed = [2,2,1,1]

print(carFleet(target, position, speed))
