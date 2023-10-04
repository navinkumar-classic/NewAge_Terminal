class HashMap(object):
    def __init__(self, size):
        """Initializing the list with the argument size for our HashMap"""
        self.data = [[]] * (size)

    def _hash(self, key):
        """Hash Function:
        marked as a private method in the Object"""

        # Initialize
        hash_value = 0

        # Iterating and generating hashed values using the logic below
        # Logic: Taking the initial value of 0 and adding to it the ASCII encoding for each character,
        # and multiplying by the index value. After that we are taking the modulus of the result using the
        # length of the array
        # This becomes our hashed value i.e. the index position of the input to be placed
        # in the output space
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data)

        return hash_value

    def set(self, key, value):
        # Represents the index position where we want to store our data
        address = self._hash(key)

        if not self.data[address]:
            self.data[address] = []
        # If there is a collision of index value i.e. our hashed value
        # then simply add on to that array
        self.data[address].append([key, value])
        return self.data

    def get(self, key):
        # Getting the hashed value again, with the same hash function to locate the value
        # for the given key
        address = self._hash(key)
        # assigning the entire array to a variable in-order to operate later
        currentBucket = self.data[address]

        if currentBucket:
            # Iterating over the entire list to get the value
            for i in range(len(currentBucket)):
                # Check to retrieve the value
                if currentBucket[i][0] == key:
                    # If found, return the current bucket
                    return currentBucket[i][1],True

        # If no value present
        return "Data Not Found",False

class CQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            return False

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
        return True

    # Delete an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            return "None"

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp
