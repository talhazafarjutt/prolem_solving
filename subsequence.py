def strStr(haystack: str, needle: str) -> int:
    end=len(needle)
    for i,v in enumerate(haystack):
        if needle==haystack[i:end]:
            return i
        else:
            end+=1
    return -1





print(strStr('leetcode','leeto'))