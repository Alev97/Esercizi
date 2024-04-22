
# Data una lista nums di n elementi, restituire l'elemento che compare più di n/2 volte.     

def majority_element(nums: list[int]) -> int:

# contiamo quante volte compare ciascun elemento

    for i in nums:
        if nums.count(i) > len(nums) / 2:
            print(i)
            return i
    return None

majority_element([1,2,2,3,2])


""" 
d: dict[int, int] = ()
for i in nums:
        d[i] = nums.count(i)

    lenght = len(nums)
    for key in d:
        d[key] /= lenght
        if d[key] > 0.5:
            return key

return None

"""


