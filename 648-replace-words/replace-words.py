class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        #take each word in sentence and check with words in dictionary
        word_array=sentence.split()
        dict_set=set(dictionary)
        
        def shorted_root(word,dict_set):
            for i in range(len(word)):
                root=word[0:i]
                if root in dict_set:
                    return root
            return word
        for i in range(len(word_array)):
            word_array[i]=shorted_root(word_array[i],dict_set)
        return ' '.join(word_array)