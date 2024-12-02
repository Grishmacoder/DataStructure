from collections import OrderedDict
from typing import Any, Optional

class LRU_Cache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.my_dict = OrderedDict()

    def get(self, key: int) -> Optional[Any]:
        if key in self.my_dict:
            self.my_dict.move_to_end(key)
            return self.my_dict[key]
        return -1

    def set(self, key: int, value: Any) -> None:
        if key in self.my_dict:
            self.my_dict[key] = value
            self.my_dict.move_to_end(key)
        else:
            if len(self.my_dict) >= self.capacity:
                self.my_dict.popitem(last=False)

            self.my_dict[key] = value


if __name__ == '__main__':
    # Testing the LRU_Cache class

    # Test Case 1: Basic functionality
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    print(our_cache.get(1))   # Returns 1
    print(our_cache.get(2))    # Returns 2
    print(our_cache.get(9))   # Returns -1 because 9 is not in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)  # This should evict key 3
    print(our_cache.get(3))  # Returns -1, 3 was evicted

    # Test Case 2
    second_cache = LRU_Cache(10)
    second_cache.set(1,0)
    second_cache.set(2,'')
    second_cache.set(3,2)
    second_cache.set(4,None)
    print("Test case empty value", second_cache.get(2))   #Returns empty
    print("Test case None value", second_cache.get(4))    #Returns None

    # Test Case 3
    third_cache= LRU_Cache(5*10**6)
    third_cache.set(1,1)
    third_cache.set(101,101)
    print("large value cache", third_cache.get(101))
