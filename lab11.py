import unittest

num1 = input()
num2 = input()
def is_subarray(nums1, nums2):
    i = 0

    for num in nums2:
        if i < len(nums1) and num == nums1[i]:
            i += 1

    return i == len(nums1)

print(is_subarray(num1, num2))


""" 
class TestSubarray(unittest.TestCase):

    def test_case_1(self):
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3, 4]
        self.assertTrue(is_subarray(nums1, nums2))

    def test_case_2(self):
        nums1 = [4, 2]
        nums2 = [1, 2, 3, 4]
        self.assertFalse(is_subarray(nums1, nums2))

    def test_case_3(self):
        nums1 = [1, 3, 5]
        nums2 = [1, 2, 3, 4, 5]
        self.assertTrue(is_subarray(nums1, nums2))


if __name__ == "__main__":
    unittest.main()
"""