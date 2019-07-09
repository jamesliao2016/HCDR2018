class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        import collections
        queue = collections.deque([[beginWord,1]])
        wordList = set(wordList)
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:i] + c + word[i+1:]
                    if tmp in wordList:
                        wordList.remove(tmp)
                        queue.append([tmp,dist+1])
        return 0

if __name__ == '__main__':
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().ladderLength( beginWord, endWord, wordList))
    '''
    Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

# 9 july, 2019

        import collections
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0

    '''
