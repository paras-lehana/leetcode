README: https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/4603987/lehanacodes-binary-slicing-partition-edge-validation-sliding-window-beats-97/


# Features

- All **$$#LehanaCodes$$** are with proper explanation of the intuition.
- In addition to text explanation, the code is also fully commented to assist coders in understanding each statement. 
- Set `DEBUG` to `True` and you can then visualize the logic as the code executes. 
- Any method (Binary Search Slicing and Partition Edge Validation) can be chosen by setting `METHOD` to `1` or `2`. 

> *Join me in my mission to teach coding in a way that goes beyond the basics, embracing the way to visualize how to code, exploring corner cases, and understanding each statement that is written. Please like and follow!*


![lehana_codes.jpg](https://assets.leetcode.com/users/images/33f36ff3-aae1-42cd-964e-841c1f8267c7_1703343149.8495882.jpeg)



# Intuition
This was a tough one to think of a solution! You already know that the Median is just the (average of) middle element(s) in case the list is in sorted order.

I suggest you to once go through the Editorial. It is claimed to be the biggest Editorial on LeetCode and gives you a fair idea of the approaches. I know that some coders might feel it misses explaning the main approaches in a intuitive way and that's why you are here.

**So yes, do go through the [Editorial](https://leetcode.com/problems/median-of-two-sorted-arrays/editorial/) once and with this Solution, you will have no further doubts!** :)

I knew that the Question is HARD and the expected complexity is $$O(log(m + n))$$. You see log and you already have a hint that some sort of binary search or divide-and-conquer solution needs to be built, right?

The simplest approach, in $$O(n+m)$$ obviously, would have been to traverse both "sorted" arrays together maintaning two pointers and just counting the elements traversed in "merged" sorted order. Once you reach the half of total elements (n + m), that is your median. If you want the code for this, I can give but I am avoiding to write this here because the question strictly does not ask for a linear complexity solution. It desperately needs a logarithmic solution!

I could not build much of a solution with the logarithmic approach but I could get an idea ***that we can, like in binary search, parition the array, compare the middle elements and then discard either part of the array continuing again with partitioning other part. I still had to look for the solution to conclude this***.

Since, the Editorial could not help me much with the idea behind the solution, ironically the "Intuition" it actually asks for, I had to spent more time on this. 

**So, this Solution comprises of what the Editorial got right, what it missed and what I researched. Gone through the Editorial once? So let's start!**

First, we will discuss the **Binary Slicing Method** that I hinted just above. Then, we will optimize it further to make the **Partition Edge Validation Method**. If you have better names for these methods, I need them badly!


# Approach


**Binary Slicing**

This approach is fairly described in the [Editorial](https://leetcode.com/problems/median-of-two-sorted-arrays/editorial/) Method #2. 

To summarize, think like this: Let's start with full arrays. Find the middle elements:

![image.png](https://assets.leetcode.com/users/images/e105c30a-1380-4f31-aee4-35bb26367e24_1705586170.191173.png)

The median of the merged array is at the half, right? So, if there are total 9 elements, the median should be the 5th element, or can we say the 5th smallest element? 

For generalizing, let median be the kth smallest element. And `k` can be calculated as

$$k = (len(A) + len(B))/2$$

Fair Enough. Now, look at the image above. If we are to take the total elements until `A_mid` and `B_mid`, and they (count of elements) are for some reason smaller than this `k`, that means we need more elements to cover until median.

Suppose, `A_mid < B_mid`. Do you think we even need to search for median in `A_left`? If even together elements until `A_mid` and `B_mid` could not make up the median elements, the median cannot be in A_left as all the elements here are smaller than `A_mid`! Unlike this, we can't safely disregard `B_left` as if we take more elements from `A_right`, even while keeping `B_left` same, we still have a possibility to reach the median. But if we disregard `B_left`, `A_left` cannot stay as all elements in it are smaller than `B_mid` since `B_mid > A_mid`. Similary, if `B_mid < A_mid`, you can ignore searching in B_left. 

Similarly, if total elements until `A_mid` and `B_mid` were greater than k, we know that we have to exclude elements and go towards left to find a smaller element. If `A_mid > B_mid`, you can skip searching in `A_right`, otherwise you can skip `B_right`. 

Whatever parition you skip above, will logarithmically decrease your search space. In some time, either of the partition will go empty. Also note that you might have removed some elements from the left of the other partition. If you have removed 3 elements and your `k=5`, you now have to search for the 2nd smallest element. Thus, you have to look for the `(k-A_start)`th smallest element. 

The solution had been perfect for odd number of total elements. For even number of elements, you need to find average of kth and (k-1)th smallest element. 

1. Let the sorted arrays be `nums1` and `nums2` with length `m` and `n` respectively. 

2. The idea is to find the kth smallest element of the merged list. If `k = (m+n)/2`, this is also the median for odd `(m+n)`. For even, we have to average this with (k+1)th shortest. 

    Let's start by letting `k = (m + n) // 2`. 

2. Initially, the partition for binary search will be full lists.

    Let `m_start = n_start = 0`
    and `m_end, n_end = m - 1, n - 1`.

3. In a binary-search fashion, keep dividing both the arrays until either of them cannot be broken further. At that time, median can be found from the other array. So the base cases are: 

    1. If nums1 partition is now empty, median is in the other array. Thus, if `m_start > m_end`, return `nums2[k - m_start]`.

    2. If nums2 partition is now empty, median is in the other array. Thus if `n_start > n_end`, return `nums1[k - n_start]`.

4. Otherwise, get the middle element of the current partitions. 

    `m_mid = (m_start + m_end) // 2`
    `n_mid = (n_start + n_end) // 2`

    `m_mid_value = nums1[m_mid]`
    `n_mid_value = nums2[n_mid]`

5. Let the combined index be `index_sum = m_mid + n_mid`.

6. If `index_sum < k`, we have to include more elements in either array i.e. left partition of the list having shorter middle element can be safely discarded:

    If `m_mid_value < n_mid_value`, make `m_start = m_mid + 1` to discard the the left half of `nums1`. 

    Else make `n_start = n_mid + 1` to discard the the left half of `nums2`. 

7. Else, we have to include more elements in either array i.e. right partition of the list having larger middle element can be safely discarded:

    If `m_mid_value < n_mid_value`, make `n_end = n_mid - 1` to discard the the right half of `nums2`.

    Else make `m_end = m_mid - 1` to discard the the right half of `nums1`.


8. Continue #4-7 until base case in #3 gets true. 

9. If total elements were even, do the same (#2-8) for `k+1` and average the result with the result for `k` and return this number. 



**Partition Edge Validation**

This approach is also mentioned in Approach #3 of the Editorial but I believe, it misses out explaining the idea behind it. As seen in comments, I was also finding difficulty in understanding the inituitive behind the approach and after researching on the best explaination for sometime, I would like to give credits to @[takeUforward](https://www.youtube.com/channel/UCJskGeByzRRSvmOyZOz61ig)'s YouTube [Video](https://www.youtube.com/watch?v=NTop3VTjmxk&t=1604s). I was never a fan of watching videos but this guy nailed the explanation. Let me now help you understand the whole idea with my language:

So, as we now know that the Median lies in middle of the merged array. It divides the array into two halves of equal size. 

Suppose you have nums1 and nums2 as:

    nums1 = [ 1, 3, 4, 7, 10, 12 ]

    nums2 = [ 2, 3, 6, 15 ]


Suppose an imaginary line that divides the merged array in such a way that the number of elements on the left half of the line are half of the total elements. We can do this in many ways like this, three of which are:

![image.png](https://assets.leetcode.com/users/images/c7e0bbe0-5449-4423-a328-7164c9eba77d_1705673472.018241.png)

Take the second example, we took `[ 1, 3, 4 ]` from `nums1` and `[ 2, 3 ]` from `nums2`:

    1 3 4  |  7 10 12 
      2 3  |  6 15

The resultant array (you don't have to make it) is `1 2 3 3 4 | 6 7 10 12 15`. Here, luckily, we have found the median = average of `[4,6]`. The median, if your division is correct, will always stay adjacent to the line. 

Do the same with example #3:

      1 3  |  4  7 10 12 
    2 3 6  |  15

This is not valid: `1 2 3 3 6 | 4 7 10 12 15`. 4 cannot come after 6, but we have to respect the line, right? So if you made the correct division, median will always be adjacent to the line. Why? Let's come to the theory.

> ***If I make all the possible combinations of combined array where number of elements in left half is equal to the half of the total elements, and if I find a valid sorted combination, the median will lie in the middle.***

Think about this for a second. If you have the correct sorted left merged half, median will always be the last element, no? Yes, because we are making sure of two things:

1. The left half including elements from both the arrays should contain just half number of total elements.

2. The combination taken should be a sorted. 

Now, you may ask, how do we make sure the combination is sorted. You don't have the check the full merged array. The left half from nums1 is already sorted just like left half from nums2. Similary, the both right halves are already sorted since we took them from sorted arrays. Let us name left and right halves of `nums1` as `A_left` and `A_right` and left and right halves of `nums2` as `B_left` and `B_right`.

![image.png](https://assets.leetcode.com/users/images/e0c47f24-b259-42d3-8a51-16496d29a2ab_1705674619.2553296.png)


1. Every element in `A_left` is sorted because we took them from sorted `nums1`.

2. Every element in `B_left` is sorted because we took them from sorted `nums2`.

3. Every element in `A_right` is sorted because we took them from sorted `nums1`.

4. Every element in `B_right` is sorted because we took them from sorted `nums2`.

5. Every element in `A_left` is smaller than every element in `A_right` because they are part of sorted `nums1`.  

6. Every element in `B_left` is smaller than every element in `B_right` because they are part of sorted `nums2`.  

7. If every element in `A_left` is smaller than every element in `B_right` and every element in `B_left` is smaller than every element in `A_right`, this combination is valid since the merged array can be written in sorted order while respecting the line. Remember this point, point #7.

    ![image.png](https://assets.leetcode.com/users/images/5ce622f5-c0dd-4ee9-b5ab-0089ea3da0eb_1705674959.7454255.png)


8. If #7 is true for a combination, since we have exactly half number of elements here, the median is maximum element in the left half. This is because when you make the merged array in #7, the maximum array will be the most adjacent left of the line. Since #1 and #2 are true, you don't need to check all the elements for the maximum, just the rightmost element of both left arrays, here 4 and 3. When you combine the arrays, 4 will stay ahead of 3. 

9. #8 was true for odd number of total elements. For even, consider to also take the minimum of the right half arrays. Again since #3 and #4 are true, you just need to compare the left most element in both right arrays. Here, 6 will be before 7 if arrays are merged and just adjacent right to the line. Your median is the average of `left_max` calculated in #8 and `right_min` calculated here.  

10. If you think about #8 or even #9, you are only comparing the edge elements of the partition you made. We will use this concept in our binary-search algorithm.

Before we proceed to the algorithm, let's understand how will a non-binary-search algorithm work here. 

So, our objective is to actually form all possible combinations of partitions where the total elements in `A_left` and `B_left` is half the total elements in the merged array. Once we find such a combination where the edge elements are in sorted order, we have found the median.

Suppose you have nums1 and nums2 as:

    nums1 = [ 1, 3, 4, 7, 10, 12 ]

    nums2 = [ 2, 3, 6, 15 ]

If we take `[ 1 3 4 7 ]` from `nums1` (4 elements) for the left side, we can only take 1 element from `nums2` for the left side since total elements must be 5 (half of total 10) for the left side.

> Remember, for any array, you can't just take any element from anywhere. The left partition must start from the beginning since in the merged array all the elements wil be in order.


Suppose at sometime, we make a parition like this:

![image.png](https://assets.leetcode.com/users/images/c0402ded-4d18-40ca-90e2-cc59e5ec6c76_1705844363.3851635.png)

Since, 7 > 3, this is not a valid partition. Think! We have took more elements from `nums1`. We can try taking 3 elements from nums1 now: `[ 1 3 4 ]` and 2 elements from `nums2`: `[ 2 3 ]`. We are essentially moving left in nums1 - we can't move right as 7 is already greater than 3 and any element on the right will always be greater than 3 (since they are sorted). Also, if you move left in nums1, you will also have to move right in nums2 (to include more elements so that total elements stay same).


![image.png](https://assets.leetcode.com/users/images/1f7ff014-02dc-494d-8005-f04e29ebf34e_1705845117.987441.png)


Suprisingly, all the condition hold! Since total elements are odd, the median is `min(4,3) = 3`. 

Sometime, during the algorithm you may reach the extreme end (before 1 or after 12) and to handle corner cases, just assume that -INF and INF stay at those ends (we will talk about this in the algorithm). 

If you understand the algorithm by now, binary-search just optimizes the search. Instead of just traversing elements in order, we just move the line to middle of partitions every time. For example, here instead of going to 4 from 7, we would put the line in the middle - maybe between 3 and 4: 


      1 3  |  4  7 10 12 
    2 3 6  |  15

This will speed up search by logarithmic time. Let's now build the alogirthm! Also, to optimize further, why don't we just traverse this algorithm on shorter list. It will work as any list will anyways cover all the combinations. 

> Crux: For the shorter list, in a binary search fashion select a partition. Take such a partition from the longer array so the total elements taken from both arrays are half of total elements in merged array i.e. the edge elements of both the arrays are median contendants. Now, if the edge elements are in sorted order i.e. left1 < right2 and left2 < right1, median can be found using these edge elements. 

 
1. Let `m = len(nums1)`; `n = len(nums2)`. If m > n, run for smaller list to save time, let `nums1` the smaller array in all cases.

2. In case `nums1` is empty, median is the median of `nums2`. In case `nums2` is empty, median is the median of `nums1`. Otherwise, continue to #3. 

3. In a binary-search fashion, find the partition of smaller array whose edge element validates the median condition. Start with full array i.e. `m_start = 0`; `m_end = m - 1`.

4. Get the middle index (`m_mid`) of the nums1 window and decide further if we want to go left or right before checking the middle element of the current window again. Our potential median will be at this index once we find it. Get the middle index of nums2 window where the window is such that both (left) window has half the total elements in merged array. 

5. Get the left edge elements. To handle corner cases, this should be -INF if binary search makes it go less than 0 (this can happen in case every element in nums1 partition is too big to be the median).

        m_left = nums1[m_mid] if m_mid >= 0 else float("-inf")
        n_left = nums2[n_mid] if n_mid >= 0 else float("-inf")

6. Get the right edge elements. Just after the partitions should lie the element which is greater than both left elements. We will check this in a while. Handle corner case with +INF if every element in the partition is too small to be the median

        m_right = nums1[m_mid + 1] if m_mid < m - 1 else float("inf") 
        n_right = nums2[n_mid + 1] if n_mid < n - 1 else float("inf")


7. If left elements are the median, they should be smaller than both right elements. Otherwise, continue to #8:

        m_left <= n_right and n_left <= m_right

8. If `nums1` left element is greater than nums2 right, the median is on further left side:
    
        if m_left > n_right: m_end = m_mid - 1


9. Else, go right:

        m_start = m_mid + 1


10. Repeat #4-9 until Median is found in #7.


---



# Complexity

**Time complexity:**

1. Binary Slicing: $$O(n)$$ `108 ms`
2. Edge Validation: $$O(n)$$ `72 ms` ***Beats 97%***


**Space complexity:**

1. Binary Slicing: $$O(n)$$ `17.7 MB`
2. Edge Validation: $$O(n)$$ `16.98 MB`

**Note:** *In Edge Validation, you can save function overhead to run for smaller array by ([Full Code to beat 97%](https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/1152658927/?submissionId=1148761280)):*

```python
if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
```

# Code
```


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        """

        Choose the METHOD you want to execute:

        (1) Binary Search Slicing: In a binary search fashion, select a parition initially divided by the middle element for each array. Compare the middle elements for the both arrays, and discard a partition from either array depending on 
 included elements (less than half?) and minimum/maximum of the middle elements. 

        (2) Partition Edge Validation: For the shorter list, in a binary search fashion select a partition. Take such a partition from the longer array so the total elements taken from both arrays are half of total elements in merged array i.e. the edge elements of both the arrays are median contendants. Now, if the edge elements are in sorted order i.e. left1 < right2 and left2 < right1, median can be found using these edge elements. 

        """
        METHOD = 2

        # If set to True, prints information to stdout during execution to help debug and visualize
        DEBUG = True

        """
        Calculates the median of two sorted list when merged in sorted order. Uses binary search in shorter list.
        
        - Time Complexity: O(min(m,n)) where m = len(nums1), n = len(nums2)
        - Space Complexity: O(1); the function does not create a new list

        @param nums1: List #1 in sorted order
        @param nums2: List #2 in sorted order
        @return: Median of the sorted merged list of nums1 and nums2, -1 otherwise
        """
        def byPartitionEdgeValidation(
            nums1: List[int], nums2: List[int]
        ) -> float:

            m, n = len(nums1), len(nums2)

            # Run for smaller list to save time, let nums1 the smaller array in all cases
            if m > n:
                return byPartitionEdgeValidation(nums2, nums1)

            is_merged_odd = (m + n) % 2 != 0 

            # In case nums1 is empty, median is the median of other array
            if m == 0:
                return (
                    nums2[n // 2]
                    if is_merged_odd
                    else (nums2[n // 2 - 1] + nums2[n // 2]) / 2
                )

            # Since m + n > 0, both arrays cant be empty
            # In case nums2 is empty, median is the median of other array
            elif n == 0:
                return (
                    nums1[m // 2]
                    if is_merged_odd
                    else (nums1[m // 2 - 1] + nums1[m // 2]) / 2
                )

            # Partition start and end index of nums1
            m_start, m_end = 0, m - 1        # Binary search will starts from middle
            # In a binary-search fashion, find the partition of smaller array whose edge element validates the median condition
            while True:
                print(f"\n{nums1=}\t|\t{nums2=}\n\n") if DEBUG else None

                # Binary Search basics: check the middle element of the window and decide further if we want to go left or right before checking the middle element of the current window again. Our potential median will be at this index once we find it.
                m_mid = (m_start + m_end) // 2        

                # Since our potential median is at m_mid, we have already taken m_mid elements from nums1. Total elements in both partition is, say (m+n)/2. Thus, the index is one less than this. To handle cases where m+n is even, we have to take (m+n-1)/2 elements in total. However, this modification works for odd cases too. Now, nums2 partition can only contain (m+n-1)/2 - m_mid elements, thus, the index will be one less than this. 
                n_mid = (m + n - 1) // 2 - m_mid - 1

                print(
                    f"\nm_mid = ( m_start + m_end ) // 2 = ( {m_start} + {m_end} ) // 2 = {m_mid}"
                ) if DEBUG else None

                print(
                    f"\nn_mid = (m + n)//2 - m_mid - 1 = ({m} + {n})//2 - {m_mid} - 1 = {n_mid}\n"
                ) if DEBUG else None

                # As decided, the median lies at the extreme edge of either partition. To handle corner cases, this should be -INF if binary search makes it go less than 0 (this can happen in case every element in nums1 partition is too big to be the median).
                m_left = nums1[m_mid] if m_mid >= 0 else float("-inf")
                n_left = nums2[n_mid] if n_mid >= 0 else float("-inf")

                # Just after the partitions should lie the element which is greater than both left elements. We will check this in a while. Handle corner case with +INF if every element in the partition is too small to be the median
                m_right = nums1[m_mid + 1] if m_mid < m - 1 else float("inf") 
                n_right = nums2[n_mid + 1] if n_mid < n - 1 else float("inf")

                print(
                    f"\nComparing {m_left} <= {n_right} and {n_left} <= {m_right}\n"
                ) if DEBUG else None

                # If left elements are the median, they should be smaller than both right elements. We dont need to check m_left <= m_right because nums1 is already sorted and smae goes for nums2. But if the cross elements also satisfy the condition, this can be only possible if either m_left of n_left is the median since we have already made sure that both partition sum up to half the total elements.
                if m_left <= n_right and n_left <= m_right:

                    # In case of odd, the maximum of the left elements is the median as it will be the element in the extreme half when both arrays are merged. In case of even, we, like generally, take the minimum of right elements (since it will the immediate right of the median) to calculate average. 
                    return (
                        max(m_left, n_left)
                        if is_merged_odd
                        else (max(m_left, n_left) + min(m_right, n_right)) / 2
                    )

                # If nums1 left element is greater than nums2 right, the median is on further left side - we are giving chance to let m_left decrease further. n_right will increase since the nums1 partition is itself decreased with this and this will cause the nums2 partition to increase to validate total number of elements. 
                if m_left > n_right:
                    m_end = m_mid - 1

                # Vice versa we only have the option to go right with nums1 such that m_left will increase and n_right will decrease
                else:
                    m_start = m_mid + 1

                # This loop repeats until the valid median is found

            # Since we have a infinite True while loop with conditional return, this return statement should not run anytime but it is here just to be safe in unknown cases and also to have the required <int> return type by default  
            return -1

        """
        Calculates the kth smallest element if nums1 and nums2 are merged using binary search.
        
        - Time Complexity: O(m + n) where m = len(nums1), n = len(nums2)
        - Space Complexity: O(1); the function does not create a new list

        @param nums1: List #1 in sorted order
        @param nums2: List #2 in sorted order
        @return: kth smallest element
        """
        def findKthSmallestElement(
            nums1: List[int], m: int, nums2: List[int], n: int, k: int
        ) -> float:

            # Initially, the partition for binary search will be full lists
            m_start = n_start = 0
            m_end, n_end = m - 1, n - 1

            # In a binary-search fashion, keep dividing both the arrays until either of them cannot be broken further. At that time, median can be found from the other array. 
            while True:

                # If nums1 partition is now empty, median is in the other array
                if m_start > m_end:

                    print(
                        f"\n{m_start=} > {m_end=}\t|\tReturning nums2[{k} - {m_start}] = nums2[{k - m_start}] = {nums2[k - m_start]}\n"
                    ) if DEBUG else None

                    # Since we have already removed m_start elements from nums1 partition which were smaller than k, we just need to find (k - m_start)th smallest element in nums2 partition
                    return nums2[k - m_start]
                    break

                # If nums2 partition is now empty, median is in the other array
                elif n_start > n_end:
                    
                    print(
                        f"\n{n_start=} > {n_end=}\t|\tReturning nums1[{k} - {n_start}] = nums1[{k - n_start}] = {nums1[k - n_start]}\n"
                    ) if DEBUG else None

                    # Since we have already removed n_start elements from nums2 partition which were smaller than k, we just need to find (k - n_start)th smallest element in nums1 partition
                    return nums1[k - n_start]
                    break

                # Get the middle element of the current partitions
                m_mid, n_mid = (m_start + m_end) // 2, (n_start + n_end) // 2
                m_mid_value, n_mid_value = nums1[m_mid], nums2[n_mid]

                index_sum = m_mid + n_mid   # Referred as combined index 

                print(
                    f"\nIteration:\n\n{nums1=} -> {nums1[m_start:m_end+1]}\t|\t{m_start=}\t|\t{m_end=}\t|\t{m_mid=}\t|\t{m_mid_value=}\n"
                ) if DEBUG else None
                print(
                    f"{nums2=} -> {nums2[n_start:n_end+1]}\t|\t{n_start=}\t|\t{n_end=}\t|\t{n_mid=}\t|\t{n_mid_value=}\n\n{index_sum=}\t|\t{k=}\n"
                ) if DEBUG else None

                # If combined index is less than k, we have to include more elements in either array
                if index_sum < k:

                    # Left partition of the list having shorter middle element can be safely discarded
                    if m_mid_value < n_mid_value:
                        m_start = m_mid + 1
                    else:
                        n_start = n_mid + 1

                # Else the combined index is not less than k and we have to remove elements from either list
                else:
                    # Right partition of the list having larger middle element can be safely discarded
                    if m_mid_value < n_mid_value:
                        n_end = n_mid - 1
                    else:
                        m_end = m_end - 1

                # This loop repeats until the either partition gets empty

        """
        Calculates the median of num1 and num2 when merged in sorted order. Uses binary search in both lists. 
        
        - Time Complexity: O(m + n) where m = len(nums1), n = len(nums2)
        - Space Complexity: O(1); the function does not create a new list

        @param nums1: List #1 in sorted order
        @param nums2: List #2 in sorted order
        @return: Median of the sorted merged list of nums1 and nums2
        """
        def byBinarySearchSlicing(nums1: List[int], nums2: List[int]) -> float:

            m, n = len(nums1), len(nums2)

            # The idea is to find the kth smallest element of the merged list. If k = (m+n)/2, this is also the median for odd (m+n). For even, we have to average this with (k+1)th shortest. 
            k = (m + n) // 2

            print(
                f"\nStatus before Looping: {m=}\t|\t{n=}\t|\t{k=}\n\n"
            ) if DEBUG else None

            # If total elements in merged array is odd, the kth smallest is also the median.
            if (m + n) % 2 != 0:
                return findKthSmallestElement(nums1, m, nums2, n, k)

            # If total elements are even, average of kth smallest and (k+1)th smallest is the meidan.
            else:
                return (
                    findKthSmallestElement(nums1, m, nums2, n, k - 1)
                    + findKthSmallestElement(nums1, m, nums2, n, k)
                ) / 2

        # Method (1) Binary Search Slicing
        if METHOD == 1:
            print(
                f"\nMethod (1) Binary Search Slicing CHOSEN\n\n"
            ) if DEBUG else None

            return byBinarySearchSlicing(nums1, nums2)

        # Method (2) Partition Edge Validation
        elif METHOD == 2:
            print(
                f"\nMethod (2) Partition Edge Validation CHOSEN\n\n"
            ) if DEBUG else None

            return byPartitionEdgeValidation(nums1, nums2)

        else:
            print("\nERROR: Please choose an appropriate METHOD!\n")
            return -1

```