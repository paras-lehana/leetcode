# Features

- All #LehanaCodes are with proper explanation of the intuition.
- In addition to text explanation, the code is also fully commented to assist coders in understanding each statement. 
- Set `DEBUG` to `True` and you can then visualize the logic as the code executes. 
- Any method (Two-Pointer and Three-Pointer) can be chosen by setting `METHOD` to `1` or `2`. 

> *Join me in my mission to teach coding in a way that goes beyond the basics, embracing the way to visualize how to code, exploring corner cases, and understanding each statement that is written. Please like and follow!*


![lehana_codes.jpg](https://assets.leetcode.com/users/images/33f36ff3-aae1-42cd-964e-841c1f8267c7_1703343149.8495882.jpeg)


# Intuition
We know that the two arrays are sorted. One way is to start from beginning and compare which element goes next in nums1 (and shift) This can be greedy since we will covering all elements in order. This is **Two-pointer Method** (1 for both comparison and insertion, 1 for comparison only) *coded by me from scratch*. 

Another way is to start comparison from end and also start insertion from end so that shifting is not required. This is **Three-Pointer Method** (2 for comparison, 1 for insertion) *researched from the Solutions*. 

# Approach


**Two-Pointer Method:**

1. Maintain two pointers starting from beginning of `nums1` (`i`) and `nums2` (`j`) respectively.

2. Compare the elements at both the index.

3. If `nums1[i] <= nums2[j]`, increment `i` and continue.

4. Otherwise, we need to insert `nums2[j]` at position `i` by shifting  elements to the right.

5. Once we are done with `nums1` and if there are still elements left in `nums2`, we insert them in place of 0s.


---


**Three-Pointer Method:**

1. Maintain two pointers (used for **comparison**) starting from end of `nums1` (at m-1) valid elements (named `i`) and `nums2` (at n-1) (named `j`) respectively.

2. Maintain another pointer (used for **insertion**) starting from the end of `nums1` which includes 0 (at m+n-1)(named `k`).

3.  Compare the elements at `i` and `j` until `nums2` is covered.

4. If `nums1[i] <= nums2[j]`, insert `nums2[j]` at `k`, decrement `j` and `k` and continue.

5. If `nums1[i] > nums2[j]`, insert n`ums1[i]` at `k`, decrement `i` and `k`. 

# Complexity

**Time complexity:**

1. Two-Pointer: $$O(m+n)^2$$ `46 ms`
2. Three-Pointer: $$O(m+n)$$ `36 ms`

**Note:** *Three-Pointer Method does not require shifting of elements as in Two-Pointer Method and hence saves one $$O(m+n)$$.*

**Space complexity:**

1. Two-Pointer: $$O(m+n)$$ `16.6 MB`
2. Three-Pointer: $$O(m+n)$$ `16.4 MB`

 
# Code
```
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        

        """

        Choose the method you want to execute:

        (1) Two-Pointer: Maintain two pointers starting from beginning of nums1 (i) and nums2 (j) respectively. Compare the elements at both the index. If nums1[i] <= nums2[j], increment i and continue. Otherwise, we need to insert nums2[j] at position i by shifting  elements to the right. Once we are done with nums1 and if there are still elements left in nums2, we insert them in place of 0s.

        (2) Three-Pointer: Maintain two pointers (used for comparison) starting from end of nums1 (at m-1) valid elements (named i) and nums2 (at n-1) (named j) respectively. Maintain another pointer (used for insertion) starting from the end of nums1 which includes 0 (at m+n-1)(named k). Compare the elements at i and j until nums2 is covered. If nums1[i] <= nums2[j], insert nums2[j] at k, decrement j and k and continue. If nums1[i] > nums2[j], insert nums1[i] at k, decrement i and k. 

        """
        METHOD = 2

        # If set to True, prints information to stdout during execution to help debug and visualize
        DEBUG = False


        # METHOD (1) Two-Pointer Approach
        if METHOD is 1:
                
            # Start the two pointers from the beginning of both arrays
            i = j = 0

            """
            Compare elements at both positions till:

            - i < m + j: The total valid elements in nums1 are the initial ones in num1 (m)
                            and those inserted from num2 (j, not n). 

            - j < n: There could be cases where elements in nums2 are completed
                        or even when nums2 is blank (corner case). 

            """
            while (i < m + j and j < n):

                print(f"\n\nINSERTION:\n\n{nums1=}\n{nums2=}\n{i=}\n{j=}") if DEBUG else None

                # If nums1[i] is not larger, increment i and continue
                if nums1[i] <= nums2[j]:

                    i = i + 1
                    continue

                # Else, insert nums2[j] at position i and shifting all valid elements to right
                else:
                    
                    to_insert = nums2[j]        # Element to insert 
                    pos = i                     # Insertion position

                    # Shifting of element in buffer will be done till first invalid element (0) 
                    while (pos < m + j + 1):     

                        # Keep the current element in buffer, replace it with the the element to insert
                        # and make the buffer element the element to insert for next iteration
                        to_shift = nums1[pos]
                        nums1[pos] = to_insert
                        to_insert = to_shift
                        
                        pos = pos + 1

                    j = j + 1   # Increment j since current element of nums2 is processed
                    i = i + 1   # Increment i since current element is now shifted to right

            print(f"\n\nPOST INSERTION:\n\n{nums1=}\n{nums2=}\n{i=}\n{j=}") if DEBUG else None


            # If there are elements still left in nums2, insert them after valid elements of num1
            # as i is already past the valid elements now. 
            while (j < n):
                
                print(f"\n\nMERGING:\n\n{nums1=}\n{nums2=}\n{i=}\n{j=}") if DEBUG else None

                nums1[i] = nums2[j]
                i = i + 1
                j = j + 1

            print(f"\n\nPOST MERGE (FINAL):\n\n{nums1=}\n{nums2=}\n{i=}\n{j=}") if DEBUG else None




        # METHOD (2) Three-Pointer Approach
        elif METHOD is 2:
            
            

            # If nums2 is empty, return nums1 as it is
            if n == 0:
                return

            i = m - 1       # starts from end of valid nums1
            j = n - 1       # starts from end of nums2
            k = m + n - 1   # position to insert element


            print(f"\n\nINITIAL STATUS:\n\n{nums1=}\n{nums2=}\n{i=} | {nums1[i]=}\n{j=} | {nums2[j]=}\n{k=} | {nums1[k]=}") if DEBUG else None

            # Until nums2 is traversed fully (in reverse order), keep inserting in nums1
            while (j >= 0):
                
                # If nums2[j] >= nums1[i], it's the largest value not inserted yet. Insert it.
                # If nums1 had no valid elements or even traversed now, keep inserting nums2 elements. 
                if i < 0 or nums2[j] >= nums1[i]:

                    nums1[k] = nums2[j]
                    j = j - 1

                # If nums1[i] > nums2[j], we are shifting it to correct position.
                # The current value will be replaced in sometime. Reason: If we have consumed one 0 from nums1 which was reserved for nums2, last valid element of nums1 will be consumed by an extra nums2 element
                else:
                    
                    nums1[k] = nums1[i]
                    i = i - 1

                # We are inserting in reverse order and hence, work on the largest values above
                k = k - 1

                print(f"\n\nPOST INSERTION:\n\n{nums1=}\n{nums2=}\n{i=} | {nums1[i]=}\n{j=} | {nums2[j]=}\n{k=} | {nums1[k]=}") if DEBUG else None

            print(f"\n\nFINAL STATUS:\n\n{nums1=}\n{nums2=}\n{i=}\n{j=}\n{k=}") if DEBUG else None


        else:
            print("\nERROR: Please choose an appropriate METHOD!\n")
                          

```