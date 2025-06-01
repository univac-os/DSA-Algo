class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        pos = {person: i for i, person in enumerate(row)}  # maps person -> index
        swaps = 0

        for i in range(0, n, 2):
            first = row[i]
            partner = first ^ 1  # get the expected partner
            if row[i + 1] != partner:
                partner_index = pos[partner]

                # swap partner into the correct position (i+1)
                row[i + 1], row[partner_index] = row[partner_index], row[i + 1]

                # update positions after swap
                pos[row[partner_index]] = partner_index
                pos[row[i + 1]] = i + 1

                swaps += 1

        return swaps
