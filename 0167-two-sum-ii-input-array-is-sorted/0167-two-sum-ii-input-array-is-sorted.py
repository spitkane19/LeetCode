class Solution(object):
    def twoSum(self, numbers, target):
        lngth = len(numbers)
        i=0
        j = lngth-1
        while i<j:
            j = lngth-1
            while j >= i:
                equals = numbers[i] + numbers[j]
                if equals == target:
                    return [i+1,j+1]
                if equals > target:
                    j -= 1
                    while numbers[j] == numbers[j+1]:
                        j -= 1        
                else:
                    i += 1
                    while numbers[i] == numbers[i-1]:
                        i += 1
                
        return False