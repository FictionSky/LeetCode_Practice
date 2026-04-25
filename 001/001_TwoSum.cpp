#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (numMap.count(complement)) {
                return {numMap[complement], i};
            }
            numMap[nums[i]] = i;  // 将数字和索引建立哈希表
        }
        return {};
    }
};

int main() {
    Solution sol;
    
    vector<int> nums = {2, 7, 11, 15};
    int target = 13;
    
    vector<int> result = sol.twoSum(nums, target);
    
    if (result.size() == 2) {
        cout << "Output: [" << result[0] << ", " << result[1] << "]" << endl;
    } else {
        cout << "No solution found!" << endl;
    }
    
    return 0;
}