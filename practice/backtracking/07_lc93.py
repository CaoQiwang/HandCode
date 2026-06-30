# 复原IP地址
# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。


def restoreIpAddresses(s: str):
    result = []
    path = []

    def back_tracking(start_idx):
        if len(path) == 4 and start_idx == len(s):
            result.append(path[:])
            return
        if len(path) > 4:
            return
        for i in range(start_idx, min(len(s), start_idx + 3)):
            if not is_valid(s, start_idx, i):
                continue
            path.append(s[start_idx:i+1])
            back_tracking(i+1)
            path.pop()

    def is_valid(s, start, end):
        if s[start] == '0' and end != start:
            return False
        num = int(s[start:end+1])
        if num > 255:
            return False
        return True

    back_tracking(0)
    result = [".".join(s) for s in result]
    return result

print(restoreIpAddresses("25525511135"))