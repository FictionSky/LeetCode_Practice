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
    int evalRPN(vector<string>& tokens) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 先判断题目需要的是后进先出还是先进先出。
        // - 如果是单调结构，先定义清楚它维护的是哪种顺序。

        (void)tokens;
        return 0;
    }
};

void runCase(const string& label, vector<string> tokens, int expected) {
    Solution solution;
    int actual = solution.evalRPN(tokens);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：150. Evaluate Reverse Polish Notation" << '\n';
    cout << "只需要补全 evalRPN() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {"2", "1", "+", "3", "*"}, 9);
    runCase("示例 2", {"4", "13", "5", "/", "+"}, 6);
    return 0;
}
