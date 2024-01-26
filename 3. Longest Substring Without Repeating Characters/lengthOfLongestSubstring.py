# README: https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/4446962/lehanacodes-last-seen-map-array-and-loop-sliding-window-beats-99-5/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        """

        Choose the METHOD you want to execute:

        (1) Last Seen Map: Traverse each character in the string and keep storing the index of the character in a Map <Character, Index>. During traversal, rgif the character was already seen (is in the map) after the current substring start index (inital), update the start index (now, last seen index + 1) and the length of the substring (now, new start till current index). Return the maximum length.

        (2) Last Seen Array: Traverse each character in the string and keep storing the index of the character in an Array <Character ASCII, Index> (initially -1). During traversal, if the character was already seen (array[ascii] > -1) after the current substring start index (inital), update the start index (now, last seen index + 1) and the length of the substring (now, new start till current index). Return the maximum length.

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
            return -1




