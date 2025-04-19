class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        we have unlimited supplies,so we want reciepes from having ingredients
        looks like graph ex: if i can make break and have meat i can make sandwich so no need to check so use hashmap to store whether we can make the bread or not
        instead of string to be graph node we will use index 
        """
        can_cook={s:True for s in supplies}
        recipes_idx={ r:i for i,r in enumerate(recipes) }
        def dfs(r):
            if r in can_cook:
                return can_cook[r]
            if r not in recipes_idx:
                return False
            can_cook[r]=False 
            for nei in ingredients[recipes_idx[r]]:
                if not dfs(nei):
                    return False
            can_cook[r]=True
            return can_cook[r]

        return [r for r in recipes if dfs(r)]# if recipes can done then we can add to final list