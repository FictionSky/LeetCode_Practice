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
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 先定义任意时刻堆顶元素应该代表什么。
        // - 想清楚什么元素要入堆，以及元素何时会失效。

        (void)points;
        (void)k;
        return {};
    }
};

void runCase(const string& label, vector<vector<int>> points, int k, vector<vector<int>> expected) {
    Solution solution;
    vector<vector<int>> actual = solution.kClosest(points, k);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：973. K Closest Points to Origin" << '\n';
    cout << "只需要补全 kClosest() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {{1, 3}, {-2, 2}}, 1, {{-2, 2}});
    return 0;
}
