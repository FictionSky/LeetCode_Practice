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


class MyQueue {
public:
    MyQueue() {}

    void push(int x) {
        (void)x;
        // TODO：实现 push。
    }

    int pop() {
        // TODO：实现 pop。
        return 0;
    }

    int peek() {
        // TODO：实现 peek。
        return 0;
    }

    bool empty() {
        // TODO：返回队列是否为空。
        return true;
    }
};

int main() {
    cout << "练习目标：232. Implement Queue using Stacks" << '\n';
    cout << "只需要补全 MyQueue 的 TODO 方法，再重新运行本地样例。" << "\n\n";
    cout << "示例 1" << '\n';
    MyQueue solution;
    vector<string> actual = {"null"};
    solution.push(1);
    actual.push_back("null");
    solution.push(2);
    actual.push_back("null");
    actual.push_back(to_string(solution.peek()));
    actual.push_back(to_string(solution.pop()));
    actual.push_back(solution.empty() ? "true" : "false");
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(vector<string>{"null", "null", "null", "1", "1", "false"});
    cout << "\n\n";
    return 0;
}
