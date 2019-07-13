class Solution:
    """
    @param people: a random list of people
    @return: the queue that be reconstructed
    """
    def reconstructQueue(self, people):
        # # 遍历排好序的people，从身高最高的人开始，根据每个人的k值，将其插入到结果数组中
        # 因为我们遍历是从身高最高的人开始的，所以即使后面有人插入改变了前面插入人在结果集中的位置，但是相对关系没有变，即每个人的前面比他高的人这个事实没有变，也因为后面插入的人的身高都低于前面的人，所以无法影响之前的结果
        # takes O(n^2)
        result = []
        sorted_people = sorted(people, key = lambda x: (-x[0], x[1]))
        
        for p in sorted_people:
            # insert takes O(n)
            result.insert(p[1], p)
            
        return result
