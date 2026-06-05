#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>  //  基于哈希表实现的关联容器
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
    vector<int> twoSum(vector<int>& nums, int target) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 先想清楚：在一次扫描过程中，哪些信息需要被及时记录下来。
        // - 考虑是否可以用额外空间换取更快的查找速度。
        unordered_map<int, int>map;
        for (int i = 0; i < nums.size(); ++i)
        {
            int comp = target - nums[i];
            if (map.find(comp) != map.end())
            {
                return {map[comp],i};
            }
            map[nums[i]] = i;
        }
        
        return {};
    }
};

void runCase(const string& label, vector<int> nums, int target, vector<int> expected) {
    Solution solution;
    vector<int> actual = solution.twoSum(nums, target);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：1. Two Sum" << '\n';
    cout << "只需要补全 twoSum() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {2, 7, 11, 15}, 9, {0, 1});
    runCase("示例 2", {3, 2, 4}, 6, {1, 2});
    runCase("示例 3", {3, 3}, 6, {0, 1});
    return 0;
}
