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
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 先定义任意时刻堆顶元素应该代表什么。
        // - 想清楚什么元素要入堆，以及元素何时会失效。

        (void)matrix;
        (void)k;
        return 0;
    }
};

void runCase(const string& label, vector<vector<int>> matrix, int k, int expected) {
    Solution solution;
    int actual = solution.kthSmallest(matrix, k);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：378. Kth Smallest Element in a Sorted Matrix" << '\n';
    cout << "只需要补全 kthSmallest() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {{1, 5, 9}, {10, 11, 13}, {12, 13, 15}}, 8, 13);
    return 0;
}
