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


class MapSum {
public:
    MapSum() {}

    void insert(string key, int val) {
        (void)key;
        (void)val;
        // TODO：实现 insert。
    }

    int sum(string prefix) {
        (void)prefix;
        // TODO：返回此前缀的和值。
        return 0;
    }
};

int main() {
    cout << "练习目标：677. Map Sum Pairs" << '\n';
    cout << "只需要补全 MapSum 的 TODO 方法，再重新运行本地样例。" << "\n\n";
    cout << "示例 1" << '\n';
    MapSum solution;
    vector<string> actual = {"null"};
    solution.insert("apple", 3);
    actual.push_back("null");
    actual.push_back(to_string(solution.sum("ap")));
    solution.insert("app", 2);
    actual.push_back("null");
    actual.push_back(to_string(solution.sum("ap")));
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(vector<string>{"null", "null", "3", "null", "5"});
    cout << "\n\n";
    return 0;
}
