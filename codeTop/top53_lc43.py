# 字符串相乘
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 输入: num1 = "123", num2 = "456",输出: "56088"

def muliply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    n1 = len(num1)
    n2 = len(num2)
    result = [0] * (n1 + n2)
    for i in range(n1 - 1, -1, -1):
        for j in range(n2 - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            sum_ = mul + result[i+j+1]
            result[i+j+1] = sum_ % 10
            result[i+j] += sum_ // 10
    result = list(map(str, result))
    return ''.join(result).lstrip('0')

print(muliply("123", "456"))