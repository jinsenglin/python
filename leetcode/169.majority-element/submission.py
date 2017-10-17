class Memo(object):
    number = None
    count = None
    
    def __init__(self, number):
        self.number = number
        self.count = 1
    
    def add_one(self):
        self.count += 1


class MemoCollection(object):
    memos = None
    threshold = None
    majority = None
    
    def __init__(self, threshold):
        self.memos = []
        self.threshold = threshold
    
    def has_memo(self, number):
        for memo in self.memos:
            if memo.number == number:
                return True
            
        return False
    
    def add_memo(self, number):
        memo = Memo(number)
        self.memos.append(memo)
    
    
    def add_one(self, number):
        for memo in self.memos:
            if memo.number == number:
                memo.add_one()
       
    
    def has_majority(self):
        for memo in self.memos:
            if memo.count > self.threshold:
                self.majority = memo.number
                return True
            
        return False


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        mc = MemoCollection(len(nums)/2)
        
        for num in nums:
            if mc.has_memo(num):
                mc.add_one(num)
            else:
                mc.add_memo(num)
            
            if mc.has_majority():
                return mc.majority
