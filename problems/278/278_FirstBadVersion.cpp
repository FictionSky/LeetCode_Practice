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


int firstBadVersionForLocalTest = 1;

bool isBadVersion(int version) {
    return version >= firstBadVersionForLocalTest;
}


class Solution {
public:
    int firstBadVersion(int n) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 先判断你是在找精确值、边界位置，还是答案空间。
        // - 写代码前，先用一句话说清楚循环不变量是什么。

        (void)n;
        return 0;
    }
};


int main() {
    cout << "练习目标：278. First Bad Version" << '\n';
    cout << "只需要补全 firstBadVersion() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    {
        firstBadVersionForLocalTest = 4;
        Solution solution;
        int actual = solution.firstBadVersion(5);
        cout << "示例 1" << '\n';
        cout << "当前结果：";
        printValue(actual);
        cout << '\n';
        cout << "预期结果：";
        printValue(4);
        cout << "\n\n";
    }
    {
        firstBadVersionForLocalTest = 1;
        Solution solution;
        int actual = solution.firstBadVersion(1);
        cout << "示例 2" << '\n';
        cout << "当前结果：";
        printValue(actual);
        cout << '\n';
        cout << "预期结果：";
        printValue(1);
        cout << "\n\n";
    }
    return 0;
}
