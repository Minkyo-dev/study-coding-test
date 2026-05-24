import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory
from typing import List


@profile_time_memory
def mysolution(prices: List[int]) -> int:
    tot_profit = 0
    today = 0
    end_day = len(prices) - 1
    while today < end_day:
        if prices[today] < prices[today + 1] :
            tot_profit += (prices[today + 1] - prices[today])
        today += 1
    print(tot_profit)    
    return tot_profit




@profile_time_memory
def othersolution(prices: List[int]) -> int:
    """
    Calculate maximum profit from multiple stock transactions.
    Buy and sell whenever there's a price increase from one day to the next.
    
    Args:
        prices: List of stock prices where prices[i] is the price on day i
        
    Returns:
        Maximum profit achievable from multiple buy-sell transactions
    """
    # Initialize total profit
    total_profit = 0
    
    # Iterate through consecutive price pairs
    for i in range(1, len(prices)):
        # Calculate profit from buying on day i-1 and selling on day i
        daily_profit = prices[i] - prices[i-1]
        
        # Only add positive profits (buy low, sell high on consecutive days)
        if daily_profit > 0:
            total_profit += daily_profit
    
    return total_profit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    prices = [1,2,3,4,5]
    prices = [7,6,4,3,1]
    mysolution(prices)
    # othersolution()
