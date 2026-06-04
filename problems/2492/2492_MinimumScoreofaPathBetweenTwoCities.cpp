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
    int minScore(int n, vector<vector<int>>& roads) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 先判断题目本质是不是在维护连通块。
        // - 明确什么时刻应该把两个点合并到同一集合。

        (void)n;
        (void)roads;
        return 0;
    }
};

void runCase(const string& label, int n, vector<vector<int>> roads, int expected) {
    Solution solution;
    int actual = solution.minScore(n, roads);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：2492. Minimum Score of a Path Between Two Cities" << '\n';
    cout << "只需要补全 minScore() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", 4, {{1, 2, 9}, {2, 3, 6}, {2, 4, 5}, {1, 4, 7}}, 5);
    return 0;
}
