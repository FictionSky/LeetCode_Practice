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
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 把每个格子看成一个节点，并先想清楚邻居如何找到。
        // - 特别注意边界判断和访问状态更新的时机。

        (void)mat;
        return {};
    }
};

void runCase(const string& label, vector<vector<int>> mat, vector<vector<int>> expected) {
    Solution solution;
    vector<vector<int>> actual = solution.updateMatrix(mat);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：542. 01 Matrix" << '\n';
    cout << "只需要补全 updateMatrix() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {{0, 0, 0}, {0, 1, 0}, {1, 1, 1}}, {{0, 0, 0}, {0, 1, 0}, {1, 2, 1}});
    return 0;
}
