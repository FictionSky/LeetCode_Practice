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
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 写代码前先定义：图中的点和边分别表示什么。
        // - 判断关键状态是遍历顺序、入度，还是访问标记。

        (void)numCourses;
        (void)prerequisites;
        return false;
    }
};

void runCase(const string& label, int numCourses, vector<vector<int>> prerequisites, bool expected) {
    Solution solution;
    bool actual = solution.canFinish(numCourses, prerequisites);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：207. Course Schedule" << '\n';
    cout << "只需要补全 canFinish() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", 2, {{1, 0}}, true);
    runCase("示例 2", 2, {{1, 0}, {0, 1}}, false);
    return 0;
}
