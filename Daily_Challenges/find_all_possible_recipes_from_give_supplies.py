from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recips_has_result = {}
        for ingd in ingredients:
            ingd_length = len(ingd)
            counter = 0
            if isinstance(ingd, str):
                if ingd in supplies:
                    counter += 1
                elif ingd in recips_has_result and recips_has_result[ingd]:
                    counter += 1
                elif ingd in recipes and ingd in supplies:
                    counter += 1

            for inner_ingd in ingd:
                if inner_ingd in supplies:
                    counter += 1
                elif inner_ingd in recips_has_result and recips_has_result[inner_ingd]:
                    counter += 1
                elif inner_ingd in recipes and inner_ingd in supplies:
                    counter += 1
                else:
                    continue

            if ingd_length == counter:
                ingd_index_number = ingredients.index(ingd)
                recipe_item = recipes[ingd_index_number]
                recips_has_result[recipe_item] = True

        return list(recips_has_result.keys())


res = Solution()
print(res.findAllRecipes(["ju","fzjnm","x","e","zpmcz","h","q"], [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]], ["f","hveml","cpivl","d"]))
