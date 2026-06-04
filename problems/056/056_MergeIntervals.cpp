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
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 如果区间之间的相对顺序重要，先考虑排序。
        // - 要明确写出贪心选择是什么，以及它为什么成立。

        (void)intervals;
        return {};
    }
};

void runCase(const string& label, vector<vector<int>> intervals, vector<vector<int>> expected) {
    Solution solution;
    vector<vector<int>> actual = solution.merge(intervals);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：56. Merge Intervals" << '\n';
    cout << "只需要补全 merge() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {{1, 3}, {2, 6}, {8, 10}, {15, 18}}, {{1, 6}, {8, 10}, {15, 18}});
    return 0;
}
