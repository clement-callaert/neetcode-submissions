class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse = True)

        slowest = 0
        nbr_fleet = 0
        
        for pos, spd in cars:
            time = (target - pos) / spd

            if time > slowest:
                nbr_fleet += 1
                slowest = time

        return nbr_fleet
                
             
        