class Solution:
    def bestClosingTime(self, customers: str) -> int:
        maxvalue = 0
        sumvalue = 0
        index = - 1
        customers = list(customers)
        for i, item in enumerate(customers):
            if item == 'Y':
                sumvalue += 1
            if item == 'N':
                sumvalue -= 1
            if sumvalue > maxvalue:
                maxvalue = sumvalue
                index = i
        
        return index + 1

            


















        