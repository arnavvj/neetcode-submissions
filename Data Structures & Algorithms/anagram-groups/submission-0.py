class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = {}

        for word in strs:

            key_c_list = [c for c in word]
            key_c_list.sort(key = lambda x: x)

            print(key_c_list)
            
            key_word = ""
            for kc in key_c_list:
                key_word += kc
            print(key_word)

            try:
                ans[key_word].append(word)

            except KeyError:
                ans[key_word] = [word]

        return [vals for vals in ans.values()]