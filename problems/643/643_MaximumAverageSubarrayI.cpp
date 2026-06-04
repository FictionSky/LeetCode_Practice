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
    double findMaxAverage(vector<int>& nums, int k) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 写代码前先定义清楚：当前窗口表示什么。
        // - 明确窗口在什么条件下失效，以及应该如何收缩。

        (void)nums;
        (void)k;
        return 0.0;
    }
};

void runCase(const string& label, vector<int> nums, int k, double expected) {
    Solution solution;
    double actual = solution.findMaxAverage(nums, k);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：643. Maximum Average Subarray I" << '\n';
    cout << "只需要补全 findMaxAverage() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {1, 12, -5, -6, 50, 3}, 4, 12.75);
    runCase("示例 2", {5}, 1, 5.0);
    return 0;
}
