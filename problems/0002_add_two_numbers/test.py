import unittest
from solution import Solution, ListNode
from typing import Optional, List

def build_linked_list(vals: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        l1 = build_linked_list([2, 4, 3])
        l2 = build_linked_list([5, 6, 4])
        result = self.solution.add_two_numbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [7, 0, 8])

    def test_example2(self):
        l1 = build_linked_list([0])
        l2 = build_linked_list([0])
        result = self.solution.add_two_numbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [0])

    def test_example3(self):
        l1 = build_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = build_linked_list([9, 9, 9, 9])
        result = self.solution.add_two_numbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [8, 9, 9, 9, 0, 0, 0, 1])

if __name__ == '__main__':
    unittest.main()
