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


class AllOne {
public:
    AllOne() {}

    void inc(string key) {
        (void)key;
        // TODO：实现 inc。
    }

    void dec(string key) {
        (void)key;
        // TODO：实现 dec。
    }

    string getMaxKey() {
        // TODO：返回任意一个最大频次的 key。
        return "";
    }

    string getMinKey() {
        // TODO：返回任意一个最小频次的 key。
        return "";
    }
};

int main() {
    cout << "练习目标：432. All O`one Data Structure" << '\n';
    cout << "只需要补全 AllOne 的 TODO 方法，再重新运行本地样例。" << "\n\n";
    cout << "示例 1" << '\n';
    AllOne solution;
    vector<string> actual = {"null"};
    solution.inc("hello");
    actual.push_back("null");
    solution.inc("hello");
    actual.push_back("null");
    actual.push_back(solution.getMaxKey());
    actual.push_back(solution.getMinKey());
    solution.inc("leet");
    actual.push_back("null");
    actual.push_back(solution.getMaxKey());
    actual.push_back(solution.getMinKey());
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(vector<string>{"null", "null", "null", "hello", "hello", "null", "hello", "leet"});
    cout << "\n\n";
    return 0;
}
