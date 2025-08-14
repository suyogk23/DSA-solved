class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        int len = nums.size();

        for (int i=0; i<len ;i++){
            
            int comp = target-nums[i];
            if(map.find(nums[i]) != map.end()){
                return {map[nums[i]], i};
            }
            map[comp]=i;
            
        }
        return {};
    }
};
