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
    int lengthOfLongestSubstring(string s) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 写代码前先定义清楚：当前窗口表示什么。
        // - 明确窗口在什么条件下失效，以及应该如何收缩。

        (void)s;
        return 0;
    }
};

void runCase(const string& label, string s, int expected) {
    Solution solution;
    int actual = solution.lengthOfLongestSubstring(s);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：3. Longest Substring Without Repeating Characters" << '\n';
    cout << "只需要补全 lengthOfLongestSubstring() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", "abcabcbb", 3);
    runCase("示例 2", "bbbbb", 1);
    runCase("示例 3", "pwwkew", 3);
    return 0;
}
