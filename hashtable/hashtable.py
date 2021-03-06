import warnings


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        current = self.head

        while current is not None:
            
            if current.key == key:
                return current
            current = current.next

        return current
    
    def head_update_insert(self, key, value):
        # check if the key is already in the linked list
            # find the node
        current = self.head
        while current is not None:
            # if key is found, change the value
            if current.key == key:
                current.value = value
                # exit function immediately
                return
            current = current.next
        # if we reach the end of the list, it's not here! 
        # make a new node, and insert at head
        new_node = HashTableEntry(key, value)
        new_node.next = self.head
        self.head = new_node

    def tail_update_insert(self, key, value):
        # walk through and check if key is here
        current = self.head
        while current is not None:
            # if key is found, change the value
            if current.key == key:
                current.value = value
                # exit function immediately
                return
            current = current.next
            if current.next is None:
            # if not, make a new node and insert at tail
                new_node = HashTableEntry(key, value)
                current.next = new_node
        

    def delete(self, key):
        # walk through and check if key is here
        current = self.head
        previous = current
        if self.head.key == key and self.head.next is not None:
            current.value = None
            current.next = self.head
            return
        if self.head.next is None and self.head.key is key:
            self.head = None
            return
        while current is not None:
            if current.key == key:
                current.value == None
                previous.next = current.next
            # increment
            current = current.next
    
# Hash table can't have fewer than this many slots
# MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = 0
        self.storage = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.items / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """

        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Day1
        # self.storage[self.hash_index(key)] = value

        # Day2
        # find the the index
        idx = self.hash_index(key)
        load = self.get_load_factor()
        if (load > 0.7):
            self.resize(self.capacity * 2)
        if self.storage[idx] == None:
            self.storage[idx] = LinkedList()
            self.storage[idx].head_update_insert(key, value)
            self.items += 1
            return
        self.storage[idx].head_update_insert(key, value)
        self.items += 1

        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Day1
        # if not key:
        #     print(warnings.warn("The key is not found!"))
        # else:
        #     self.storage[self.hash_index(key)] = None

        # Day2
        idx = self.hash_index(key)
        if self.storage is None:
            return "Nothing there to Delete"
        self.storage[idx].delete(key)
        self.items -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Day1
        # if not key:
        #     return None
        # else:
        #     return self.storage[self.hash_index(key)]

        # Day2
        idx = self.hash_index(key)
        if self.storage[idx] is None:
            return None
        found = self.storage[idx].find(key)
        if found is None:
            return
        return found.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # set up a new storage with new capacity
        new_storage = [None] * new_capacity
        # loop thru old storage
        for i in range(self.capacity):
            # check for stored items
            if self.storage[i] is not None:
                # create current variable
                current = self.storage[i].head
                # access new hash index for new storage
                idx = self.djb2(current.key) % new_capacity
                # instantiate a linked List
                new_storage[idx] = LinkedList()
                # check the old linked list for items
                while current is not None:
                    # insert values in new storage
                    new_storage[idx].head_update_insert(current.key, current.value)
                    # increment
                    current = current.next
                
        # re-assign and exit function   
        self.storage = new_storage 
        self.capacity = new_capacity
        return


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
