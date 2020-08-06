'''
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

Example 1:
Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.

Example 2:
Input: str1="xy#z", str2="xyz#"
Output: false
Explanation: After applying backspaces the strings become "xz" and "xy" respectively.

Example 3:
Input: str1="xp#", str2="xyz##"
Output: true
Explanation: After applying backspaces the strings become "x" and "x" respectively.
In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.

Example 4:
Input: str1="xywrrmp", str2="xywrrmu#p"
Output: true
Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
'''


def solution1(str1, str2):
    def clean(s):
        stack, cleaned = [], ""
        i = len(s)-1
        while i >= 0:
            ch = s[i]
            if ch == "#":
                stack.append("#")
                i -= 1    
            elif stack:
                if stack:
                    stack.pop()
                    i -= 1
            else:
                cleaned = s[i] + cleaned       
                i -= 1    
        return cleaned
    return clean(str1) == clean(str2)

def solution2(str1, str2):
    def clean(s):
        # start iterating from begining
        # if ch in not backspace append 
        # it to the stack. If it is a 
        # backspace and stack is not empty
        # pop the recently added character
        stack = []
        for ch in s:
            if stack and ch == "#":
                stack.pop()
            elif ch != "#": # check if the first ch is not backspace, which makes no sense
                stack.append(ch)
        return "".join(stack)
    return clean(str1) == clean(str2)

def solution(str1, str2):
    ptr1 = len(str1)-1
    ptr2 = len(str2)-1

    while ptr1 >= 0 or ptr2 >= 0:
        ptr1 = get_next_index(str1, ptr1)
        ptr2 = get_next_index(str2, ptr2)

        if ptr1 < 0 and ptr2 < 0:
            return True
        if ptr1 < 0 or ptr2 < 0:
            return False
        if str1[ptr1] != str2[ptr2]:
            return False
        
        ptr1 -= 1
        ptr2 -= 1
    return True

def get_next_index(s, i):
    backspace = 0
    while i >= 0:
        if s[i] == "#":
            backspace += 1
        elif backspace > 0:
            backspace -= 1
        else:
            break
        i -= 1
    return i - backspace
        

if __name__ == "__main__":
    print(solution(str1="xy#z", str2="xzz#"))
    print(solution(str1="xy#z", str2="xyz#"))
    print(solution(str1="xp#", str2="xyz##"))
    print(solution(str1="xywrrmp", str2="xywrrmu#p"))