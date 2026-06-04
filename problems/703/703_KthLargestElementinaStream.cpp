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


class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) {
        (void)k;
        (void)nums;
        // TODO：初始化数据结构。
    }

    int add(int val) {
        (void)val;
        // TODO：插入 val，并返回当前第 k 大元素。
        return 0;
    }
};

int main() {
    cout << "练习目标：703. Kth Largest Element in a Stream" << '\n';
    cout << "只需要补全 KthLargest 的 TODO 方法，再重新运行本地样例。" << "\n\n";
    cout << "示例 1" << '\n';
    vector<int> initialNumbers = vector<int>{4, 5, 8, 2};
    KthLargest solution(3, initialNumbers);
    vector<string> actual = {"null"};
    actual.push_back(to_string(solution.add(3)));
    actual.push_back(to_string(solution.add(5)));
    actual.push_back(to_string(solution.add(10)));
    actual.push_back(to_string(solution.add(9)));
    actual.push_back(to_string(solution.add(4)));
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(vector<string>{"null", "4", "5", "5", "8", "8"});
    cout << "\n\n";
    return 0;
}
