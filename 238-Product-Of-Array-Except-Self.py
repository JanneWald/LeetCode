# I used the divide operator, would be more effecient if I used prefix list and postfix list

def productExceptSelf(self, nums: List[int]) -> List[int]:
        Zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                Zeros += 1
        if Zeros > 1:
            return [0] * len(nums)
        if Zeros == 1:
            res = []
            total = 1
            for num in nums:
                if num != 0:
                    total *= num
            for num in nums:
                if num != 0:
                    res.append(0)
                else:
                    res.append(total)
            return res
        else:
            res = []
            total = 1
            for num in nums:
                total *= num
            for num in nums:
                res.append(int(total/num))
            return res
