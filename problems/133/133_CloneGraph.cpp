#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
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


class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() : val(0) {}
    explicit Node(int value) : val(value) {}
    Node(int value, vector<Node*> neighbors) : val(value), neighbors(neighbors) {}
};


Node* buildSampleGraph() {
    Node* n1 = new Node(1);
    Node* n2 = new Node(2);
    Node* n3 = new Node(3);
    Node* n4 = new Node(4);
    n1->neighbors = {n2, n4};
    n2->neighbors = {n1, n3};
    n3->neighbors = {n2, n4};
    n4->neighbors = {n1, n3};
    return n1;
}

vector<vector<int>> graphToAdjList(Node* node) {
    if (node == nullptr) {
        return {};
    }

    unordered_map<Node*, bool> seen;
    queue<Node*> pending;
    vector<Node*> nodes;
    pending.push(node);
    seen[node] = true;

    while (!pending.empty()) {
        Node* current = pending.front();
        pending.pop();
        nodes.push_back(current);
        for (Node* neighbor : current->neighbors) {
            if (!seen[neighbor]) {
                seen[neighbor] = true;
                pending.push(neighbor);
            }
        }
    }

    size_t maxValue = 0;
    for (Node* current : nodes) {
        maxValue = max(maxValue, static_cast<size_t>(current->val));
    }
    vector<vector<int>> result(maxValue);
    for (Node* current : nodes) {
        for (Node* neighbor : current->neighbors) {
            result[current->val - 1].push_back(neighbor->val);
        }
    }
    return result;
}


class Solution {
public:
    Node* cloneGraph(Node* node) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 写代码前先定义：图中的点和边分别表示什么。
        // - 判断关键状态是遍历顺序、入度，还是访问标记。

        (void)node;
        return nullptr;
    }
};

int main() {
    Solution solution;
    Node* node = buildSampleGraph();
    Node* cloned = solution.cloneGraph(node);
    cout << "练习目标：133. Clone Graph" << '\n';
    cout << "只需要补全 cloneGraph() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    cout << "示例 1" << '\n';
    cout << "当前结果：";
    printValue(graphToAdjList(cloned));
    cout << '\n';
    cout << "预期结果：";
    printValue(vector<vector<int>>{{2, 4}, {1, 3}, {2, 4}, {1, 3}});
    cout << "\n\n";
    return 0;
}
