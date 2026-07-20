""" Arrange array elements in alternating odd and even positions """

class Solution:
    def alternate_o_and_e(self, ar):
        even = sorted([x for x in ar if x % 2 == 0])
        odd = sorted([x for x in ar if x % 2 != 0])

        # Decide who starts
        if even[0] < odd[0]:
            even_idx, odd_idx = 0, 1
        else:
            even_idx, odd_idx = 1, 0

        # Check if arrangement is possible
        if abs(len(even) - len(odd)) > 1:
            print("Not Possible")
            return

        if len(even) > len(odd) and even_idx != 0:
            print("Not Possible")
            return

        if len(odd) > len(even) and odd_idx != 0:
            print("Not Possible")
            return

        # Fill the array
        for num in even:
            ar[even_idx] = num
            even_idx += 2

        for num in odd:
            ar[odd_idx] = num
            odd_idx += 2

        print(*ar)

if __name__=="__main__":
     c= Solution()
     ar = [6, 5 ,3, 2, 1, 4]
     c.alternate_o_and_e(ar)

