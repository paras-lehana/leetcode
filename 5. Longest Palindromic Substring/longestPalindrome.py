# rebuild from mind logic, also take care of case2 (cbbd) 

class Solution:
    def longestPalindrome(self, s: str) -> str:

        DEBUG = True

        slen = len(s)
        max_len = 0
        max_p = ""
        
        
        for i in range(slen):

            plen = 0
            h1 = ""
            h2 = "" 
            offset = 0

            print(f"\n{s=} | {i=} \n") if DEBUG else None

            for j in range(slen - 1, i - 1, -1):

                print(f"\n{s=} | {i=} | {j=} | {offset=} | {h1=} | {h2=} | {plen=}\n") if DEBUG else None 

                if s[i + offset] == s[j]:

                    print(f"\nCHAR MATCH! s[{i+offset}] == s[{j}] => {s[i+offset]} = {s[j]} | \n") if DEBUG else None 

                    h2 = s[j] + h2

                    plen = offset + len(h2)
                    
                    if i + offset >= j:
                        break
                    
                    h1 = h1 + s[i + offset]
                    offset = offset + 1

                else:
                    offset = 0
                    h1 = h2 = ""

                if i + offset >= j:
                    break


            if plen > max_len:
                
                max_len = plen
                max_p = h1 + h2

                print(f"\nUPDATE! {max_len=} | {max_p=}\n") if DEBUG else None

        return max_p
            

                





        