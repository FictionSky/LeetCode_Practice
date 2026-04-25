#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    // 这里是你刚刚写下的核心算法
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (numMap.count(complement)) {
                return {numMap[complement], i};
            }
            numMap[nums[i]] = i;
        }
        return {};
    }
};

int main() {
    Solution sol;
    
    // 第三步：在 main 函数中写测试用例
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    
    // 调用你的算法
    vector<int> result = sol.twoSum(nums, target);
    
    // 打印输出结果来验证
    if (result.size() == 2) {
        cout << "Output: [" << result[0] << ", " << result[1] << "]" << endl;
    } else {
        cout << "No solution found!" << endl;
    }
    
    return 0;
}