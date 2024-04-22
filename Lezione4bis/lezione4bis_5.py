
# Date due liste, restituire i valori che hanno in comune.

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    elementi_in_comune: list[int] = []
    for num in nums1:
        if num in nums2 and num not in elementi_in_comune:
            elementi_in_comune.append(num)
    return elementi_in_comune
print(intersection([1,2,3,4,2,],[7,2,4,8]))
