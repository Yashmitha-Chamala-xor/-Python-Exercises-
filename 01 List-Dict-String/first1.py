def list_stats(nums):
    total=sum(nums)
    return{
        "max":max(nums),
        "min":min(nums),
        "total" : total,
        "average": total/len(nums),
        "descending": sorted(nums,reverse=True),
        "every second": nums[::2]
        
    }
numbers=[14, 3, 9, 27, 8, 21, 5, 18]
stats=list_stats(numbers)
for key,value in stats.items():
    print(f"{key}:{value}")