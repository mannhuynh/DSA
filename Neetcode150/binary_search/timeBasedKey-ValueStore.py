"""Implement a time-based key-value data structure that supports:

Storing multiple values for the same key at specified time stamps
Retrieving the key's value at a specified timestamp
Implement the TimeMap class:
TimeMap() Initializes the object.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".
Note: For all calls to set, the timestamps are in strictly increasing order.

Example 1:

Input:
["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

Output:
[null, null, "happy", "happy", null, "sad"]
Explanation:
TimeMap timeMap = new TimeMap();
timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
timeMap.get("alice", 1);           // return "happy"
timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
timeMap.get("alice", 3);           // return "sad"

Constraints:
1 <= key.length, value.length <= 100
key and value only include lowercase English letters and digits.
1 <= timestamp <= 1000
"""
class TimeMap:
    # Initialize the data structure with an empty dictionary to store key-value pairs
    def __init__(self):
        self.store_map = {} 

    # Set a new key-value pair at the specified timestamp, maintaining increasing timestamps for each key
    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key is not in the dictionary yet, add it with an empty list to store values and timestamps
        if key not in self.store_map:
            self.store_map[key] = []
        # Append a new value-timestamp pair to the list for this key
        self.store_map[key].append([value, timestamp])

    # Retrieve the most recent value of a given key up to a specified timestamp using binary search
    def get(self, key: str, timestamp: int) -> str:
        result = ''
        # Get the list of values and timestamps for this key (empty if not present)
        value_list = []
        if key in self.store_map:
            value_list = self.store_map[key]
        
        # value_list = self.store_map.get(key,[])
        
        # Initialize binary search bounds
        left = 0
        right = len(value_list) - 1

        while left <= right:
            # Calculate the midpoint of the current range
            mid = (left + right) // 2
            
            # If the timestamp at the midpoint is less than or equal to the target, update the result and move the left bound past this index
            if value_list[mid][1] <= timestamp:
                result = value_list[mid][0]
                left = mid + 1
            # Otherwise, the key-value pair at the current midpoint has a later timestamp, so we can eliminate all values to its right by moving the right bound to this index
            else:
                right = mid - 1

        return result

sol = TimeMap()
sol.set("alice", "happy", 1)
sol.set("alice", "sad", 3)
sol.set("alice", "neutral", 7)
print(sol.get("alice", 8))



        

