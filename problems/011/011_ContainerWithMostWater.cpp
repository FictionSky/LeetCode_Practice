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
    int maxArea(vector<int>& height) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 先定义每个指针分别表示什么，再去移动它。
        // - 思考左指针或右指针变化时，答案如何被更新。

        (void)height;
        return 0;
    }
};

void runCase(const string& label, vector<int> height, int expected) {
    Solution solution;
    int actual = solution.maxArea(height);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：11. Container With Most Water" << '\n';
    cout << "只需要补全 maxArea() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {1, 8, 6, 2, 5, 4, 8, 3, 7}, 49);
    runCase("示例 2", {1, 1}, 1);
    return 0;
}
