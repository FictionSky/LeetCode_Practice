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
    bool canJump(vector<int>& nums) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 如果区间之间的相对顺序重要，先考虑排序。
        // - 要明确写出贪心选择是什么，以及它为什么成立。

        (void)nums;
        return false;
    }
};

void runCase(const string& label, vector<int> nums, bool expected) {
    Solution solution;
    bool actual = solution.canJump(nums);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：55. Jump Game" << '\n';
    cout << "只需要补全 canJump() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {2, 3, 1, 1, 4}, true);
    runCase("示例 2", {3, 2, 1, 0, 4}, false);
    return 0;
}
