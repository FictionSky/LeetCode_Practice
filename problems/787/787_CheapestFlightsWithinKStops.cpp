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
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 在选择 BFS、Dijkstra 或 DP 前，先定义清楚“状态”是什么。
        // - 注意某条路径代价何时已经确定，何时还可能继续变优。

        (void)n;
        (void)flights;
        (void)src;
        (void)dst;
        (void)k;
        return 0;
    }
};

void runCase(const string& label, int n, vector<vector<int>> flights, int src, int dst, int k, int expected) {
    Solution solution;
    int actual = solution.findCheapestPrice(n, flights, src, dst, k);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：787. Cheapest Flights Within K Stops" << '\n';
    cout << "只需要补全 findCheapestPrice() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", 4, {{0, 1, 100}, {1, 2, 100}, {2, 0, 100}, {1, 3, 600}, {2, 3, 200}}, 0, 3, 1, 700);
    return 0;
}
