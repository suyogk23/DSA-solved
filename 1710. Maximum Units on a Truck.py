class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # TC: O(n log n) + O(n)
        # Space: constant
        # sort the boxes according to unit size and start adding the boxes with highest unit first to the truct
        # maximise (units/box) into the truck
        n = len(boxTypes)
        boxTypes.sort(key = lambda x : x[1], reverse = True)
        max_units = 0

        for box in boxTypes:
            num_boxes = box[0]
            num_units = box[1]
            if num_boxes <= truckSize:
                max_units += (num_units * num_boxes)
                truckSize -= num_boxes
            else:
                max_units += (num_units * truckSize)
                truckSize = 0
            if truckSize == 0:
                return max_units
        
        return max_units


