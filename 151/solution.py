# 151. Reverse Words in a String

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters.
# The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words. Do not include any extra spaces.


class Solution:
    def reverseWords(self, s: str) -> str:
        # words = s.strip().split()
        # words = [element for element in words if element != ""][::-1]
        # myString = ""
        # for word in words:
        #     myString += word
        #     if words[-1] != word:
        #         myString += " "
        # return myString

        # This ^ actually fails testcase04... not sure how/why
        # but what should be "s TVi" about 4 lines in becomes "sTVi"
        # and that's this code's only mistake. It's weird.
        # But the code below works fine.

        s = s.split()
        s = s[::-1]
        return " ".join(s)
