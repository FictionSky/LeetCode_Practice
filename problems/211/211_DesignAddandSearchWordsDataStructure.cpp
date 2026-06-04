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


class WordDictionary {
public:
    WordDictionary() {}

    void addWord(string word) {
        (void)word;
        // TODO：实现 addWord。
    }

    bool search(string word) {
        (void)word;
        // TODO：实现 search。
        return false;
    }
};

int main() {
    cout << "练习目标：211. Design Add and Search Words Data Structure" << '\n';
    cout << "只需要补全 WordDictionary 的 TODO 方法，再重新运行本地样例。" << "\n\n";
    cout << "示例 1" << '\n';
    WordDictionary solution;
    vector<string> actual = {"null"};
    solution.addWord("bad");
    actual.push_back("null");
    solution.addWord("dad");
    actual.push_back("null");
    solution.addWord("mad");
    actual.push_back("null");
    actual.push_back(solution.search("pad") ? "true" : "false");
    actual.push_back(solution.search("bad") ? "true" : "false");
    actual.push_back(solution.search(".ad") ? "true" : "false");
    actual.push_back(solution.search("b..") ? "true" : "false");
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(vector<string>{"null", "null", "null", "null", "false", "true", "true", "true"});
    cout << "\n\n";
    return 0;
}
