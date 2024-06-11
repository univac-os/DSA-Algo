class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #hashmap of arr1 and check arr2 and give result O(n+nlogn)
        arr2_set=set(arr2)
        arr1_count=defaultdict(int)
        end_arr=[]
        for n in arr1:
            if n not in arr2_set:#this is O(1) operation because of set if array is use then O(n)
                end_arr.append(n)
            arr1_count[n]+=1
        end_arr.sort()
        res=[]
        for n in arr2:
            res.extend([n] * arr1_count[n])

        res.extend(end_arr)

        return res

        
