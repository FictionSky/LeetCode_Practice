#include <iostream>
#include <string>
#include <vector>

using namespace std;

void printValue(bool value) {
    cout << (value ? "true" : "false");
}

void printValue(const string& value) {
    cout << value;
}

void printValue(char value) {
    cout << value;
}

template <typename T>
void printValue(const vector<T>& values);

template <typename T>
void printValue(const T& value) {
    cout << value;
}

template <typename T>
void printVector(const vector<T>& values) {
    cout << "[";
    for (size_t i = 0; i < values.size(); ++i) {
        printValue(values[i]);
        if (i + 1 < values.size()) {
            cout << ", ";
        }
    }
    cout << "]";
}

template <typename T>
void printValue(const vector<T>& values) {
    printVector(values);
}


class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 下笔前先用一句话写清楚状态定义。
        // - 先从更小子问题如何转移到当前问题开始想。

        // ------------初版一----------------------

        // int result_c = 0;
        // int result_best = nums[0];
        // for (int i = 0; i < nums.size(); ++i){
        //     if(result_c + nums[i] < 0 ){
        //         result_c = 0;
        //         result_best = max(result_best,nums[i]);
        //         continue;
        //     }
        //     else{
        //         if(result_best < result_c + nums[i]){
        //             result_best =result_c + nums[i];
        //             result_c = result_best;
        //         }
        //         else{
        //             result_c = result_c + nums[i];
        //         }
        //     }
            
        // }
        // return result_best;

        // --------------------------------------------
        // ----------------优化后  贪心算法-------

        // int result = nums[0];
        // int count = 0;
        // for (int i = 0; i < nums.size(); i++) {
        //     count += nums[i];
        //     if (count > result) { // 取区间累计的最大值（相当于不断确定最大子序终止位置）
        //         result = count;
        //     }
        //     if (count <= 0) count = 0; // 相当于重置最大子序起始位置，因为遇到负数一定是拉低总和
        // }
        // return result;

        // --------------------------------------------
        // ----------------动态规划-------
        int dp = nums[0];
        int result = nums[0];

        for(int i = 1; i < nums.size(); ++i){
            dp = max(dp + nums[i],nums[i]);

            result = max(result, dp);
        }
        return result;


    }
};

void runCase(const string& label, vector<int> nums, int expected) {
    Solution solution;
    int actual = solution.maxSubArray(nums);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：53. Maximum Subarray" << '\n';
    cout << "只需要补全 maxSubArray() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {-2, 1, -3, 4, -1, 2, 1, -5, 4}, 6);
    runCase("示例 2", {1}, 1);
    return 0;
}
