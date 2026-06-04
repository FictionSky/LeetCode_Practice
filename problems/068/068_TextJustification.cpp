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
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 先把题目拆成几个简单的状态更新步骤。
        // - 明确每个下标、单词片段或子串分别代表什么。

        (void)words;
        (void)maxWidth;
        return {};
    }
};

void runCase(const string& label, vector<string> words, int maxWidth, vector<string> expected) {
    Solution solution;
    vector<string> actual = solution.fullJustify(words, maxWidth);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：68. Text Justification" << '\n';
    cout << "只需要补全 fullJustify() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {"This", "is", "an", "example", "of", "text", "justification."}, 16, {"This    is    an", "example  of text", "justification.  "});
    return 0;
}
