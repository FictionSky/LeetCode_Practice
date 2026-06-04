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


class LFUCache {
public:
    explicit LFUCache(int capacity) {
        (void)capacity;
        // TODO：初始化缓存状态。
    }

    int get(int key) {
        (void)key;
        // TODO：返回对应值，不存在时返回 -1。
        return -1;
    }

    void put(int key, int value) {
        (void)key;
        (void)value;
        // TODO：插入或更新一条记录。
    }
};

int main() {
    cout << "练习目标：460. LFU Cache" << '\n';
    cout << "只需要补全 LFUCache 的 TODO 方法，再重新运行本地样例。" << "\n\n";
    cout << "示例 1" << '\n';
    LFUCache solution(2);
    vector<string> actual = {"null"};
    solution.put(1, 1);
    actual.push_back("null");
    solution.put(2, 2);
    actual.push_back("null");
    actual.push_back(to_string(solution.get(1)));
    solution.put(3, 3);
    actual.push_back("null");
    actual.push_back(to_string(solution.get(2)));
    actual.push_back(to_string(solution.get(3)));
    solution.put(4, 4);
    actual.push_back("null");
    actual.push_back(to_string(solution.get(1)));
    actual.push_back(to_string(solution.get(3)));
    actual.push_back(to_string(solution.get(4)));
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(vector<string>{"null", "null", "null", "1", "null", "-1", "3", "null", "-1", "3", "4"});
    cout << "\n\n";
    return 0;
}
