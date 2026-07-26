# 比较版本号
# 给你两个 版本号字符串 version1 和 version2 ，请你比较它们。版本号由被点 '.' 分开的修订号组成。修订号的值 是它 转换为整数 并忽略前导零。


def compareVersion(version1: str, version2: str) -> int:
    nums1 = version1.split(".")
    nums2 = version2.split(".")
    n = max(len(nums1), len(nums2))
    for i in range(n):
        a = int(nums1[i]) if i < len(nums1) else 0
        b = int(nums2[i]) if i < len(nums2) else 0
        if a > b:
            return 1
        elif a < b:
            return -1
    return 0

version1 = "1.2"
version2 = "1.10"
print(compareVersion(version1, version2))

version3 = "1.0"
version4 = "1.0.0.0"
print(compareVersion(version3, version4))