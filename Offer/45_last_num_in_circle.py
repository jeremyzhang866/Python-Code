class Solution:
    def simulation_by_cir_linked_list(self, n, m):
        nums = list(range(n))
        steps = m
        nums_length = n
        visited = 0
        while nums_length > 1:
            step = 0
            while step < steps:
                # 当越过当前数组的长度的时候，才会出现
                if visited + step > nums_length:
                    visited = 0
                    step = steps - step
                    break
                step += 1
            pop_num = visited + step
            
            # 这种情况只有在step都比num_length长的情况下出现
            if visited + step > nums_length:
                pop_num = step % nums_length  
            nums.pop(pop_num)
            visited = step
            nums_length -= 1
        return nums


    # 动态规划，找出递推关系，速度非常快
    # 我们注意到参数的位置非常重要，不能弄错，很多东西得严格。
    def game_by_dp_recu(self, n, m):
        if n == 1:
            return 0
        return (self.game_by_dp_recu(n - 1, m) + m) % n

    def game_by_dp_iter(self, n, m):
        res = 0
        count = 2
        while count <= n:
            res = (res + m) % count
            count += 1
        return res
