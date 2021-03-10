# To Find the count of prime numbers under n. Complexity of sieve of erathosthenis is o(nloglogn)


class Solution:
    def countPrimes(self, n: int) -> int:
#         Solving using normal method . When there is space constraint
#         if (n in [0, 1, 2]):
#             return 0
        
#         count = 1
#         for i in range(3, n):
#             prime = True
#             for j in range (2, math.ceil(math.sqrt(i)) + 1):
#                 if(i % j) == 0 and i !=j:
#                     prime = False
#                     break
#             if prime:
#                 count +=1
                    
#         return count


        # When there is no space constraint. Using the methos seive of erathosthenis
        #Initial cases
        if (n in [0, 1, 2]):
            return 0
        
        ans = [0] * n
        for i in range(2, n):
            j = i + i
            while(j < n):
                ans[j] = 1
                j = j+i
        count = 0
        for i in range(2, n):
            if ans[i] == 0:
                count +=1
        return count
