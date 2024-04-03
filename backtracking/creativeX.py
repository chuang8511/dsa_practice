# // https://codeinterview.io/PJBWBZQEWS
# // Inputs:
# // Coins: [1,2,3]
# // Sum: 5
# //
# // Expected Output:
# // [
# // [1, 1, 1, 1, 1],
# // [2, 3],
# // [1, 1, 3],
# // [1, 1, 1, 2],
# // [1, 2, 2],
# // ]
class Soultion:
  def solution(self, sum: int, coins: list):
    self.res = []
    
    coins.sort()
    possible_solution = []
    i = len(coins) - 1
    while sum > 0 and i >= 0:
      if coins[i] > sum:
        i -= 1
      else:
        sum -= coins[i]
        possible_solution.append(coins[i])
    
    possible_solution.sort()
    self.res.append(possible_solution) # [3, 2]
    
    if sum != 0:
      return []
    
    j = 0
    while j < len(self.res):
      result_to_be_break_down = self.res[j]
      for num in result_to_be_break_down:
        copy_solution = result_to_be_break_down.copy()
        copy_solution.remove(num)
        this_coin = num
        
        i = coins.index(num) - 1 # optimize the loop
        while num > 0 and i >= 0:
          if this_coin == coins[i]:
            i -= 1
          elif coins[i] > num:
            i -= 1
          else:
            num -= coins[i]
            copy_solution.append(coins[i])
        copy_solution.sort()
        if copy_solution and num == 0 and copy_solution not in self.res:
          self.res.append(copy_solution)
      j += 1

    return self.res

a = Soultion()
print(a.solution(5, [1,2,3]))

def coin_combinations(coins, target):
    def backtrack(start, remain, path):
        if remain == 0:
            result.append(path)
            return
        if remain < 0:
            return
        for i in range(start, len(coins)):
            backtrack(i, remain - coins[i], path + [coins[i]])
    
    result = []
    backtrack(0, target, [])
    return result


coins = [1, 2, 3]
target = 5
print(coin_combinations(coins, target))    
