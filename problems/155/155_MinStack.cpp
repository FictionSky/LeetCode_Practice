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


class MinStack {
public:
    MinStack() {}

    void push(int val) {
        (void)val;
        // TODO：实现 push。
    }

    void pop() {
        // TODO：实现 pop。
    }

    int top() {
        // TODO：返回当前栈顶元素。
        return 0;
    }

    int getMin() {
        // TODO：返回当前最小值。
        return 0;
    }
};

int main() {
    cout << "练习目标：155. Min Stack" << '\n';
    cout << "只需要补全 MinStack 的 TODO 方法，再重新运行本地样例。" << "\n\n";
    cout << "示例 1" << '\n';
    MinStack solution;
    vector<string> actual = {"null"};
    solution.push(-2);
    actual.push_back("null");
    solution.push(0);
    actual.push_back("null");
    solution.push(-3);
    actual.push_back("null");
    actual.push_back(to_string(solution.getMin()));
    solution.pop();
    actual.push_back("null");
    actual.push_back(to_string(solution.top()));
    actual.push_back(to_string(solution.getMin()));
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(vector<string>{"null", "null", "null", "null", "-3", "null", "0", "-2"});
    cout << "\n\n";
    return 0;
}
