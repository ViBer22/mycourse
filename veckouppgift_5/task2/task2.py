import unittest

def c_to_f(degree):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32

class TestTemperatureConversion(unittest.TestCase):
    def test_c_to_f(self):
        self.assertEqual(c_to_f(0), 32)
        self.assertEqual(c_to_f(100), 212)
        self.assertEqual(c_to_f(-40), -40)
        self.assertIsNone(c_to_f(-300))
        self.assertAlmostEqual(c_to_f(37.78), 100, places=1)

# Funktion count_words

def count_words(sentence):
    return len(sentence.split())

class TestWordCount(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("Hello world"), 2)
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_words("One    two  three"), 3)
        self.assertEqual(count_words("word"), 1)
        self.assertEqual(count_words("   "), 0)

# Funktion find_median

def find_median(numbers):
    if not numbers:
        return None
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    return numbers[mid]

class TestFindMedian(unittest.TestCase):
    def test_find_median(self):
        self.assertEqual(find_median([1, 2, 3]), 2)
        self.assertEqual(find_median([1, 2, 1000]), 2)
        self.assertEqual(find_median([1, 2, 3, 4]), 2.5)
        self.assertEqual(find_median([7]), 7)
        self.assertIsNone(find_median([]))

# Funktion is_sorted_ascending

def is_sorted_ascending(numbers):
    return numbers == sorted(numbers)

class TestIsSortedAscending(unittest.TestCase):
    def test_is_sorted_ascending(self):
        self.assertTrue(is_sorted_ascending([1, 2, 3, 4, 5]))
        self.assertFalse(is_sorted_ascending([5, 3, 1]))
        self.assertTrue(is_sorted_ascending([]))
        self.assertTrue(is_sorted_ascending([42]))
        self.assertFalse(is_sorted_ascending([1, 3, 2, 4]))

if __name__ == "__main__":
    unittest.main()
