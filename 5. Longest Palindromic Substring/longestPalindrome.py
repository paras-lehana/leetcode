# for bacabab, decide the right way as j is not 4 but 3 for u, can we have a infinite loop with j handling instead of range tuple

class Solution:
    def longestPalindrome(self, s: str) -> str:

        DEBUG = True

        slen = len(s)
        max_p = ""
        
        for i in range(slen):

            h1 = ""
            h2 = "" 
            offset = 0

            print(f"\n{s=} | {i=} \n") if DEBUG else None

            for j in range(slen - 1, i - 1, -1):

                print(f"\n{s=} | {i=} | {j=} | {offset=} | {h1=} | {h2=} | Comparing {s[i+offset]} <-> {s[j]}\n") if DEBUG else None 

                if s[i + offset] == s[j]:

                    print(f"\nCHAR MATCH! s[{i+offset}] == s[{j}] => {s[i+offset]} = {s[j]} | \n") if DEBUG else None 
                    

                    h1 = h1 + s[i + offset]

                    if i + offset == j:
                        break

                    h2 = s[j] + h2  
                    
                    offset = offset + 1

                    if i + offset == j:
                        break
                    

                else:
                    if offset != 0:
                        print("yay")
                        j = j + 1
                        print(j)
                    offset = 0
                    h1 = h2 = ""
 
            if len(h1 + h2) > len(max_p):
                max_p = h1 + h2

                print(f"\nUPDATE! {max_p=}\n") if DEBUG else None

        return max_p
            

                





        
