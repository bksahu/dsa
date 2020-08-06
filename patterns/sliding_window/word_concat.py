"""
Words Concatenation (hard) #
Given a string and a list of words, find all the starting indices of substrings in 
the given string that are a concatenation of all the given words exactly once without 
any overlapping of words. It is given that all words are of the same length.

Example 1:

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".
Example 2:

Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
"""

def solution(str, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    word_count = len(words)
    word_length = len(words[0])
    res = []

    for i in range((len(str) - word_count * word_length) + 1):
        seen_word = {}
        for j in range(word_count):
            next_word_index = i + j*word_length
            curr_word = str[next_word_index: next_word_index+word_length]

            if curr_word not in word_frequency:
                break

            if curr_word not in seen_word:
                seen_word[curr_word] = 0
            seen_word[curr_word] += 1

            if seen_word[curr_word] > word_frequency.get(curr_word, 0):
                break

            if j+1 == word_count:
                res.append(i)
    return res


        

if __name__ == "__main__":
    print(solution("catfoxcat", ["cat", "fox"]))
    print(solution("catcatfoxfox", ["cat", "fox"]))