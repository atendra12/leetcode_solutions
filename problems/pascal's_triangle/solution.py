class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for row in range(1,numRows):
            row_result = []
            cols = row + 1
            prev_row = result[row - 1]
            for col in range(cols):
                if col-1 in range(len(prev_row)):
                    first_val = prev_row[col-1]
                else:
                    first_val = 0
                if col in range(len(prev_row)):
                    second_val = prev_row[col]
                else:
                    second_val = 0
                row_result.append(first_val + second_val)
            result.append(row_result)
        return result
            



        