class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        seen1 = [0] * 26
        seen2 = [0] * 26

        # Count s1 and the first window of s2
        for i in range(len(s1)):
            seen1[ord(s1[i]) - ord("a")] += 1
            seen2[ord(s2[i]) - ord("a")] += 1

        # Count how many letter frequencies currently match
        matches = 0

        for i in range(26):
            if seen1[i] == seen2[i]:
                matches += 1

        l = 0

        # Slide the window through s2
        for r in range(len(s1), len(s2)):
            # Check the current window before sliding it
            if matches == 26:
                return True

            # Add the new character on the right
            rightIndex = ord(s2[r]) - ord("a")
            seen2[rightIndex] += 1

            # Update matches for the entering character
            if seen1[rightIndex] == seen2[rightIndex]:
                matches += 1
            elif seen1[rightIndex] + 1 == seen2[rightIndex]:
                matches -= 1

            # Remove the old character on the left
            leftIndex = ord(s2[l]) - ord("a")
            seen2[leftIndex] -= 1

            # Update matches for the leaving character
            if seen1[leftIndex] == seen2[leftIndex]:
                matches += 1
            elif seen1[leftIndex] - 1 == seen2[leftIndex]:
                matches -= 1

            l += 1

        # The loop checks before sliding, so check the final window here
        return matches == 26