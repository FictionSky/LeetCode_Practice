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


class RandomizedSet {
public:
    RandomizedSet() {}

    bool insert(int val) {
        (void)val;
        // TODO：实现 insert。
        return false;
    }

    bool remove(int val) {
        (void)val;
        // TODO：实现 remove。
        return false;
    }

    int getRandom() {
        // TODO：返回一个当前存储的值。
        return 0;
    }
};

int main() {
    cout << "练习目标：380. Insert Delete GetRandom O(1)" << '\n';
    cout << "只需要补全 RandomizedSet 的 TODO 方法，再重新运行本地样例。" << "\n\n";
    cout << "示例 1" << '\n';
    RandomizedSet solution;
    vector<string> actual = {"null"};
    actual.push_back(solution.insert(1) ? "true" : "false");
    actual.push_back(solution.remove(2) ? "true" : "false");
    actual.push_back(solution.insert(2) ? "true" : "false");
    actual.push_back(to_string(solution.getRandom()));
    actual.push_back(solution.remove(1) ? "true" : "false");
    actual.push_back(solution.insert(2) ? "true" : "false");
    actual.push_back(to_string(solution.getRandom()));
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(vector<string>{"null", "true", "false", "true", "2", "true", "false", "2"});
    cout << "\n\n";
    return 0;
}
