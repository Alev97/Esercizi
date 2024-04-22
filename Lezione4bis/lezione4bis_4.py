
# Data una lista nums di interi, spostare gli zeri alla fine di questa lista 
# mantenendo l'ordine originale dei numeri che non sono zeri

def move_zeroes(nums: list[int]) -> list:
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(nums.pop(i))        
    print(nums)

list: list = [4,6,7,0,2,0,3]
move_zeroes(list)



    
