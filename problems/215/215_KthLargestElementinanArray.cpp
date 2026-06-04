#include <algorithm>
#include <cstdint>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
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
    int findKthLargest(vector<int>& nums, int k) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 先定义任意时刻堆顶元素应该代表什么。
        // - 想清楚什么元素要入堆，以及元素何时会失效。

        (void)nums;
        (void)k;
        return 0;
    }
};

void runCase(const string& label, vector<int> nums, int k, int expected) {
    Solution solution;
    int actual = solution.findKthLargest(nums, k);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：215. Kth Largest Element in an Array" << '\n';
    cout << "只需要补全 findKthLargest() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {3, 2, 1, 5, 6, 4}, 2, 5);
    return 0;
}
