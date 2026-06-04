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


class StockSpanner {
public:
    StockSpanner() {}

    int next(int price) {
        (void)price;
        // TODO：返回当前跨度。
        return 0;
    }
};

int main() {
    cout << "练习目标：901. Online Stock Span" << '\n';
    cout << "只需要补全 StockSpanner 的 TODO 方法，再重新运行本地样例。" << "\n\n";
    cout << "示例 1" << '\n';
    StockSpanner solution;
    vector<string> actual = {"null"};
    actual.push_back(to_string(solution.next(100)));
    actual.push_back(to_string(solution.next(80)));
    actual.push_back(to_string(solution.next(60)));
    actual.push_back(to_string(solution.next(70)));
    actual.push_back(to_string(solution.next(60)));
    actual.push_back(to_string(solution.next(75)));
    actual.push_back(to_string(solution.next(85)));
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(vector<string>{"null", "1", "1", "1", "2", "1", "4", "6"});
    cout << "\n\n";
    return 0;
}
