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


class Trie {
public:
    Trie() {}

    void insert(string word) {
        (void)word;
        // TODO：实现 insert。
    }

    bool search(string word) {
        (void)word;
        // TODO：实现 search。
        return false;
    }

    bool startsWith(string prefix) {
        (void)prefix;
        // TODO：实现 startsWith。
        return false;
    }
};

int main() {
    cout << "练习目标：208. Implement Trie (Prefix Tree)" << '\n';
    cout << "只需要补全 Trie 的 TODO 方法，再重新运行本地样例。" << "\n\n";
    cout << "示例 1" << '\n';
    Trie solution;
    vector<string> actual = {"null"};
    solution.insert("apple");
    actual.push_back("null");
    actual.push_back(solution.search("apple") ? "true" : "false");
    actual.push_back(solution.search("app") ? "true" : "false");
    actual.push_back(solution.startsWith("app") ? "true" : "false");
    solution.insert("app");
    actual.push_back("null");
    actual.push_back(solution.search("app") ? "true" : "false");
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(vector<string>{"null", "null", "true", "false", "true", "null", "true"});
    cout << "\n\n";
    return 0;
}
