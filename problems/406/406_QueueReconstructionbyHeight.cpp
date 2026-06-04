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
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 写代码前先明确贪心选择到底是什么。
        // - 解释清楚为什么当前局部最优不会破坏全局最优。

        (void)people;
        return {};
    }
};

void runCase(const string& label, vector<vector<int>> people, vector<vector<int>> expected) {
    Solution solution;
    vector<vector<int>> actual = solution.reconstructQueue(people);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：406. Queue Reconstruction by Height" << '\n';
    cout << "只需要补全 reconstructQueue() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {{7, 0}, {4, 4}, {7, 1}, {5, 0}, {6, 1}, {5, 2}}, {{5, 0}, {7, 0}, {5, 2}, {6, 1}, {4, 4}, {7, 1}});
    return 0;
}
