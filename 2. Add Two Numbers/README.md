# Features

- All #LehanaCodes are with proper explanation of the intuition.
- In addition to text explanation, the code is also fully commented to assist coders in understanding each statement. 
- Set `DEBUG` to `True` and you can then visualize the logic as the code executes. 
- Any method (Two-Pointer and Three-Pointer) can be chosen by setting `METHOD` to `1` or `2`. 


> *Join me in my mission to teach coding in a way that goes beyond the basics, embracing the way to visualize how to code, exploring corner cases, and understanding each statement that is written. Please like and follow!*


![lehana_codes.jpg](https://assets.leetcode.com/users/images/33f36ff3-aae1-42cd-964e-841c1f8267c7_1703343149.8495882.jpeg)


# Intuition
The nodes can represent a large number (upto 100 digits). Basic school addition can be done here - using digit sum and adjusting carry. The best part here is this addition is done from the rightmost digit and the linked-list also starts in reverse. This is the **Carry Method** and can handle very large numbers.  

I will still explain the **Decimal Conversion Method** where we simply convert the both linked list to decimal numbers, sum them and create linked-list from the resultant number. Please note that for this we will require support a very big integer (upto **101 digits**, 1 digit extra for carry). 

# Approach


**Carry Method:**

1. Basic school addition maths: for adding two numbers we sum the rightmost digit of both numbers.

2. If the sum is greater than 9, we carry 1.

3. We proceed to immediate left and sum the number including carry.

4. If the number of digits are unequal, we assume the shorter number to have digits 0.

5. Here, fortunately, the linked list is already starting from the right-most digit.

6. Traverse the linked list until both ends are and sum the digits adjusting the carry. 

7. Make a new node with the resultant digit sum.  


---


**Decimal Conversion Method:**

1. Convert both numbers to decimal representation.

2. Sum them using `+` operator.

3. Make a new linked-list from the generated number.


Be careful that the number could be very large (upto 100 digits) and thus, you will need a very long integer space. In python, there is no limit for a integer but in other programming languages, you might have to use a very long integer or might not have such a big integer. Also, beware that to remove the last digit from the number, this won't work:


```python []
list_sum = (int) (list_sum / 10)    # won't work for large integer
```

This will mess up with the precision of a large integer. Use the integer division provided by python:

 ```python []
list_sum = list_sum // 10     # integer-division, works!
```

# Complexity

**Time complexity:**

1. Carry: $$O(max(m,n))$$ `68 ms`
2. Decimal Conversion: $$O(max(m,n))$$ `71 ms`

**Note:** *Carry Method only needs to traverse both the linked-lists in one loop and generate the new linked-list during traversal while Decimal Method requires two traversals for each linked-list and then seperate generation of resultant linked-list.*

**Space complexity:**

1. Carry: $$O(max(m,n))$$ `16.4 MB`
2. Decimal Conversion: $$O(max(m,n))$$ `16.3 MB`

**Note 1:** *You might think that Decimal Method require more space due to a very large intege but storing all the nodes with individual values in integer is taking the major space here.*

**$$O(|n-m|)$$ Space Complexity:** With the carry method, as suggested by [@Amit_kumar_07](https://leetcode.com/Amit_kumar_07/) in this [solution](https://leetcode.com/problems/add-two-numbers/solutions/4422033/java-solution-t-c-o-n-s-c-o-1/), we can replace l1 node with the resultant digit and return the head of l1. Smart! 


# Code
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        """

        Choose the METHOD you want to execute:

        (1) Carry: Basic school maths. For adding two numbers we sum the rightmost digit of both numbers. If the sum is greater than 9, we carry 1. We proceed to immediate left and sum the number including carry. If the number of digits are unequal, we assume the shorter number to have digits 0. Here, fortunately, the linked list is already starting from the right-most digit. Traverse the linked list until both ends are and sum the digits adjusting the carry. 

        (2) Decimal Conversion: Convert both numbers to decimal representation. Sum them using + operator. Make linked list from the generated number. Be careful that the number could be very large (upto 100 digits) and thus, you will need a very long integer space. 

        """

        DEBUG = False
        METHOD = 1

        # Carry Method
        if METHOD == 1:
            
            l3 = ListNode()     # Linked List for the resultant number

            # Good practice to save the heads of Linked Lists before traversing
            l1_start = l1
            l2_start = l2
            l3_start = l3
            
            carry = 0           

            # Traverse until both ends are reached or carry is not adjusted. Note that one number could be larger (123 + 45) and even if ends are reached, carry is still to be adjusted (999 + 1).
            while l1 != None or l2 != None or carry != 0:

                # To keep the loop generalized, we start putting the digits from 2nd node and return the head as 2nd node. Otherwise, we would have an extra node when the loop ends.
                l3.next = ListNode()
                l3 = l3.next

                # The sum of digits is the sum of inidividual node digits if the node exists adjusting the carry
                # If either node does not exist, we naturally assume the digit to be 0. 
                node_sum = (l1.val if l1 != None else 0) + (l2.val if l2 != None else 0) + carry

                print(f"\n\nl3 Node:\n\nl1 = {l1.val if l1 != None else 0}\nl2 = {l2.val if l2 != None else 0}\n{carry=}\n{l3.val=}\n") if DEBUG else None

                # Carry is generated in case node_sum > 9
                if node_sum >= 10:

                    node_sum = node_sum - 10
                    carry = 1

                # Important as previous carry needs to nullified
                else: 
                    carry = 0
                
                l3.val = node_sum
                
                print(f"\n\nl3 Node:\n\n{l3.val=}\n") if DEBUG else None

                # Traverse to next node only if it exists.
                # If either node does not exist, we naturally assume the digit to be 0.  
                l1 = l1.next if l1 != None else None
                l2 = l2.next if l2 != None else None

            return l3_start.next    # Return the 2nd node as HEAD since 1st node is kept empty

        # Decimal Conversion Method
        elif METHOD == 2:

            l3 = ListNode()     # Linked List for the resultant number

            # Good practice to save the heads of Linked Lists before traversing
            l1_start = l1
            l2_start = l2
            l3_start = l3

            l1_sum = 0
            multiple = 1    # Multiple to make number from digits: 1, 10, 100 ...

            # Sum = digit1 + 10*digit2 + 100*digit3 ... starting from rightmost digit (or head of linked list) 
            while l1 != None:

                l1_sum = l1_sum + (multiple * l1.val)

                l1 = l1.next
                multiple = multiple * 10
            
            print(f"\n{l1_sum=}\n") if DEBUG else None

            l2_sum = 0
            multiple = 1    # Reset multiple

            # Similar sum for second number
            while l2 != None:

                l2_sum = l2_sum + (multiple * l2.val)

                l2 = l2.next
                multiple = multiple * 10

            print(f"\n{l2_sum=}\n") if DEBUG else None

            # Now basic sum can be done. 
            list_sum = l1_sum + l2_sum

            print(f"\n{list_sum=}\n") if DEBUG else None

            # Since there is atleast one node for each number, if the sum is 0, we need to output one node with value 0 instead of no node. 
            if list_sum == 0:
                
                l3.val = 0
                return l3

            # Generate linked list from the sum generated by making the node from rightmost digit and removing it from the number until no digits are remaining
            while list_sum != 0:

                # To keep the loop generalized, we start putting the digits from 2nd node and return the head as 2nd node. Otherwise, we would have an extra node when the loop ends.
                l3.next = ListNode()
                l3 = l3.next

                l3.val = list_sum % 10      # The value is just the right-most digit

                # Remove the last digit to continue the loop until all digits are removed 
                list_sum = list_sum // 10 

                # NOTE here that integer division is required but if you try to convert the resultant to integer after dividing it by 10, you will mess up with the number precision since the number could be very big. Try this commenting the above line to get random numbers :D. 
                # list_sum = (int) (list_sum / 10)

                print(f"\n\nl3 Node:\n\n{l3.val=}\n{list_sum=}\n") if DEBUG else None

            return l3_start.next    # Return the 2nd node as HEAD since 1st node is kept empty

        else:
            print("\nERROR: Please choose an appropriate METHOD!\n")








        

```