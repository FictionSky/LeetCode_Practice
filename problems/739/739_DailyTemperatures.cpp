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
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 先判断题目需要的是后进先出还是先进先出。
        // - 如果是单调结构，先定义清楚它维护的是哪种顺序。

        (void)temperatures;
        return {};
    }
};

void runCase(const string& label, vector<int> temperatures, vector<int> expected) {
    Solution solution;
    vector<int> actual = solution.dailyTemperatures(temperatures);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：739. Daily Temperatures" << '\n';
    cout << "只需要补全 dailyTemperatures() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {73, 74, 75, 71, 69, 72, 76, 73}, {1, 1, 4, 2, 1, 1, 0, 0});
    return 0;
}
