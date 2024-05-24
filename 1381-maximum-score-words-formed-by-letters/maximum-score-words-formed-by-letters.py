class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        #include word and go next
        #we want score go till last and backtrack it
        #letter will be hashmap to check whether we have required letters or not
        #O(2^n * Word + Letter) --TC  
        def can_form_word(word,letter_cnt):
            word_cnt=Counter(word)
            for c in word_cnt:
                if word_cnt[c]>letter_cnt[c]:
                    return False
            return True
        def get_score(word):
            ans=0
            for c in word:
                ans+=score[ord(c)-ord('a')]
            return ans

        letter_cnt=Counter(letters)
        def backTrack(i):
            if i==len(words):
                return 0
            res=backTrack(i+1) #skip    
            if can_form_word(words[i],letter_cnt):
                #include
                #decrease letter_cnt
                for c in words[i]:
                    letter_cnt[c]-=1
                res=max(res,get_score(words[i])+backTrack(i+1))
                #backtracking increase letter_cnt
                for c in words[i]:
                    letter_cnt[c]+=1
            return res
        return backTrack(0)
        