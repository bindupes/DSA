'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def backtrack(curr, open_count, close_count):
            # If current string is complete
            if len(curr) == 2 * n:
                res.append(curr)
                return

            # Add '(' if we still can
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            # Add ')' if it won't break validity
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res
