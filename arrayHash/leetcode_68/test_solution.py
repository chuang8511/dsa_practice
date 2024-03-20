import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_fullJustify(self):
        solution = Solution()

        result = solution.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16)
        self.assertEqual(result, [
   "This    is    an",
   "example  of text",
   "justification.  "
]
)

        result = solution.fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16)
        self.assertEqual(result, [
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
])

        result = solution.fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20)
        self.assertEqual(result, [
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
])