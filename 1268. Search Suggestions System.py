class Solution:
    # solution by @suyogk23 GITHUB
    # sort products and check for matching prefix of searchWord upto 3 words in products by a linear scan
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        i, n, m = 1, len(searchWord)+1, len(products)
        suggestions = []
        while (i<n):
            suggestion = []
            j = 0
            while len(suggestion) < 3 and j < m:
                if searchWord[:i] == products[j][:i]:
                    suggestion.append(products[j])
                j += 1
            i+=1
            suggestions.append(suggestion)
        return suggestions
