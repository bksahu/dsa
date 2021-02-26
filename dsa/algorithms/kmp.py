"""
KMP Algorithm for Pattern Matching

Given a text text[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) 
that prints all occurrences of pat[] in txt[]. You may assume that n > m.

Examples:
Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12
"""

class KMP:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern

    def matchPattern(self):
        n = len(self.text)
        m = len(self.pattern)
        lps = [0]*m
        indexes = []
        self._computerLPSArray(lps, m)
        
        j = 0 # index of pattern 
        i = 0 # index of text
        while i < n:
            if self.pattern[j] == self.text[i]: # if curr char is equal increment
                i += 1
                j += 1

            # if the pattern pointer reaches end of pattern
            # add it to indexes as we have found a match and
            # go to the starting of the suffix
            if j == m: 
                indexes.append(i-j)
                j = lps[j-1]
            
            # char did not matched
            elif i < n and self.pattern[j] != self.text[i]:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyways
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
                

        return indexes

    def _computerLPSArray(self, lps, m):
        len = 0 # length of previous longest prefix suffix
        i = 1 # staring index of pattern, since lps[0] = 0, we start from 1
        while i < m:
            if self.pattern[i] == self.pattern[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                # Do not match lps[0..lps[j-1]] characters,
                if len != 0:
                    len = lps[len-1]
                else:
                    lps[i] = 0
                    i += 1


if __name__ == "__main__":
    kmp = KMP("THIS IS A TEST TEXT", "TEST")
    print(kmp.matchPattern())
    kmp = KMP("AABAACAADAABAABA", "AABA")
    print(kmp.matchPattern())