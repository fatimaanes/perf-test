# Demo benchmarks showcasing ASV capabilities
import time
import random
import math


class DataStructureSuite:
    """
    Benchmarks for comparing different data structures and operations.
    """
    
    def setup(self):
        self.size = 1200  # Increased size for different performance
        self.data = list(range(self.size))
        self.dict_data = {i: i for i in range(self.size)}
        self.search_keys = [random.randint(0, self.size-1) for _ in range(100)]

    def time_list_creation(self):
        """Time creating a list"""
        return list(range(self.size))

    def time_dict_creation(self):
        """Time creating a dictionary"""
        return {i: i for i in range(self.size)}

    def time_list_search(self):
        """Time searching in a list"""
        for key in self.search_keys:
            key in self.data

    def time_dict_search(self):
        """Time searching in a dictionary"""
        for key in self.search_keys:
            key in self.dict_data

    def time_list_append(self):
        """Time appending to a list"""
        result = []
        for i in range(80):  # Reduced iterations for better performance
            result.append(i)

    def time_list_extend(self):
        """Time extending a list"""
        result = []
        result.extend(range(100))


class MathSuite:
    """
    Mathematical operation benchmarks with different input sizes.
    """
    params = [100, 1000, 5000]
    param_names = ['size']

    def setup(self, size):
        self.numbers = [random.random() for _ in range(size)]

    def time_sum_builtin(self, size):
        """Time built-in sum function"""
        return sum(self.numbers)

    def time_sum_manual(self, size):
        """Time manual sum calculation"""
        total = 0
        for num in self.numbers:
            total += num
        return total

    def time_sqrt_operations(self, size):
        """Time square root operations"""
        return [math.sqrt(x) for x in self.numbers]

    def time_pow_operations(self, size):
        """Time power operations"""
        return [x ** 2 for x in self.numbers]


class StringSuite:
    """
    String operation benchmarks.
    """
    
    def setup(self):
        self.words = ['hello', 'world', 'python', 'benchmark'] * 100
        self.text = ' '.join(self.words)

    def time_string_join(self):
        """Time string joining"""
        return ' '.join(self.words)

    def time_string_split(self):
        """Time string splitting"""
        return self.text.split()

    def time_string_upper(self):
        """Time string upper case conversion"""
        return [word.upper() for word in self.words]

    def time_string_replace(self):
        """Time string replacement"""
        return self.text.replace('hello', 'hi')


class MemorySuite:
    """
    Memory usage benchmarks.
    """
    
    def mem_small_list(self):
        """Memory usage of a small list"""
        return [0] * 100

    def mem_large_list(self):
        """Memory usage of a large list"""
        return [0] * 10000

    def mem_dict_small(self):
        """Memory usage of a small dictionary"""
        return {i: i for i in range(100)}

    def mem_dict_large(self):
        """Memory usage of a large dictionary"""
        return {i: i for i in range(10000)}

    def mem_nested_structure(self):
        """Memory usage of nested data structures"""
        return [[i for i in range(10)] for _ in range(100)]


class TrackingSuite:
    """
    Custom tracking benchmarks for specific metrics.
    """
    
    def track_fibonacci_result(self):
        """Track the 20th Fibonacci number"""
        a, b = 0, 1
        for _ in range(20):
            a, b = b, a + b
        return a

    def track_prime_count(self):
        """Track count of prime numbers up to 100"""
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        return sum(1 for i in range(2, 100) if is_prime(i))

    def track_list_length(self):
        """Track length of generated list"""
        return len([x for x in range(50) if x % 2 == 0])

    # Set units for tracking benchmarks
    track_fibonacci_result.unit = "value"
    track_prime_count.unit = "count"
    track_list_length.unit = "items"
