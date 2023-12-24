# Features

- All **$$#LehanaCodes$$** are with proper explanation of the intuition.
- In addition to text explanation, the code is also fully commented to assist coders in understanding each statement. 
- Set `DEBUG` to `True` and you can then visualize the logic as the code executes. 
- Any method (Two-Pointer and Three-Pointer) can be chosen by setting `METHOD` to `1`, `2` or `3`. 

> *Join me in my mission to teach coding in a way that goes beyond the basics, embracing the way to visualize how to code, exploring corner cases, and understanding each statement that is written. Please like and follow!*


![lehana_codes.jpg](https://assets.leetcode.com/users/images/33f36ff3-aae1-42cd-964e-841c1f8267c7_1703343149.8495882.jpeg)



# Intuition
We know substring is continous and so can our approach be. Let's start from the beginning of string! For each character we see, in order to include it in the substring, it should not have appeared before. So, we check if it appeared before. If yes, we shorten our current substring by starting it from the last appearence of the character so that our current character is included and we continue our iteration to expand our substring.

The next time we check for the appearance, we only check in the current substring window since we have already excluded the characters appearing before the character excluded in previous iteration. For example, in string `fdvdfe`, once we reach the last `f`, we would have already excluded first `f` in our current substring when we excluded first `d` to include second `d`. Hence, we just maintain the start of current substring which is always one plus the index of any last seen character. 

This approach might seem greedy since we are ignoring previous substring only to concentrate on expanding our current substring, which could come smaller than last biggest substring.But since we only have to return the maximum length, just keep focusing on expanding your current substring and maintain the maximum length yet. If you go through the DEBUG code, you will realize that previous substring (or last seen characters) were already accounted.

Now, to check the last appearance, we have three methods. Simplest one is to check the appearance in the current substring using a loop. This is the **Last Seen Loop Method** and it introduces another time complexity. To simplify this, we can use a HashMap to store the last index of any character which is the **Last Seen Map Method**. This introduces a variable space (maximum of possible characters) but makes the nested process in $$O(1)$$. Further, to use constant space with similar time, an integer array can be used to store the index for a Character ASCII. This is the **Last Seen Array Method** and uses constant 128-byte array.   

# Approach


**Last Seen Map Method**

Traverse each character in the string and keep storing the index of the character in a `HashMap <Character, Index>`. During traversal, if the character was already seen (is in the map) after the current substring start index (inital), update the start index (now, last seen index + 1) and the length of the substring (now, new start till current index). Return the maximum length.

 
1. Initialize current substring length (`current_len = 0`), maximum length yet (`max_len = 0`) and start index of current substring (`start = 0`).

2. Initialize a character HashMap (`char_map`) which will store the last seen index of a character in form <Character, Index>. 

3. Traverse the string until end with each character as `ch`.

4. Check if the `ch` has appeared before in current substring i,e. `char_map[ch] >= start`.

5. If yes, update current substring length to start after the last seen index i.e. `current_len = idx - char_map[ch] - 1`. This excludes current ch as it will be accounted always in Step 6. Also, update the start of current substring to just after the last seen index i.e. `start = char_map[ch] + 1 `.

6. Increment the current substring length and update the last seen index for `ch`.  

7. Update the maximum length (`max_len`) yet if current length crosses it.

8. Repeat from 3.

9. Return the `max_len`.   


---


**Last Seen Array Method**

Traverse each character in the string and keep storing the index of the character in an `Array <Character ASCII, Index>` (initially `-1`). During traversal, if the character was already seen (`array[ascii] > -1`) after the current substring start index (initally, `0`), update the start index (now, last seen index + 1) and the length of the substring (now, new start till current index). Return the maximum length.

 
1. Initialize current substring length (`current_len = 0`), maximum length yet (`max_len = 0`) and start index of current substring (`start = 0`).

2. Initialize an Array (`char_set`) which will store the last seen index of a character in form <Character ASCII, Index>. Thus, the index of this array will be the character ASCII value and the value will be the last seen index of the character. Intialize it to `-1` not `0` since `0` is a valid index.  

3. Traverse the string until end with each character as `ch`.

4. Check if the `ch` has appeared before in current substring i,e. `char_set[int(ch)] >= start`.

5. If yes, update current substring length to start after the last seen index. This excludes current ch as it will be accounted always in Step 6. Also, update the start of current substring to just after the last seen index.

6. Increment the current substring length and update the last seen index for `ch`.  

7. Update the maximum length (`max_len`) yet if current length crosses it.

8. Repeat from 3.

9. Return the `max_len`.   


---


**Last Seen Loop Method**

Traverse each character in the string and check if current character exists in the current substring by running a loop. If yes, update the substring from after the last seen position. Return the maximum length.


 
1. Initialize current substring length (`current_len = 0`), maximum length yet (`max_len = 0`) and start index of current substring (`start = 0`). 

2. Traverse the string until end with each character as `ch`.

3. Initialize a flag, `ch_exists = False` to check if `ch` existed before in the current substring. 

4. Check if the `ch` has appeared before in current substring i,e. run a loop from start to just before `ch` and break with `ch_exists = True` if `ch` is found. 

5. If `ch` existed, update current substring length to start after the last seen index. This excludes current ch as it will be accounted always in Step 6. Also, update the start of current substring to just after the last seen index.

6. Increment the current substring length.  

7. Update the maximum length (`max_len`) yet if current length crosses it.

8. Repeat from 3.

9. Return the `max_len`.   

# Complexity

**Time complexity:**

1. Map: $$O(n)$$ `42 ms`
2. Array: $$O(n)$$ `48 ms`
3. Loop: $$O(n^2)$$ `60 ms`


**Space complexity:**

1. Map: $$O(n)$$ `17.6 MB`
2. Array: $$O(n)$$ `17.3 MB`
3. Loop: $$O(n^2)$$ `17.6 MB`

**Note:** *Loop Method introduces quadratic time complexity but does not save much space. This is because the space used by Map is maximum of 128 keys (max of possible characters). For the same reasons, the Array method won't necessary do much good with constant space.*


# Code
```

# README: https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/4446962/lehanacodes-last-seen-map-array-and-loop-sliding-window-beats-99-5/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        """

        Choose the METHOD you want to execute:

        (1) Last Seen Map: Traverse each character in the string and keep storing the index of the character in a Map <Character, Index>. During traversal, if the character was already seen (is in the map) after the current substring start index (inital), update the start index (now, last seen index + 1) and the length of the substring (now, new start till current index). Return the maximum length.

        (2) Last Seen Array: Traverse each character in the string and keep storing the index of the character in an Array <Character ASCII, Index> (initially -1). During traversal, if the character was already seen (array[ascii] > -1) after the current substring start index (initally, 0), update the start index (now, last seen index + 1) and the length of the substring (now, new start till current index). Return the maximum length.

        (3) Last Seen Loop: Traverse each character in the string and check if current character exists in the current substring. If yes, update the substring from after the last seen position. Return the maximum length.

        """

        METHOD = 1

        # If set to True, prints information to stdout during execution to help debug and visualize
        DEBUG = False
        
        # Last Seen Map
        if METHOD == 1:

            current_len = 0     # Length on current substring
            max_len = 0         # Length of longest substring yet
            start = 0           # Start index of current substring
            char_map = {}       # Map to store last seen index of a character in form <Character, Index>

            # Traverse the string and when a character reappears, recalculate the current_len and start
            for idx, ch in enumerate(s):

                print(f"\n-----\n{char_map=}\n") if DEBUG else None
                
                # If the character has appeared before in current substring, update the start of substring after the character
                if ch in char_map and char_map[ch] >= start:
                    
                    current_len = idx - char_map[ch] - 1    # Updated length, excluding current character
                    start = char_map[ch] + 1                # Updated start is just after last seen index

                    print(f"\nDuplicate found: {ch} at position {char_map[ch]}\n\n") if DEBUG else None

                
                current_len += 1    # For every case, as we are progressing, increment the current substring length to include current character. 
                char_map[ch] = idx  # Store the latest index of the character for future iterations

                # Update the maximum length if the current length is the longest substring yet, otherwise, just keep progressing with current substring as maximum length is already stored
                if current_len > max_len:
                    max_len = current_len

                
                print(f"\nPost Iteration (string = {s}):\n{current_len=}\t{max_len=}\t{start=}\t{char_map=}\n") if DEBUG else None

            return max_len

        elif METHOD == 2:

            current_len = 0         # Length on current substring
            max_len = 0             # Length of longest substring yet
            start = 0               # Start index of current substring

            # Integer array to store last seen index of a character in form <Character ASCII, Index, inialized to -1 since index starts from 0
            char_set = [-1] * 128   

            # Traverse the string and when a character reappears, recalculate the current_len and start
            for idx, ch in enumerate(s):
                
                # Index of the character last seen, -1 in case not seen yet
                ch_idx = char_set[ord(ch)]

                # If the character has appeared before in current substring, update the start of substring after the character
                if ch_idx >= start:

                    current_len = idx - ch_idx - 1  # Updated length, excluding current character
                    start = ch_idx + 1              # Updated start is just after last seen index

                    print(f"\nDuplicate found: {ch} at position {ch_idx}\n\n") if DEBUG else None


                current_len += 1        # For every case, as we are progressing, increment the current substring length to include current character. 
                char_set[ord(ch)] = idx # Store the latest index of the character (ascii) for future iterations

                # Update the maximum length if the current length is the longest substring yet, otherwise, just keep progressing with current substring as maximum length is already stored
                if current_len > max_len:
                    max_len = current_len

                
                print(f"\nPost Iteration (string = {s}):\n{current_len=}\t{max_len=}\t{start=}\n") if DEBUG else None
            return max_len

        elif METHOD == 3:

            current_len = 0         # Length on current substring
            max_len = 0             # Length of longest substring yet
            start = 0               # Start index of current substring

            # Traverse the string and when a character reappears, recalculate the current_len and start
            for idx, ch in enumerate(s):
                
                ch_exists = False   # Flag to check if character existed before in current substring

                # Iterate the current substring (exludes current character) to check if current character appeared before
                for j in range(start, idx):
                    
                    # If seen before, set Flag and break with j as the index of last appearance
                    if s[j] == ch:
                        ch_exists = True
                        break

                # If the character has appeared before in current substring, update the start of substring after the character
                if ch_exists:

                    current_len = idx - j - 1   # Updated length, excluding current character 
                    start = j + 1               # Updated start is just after last seen index              

                    print(f"\nDuplicate found: {ch} at position {j}\n\n") if DEBUG else None

                
                current_len += 1    # For every case, as we are progressing, increment the current substring length to include current character. 

                # Update the maximum length if the current length is the longest substring yet, otherwise, just keep progressing with current substring as maximum length is already stored
                if current_len > max_len:
                    max_len = current_len

                
                print(f"\nPost Iteration (string = {s}):\n{current_len=}\t{max_len=}\t{start=}\n") if DEBUG else None
            return max_len
            

        else:
            print("\nERROR: Please choose an appropriate METHOD!\n")





```