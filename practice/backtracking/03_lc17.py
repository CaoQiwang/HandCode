# 电话号码的字母组合
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

class Solution:
    def __init__(self):
        self.letter_map = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        self.result = []
        self.s = ""
    
    def back_tracking(self, digits, index):
        if index == len(digits):
            self.result.append(self.s)
            return
        digit = int(digits[index])
        letters = self.letter_map[digit]
        for i in range(len(letters)):
            self.s += letters[i]
            self.back_tracking(digits, index+1)
            self.s = self.s[0:-1]

    def letterCombinations(self, digits: str):
        self.back_tracking(digits, 0)
        return self.result
    
solution = Solution()
print(solution.letterCombinations("23"))