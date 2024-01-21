README: https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/4603987/lehanacodes-binary-slicing-partition-edge-validation-sliding-window-beats-97/

class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        """

        Choose the METHOD you want to execute:

        (1) Binary Search Slicing: In a binary search fashion, select a parition initially divided by the middle element for each array. Compare the middle elements for the both arrays, and discard a partition from either array depending on total included elements (less than half?) and minimum/maximum of the middle elements. 

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

                # Else the combined index is not less than k and we have to remove elements from either element
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
