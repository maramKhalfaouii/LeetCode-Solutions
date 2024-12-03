class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
    
        total_surplus = 0
        current_surplus = 0
        start_station = 0
        
        for i in range(len(gas)):
            total_surplus += gas[i] - cost[i]
            current_surplus += gas[i] - cost[i]
            
            # Reset start station if current surplus becomes negative
            if current_surplus < 0:
                start_station = i + 1
                current_surplus = 0
        
        return start_station
                        





        