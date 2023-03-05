class Solution:
    def all_combinations(self, elms):
        def back_tracking(elms, comb=[], i=0):
            if i > len(elms)-1:
                results.append(comb[:])
                return comb
            comb.append(elms[i])
            back_tracking(elms, comb, i + 1)
            comb.pop()
            back_tracking(elms, comb, i + 1)

        results = []
        back_tracking(elms)
        return results

    def k_combinations(self, elms, k):
        def back_tracking(elms, comb=[], i=0):
            if i > len(elms)-1:
                if len(comb) == k:
                    results.append(comb[:])
                return comb
            comb.append(elms[i])
            back_tracking(elms, comb, i + 1)
            comb.pop()
            back_tracking(elms, comb, i + 1)

        results = []
        back_tracking(elms)
        return results


list_temp = [i for i in range(3)]
list_temp = ["a", "b", "c"]
s = Solution()
res = s.all_combinations(list_temp)
print(res)
res2 = s.k_combinations(list_temp, 2)
print(res2)


