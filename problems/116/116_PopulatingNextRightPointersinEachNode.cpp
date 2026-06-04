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


class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;
    Node() : val(0), left(nullptr), right(nullptr), next(nullptr) {}
    explicit Node(int value) : val(value), left(nullptr), right(nullptr), next(nullptr) {}
    Node(int value, Node* left, Node* right, Node* next)
        : val(value), left(left), right(right), next(next) {}
};


Node* buildNextTree(const vector<string>& values) {
    if (values.empty() || values[0] == "null") {
        return nullptr;
    }

    Node* root = new Node(stoi(values[0]));
    queue<Node*> pending;
    pending.push(root);
    size_t index = 1;

    while (!pending.empty() && index < values.size()) {
        Node* node = pending.front();
        pending.pop();

        if (index < values.size() && values[index] != "null") {
            node->left = new Node(stoi(values[index]));
            pending.push(node->left);
        }
        ++index;

        if (index < values.size() && values[index] != "null") {
            node->right = new Node(stoi(values[index]));
            pending.push(node->right);
        }
        ++index;
    }

    return root;
}

vector<vector<int>> nextLevelsToVector(Node* root) {
    vector<vector<int>> levels;
    Node* levelStart = root;

    while (levelStart != nullptr) {
        vector<int> level;
        Node* current = levelStart;
        Node* nextStart = nullptr;
        while (current != nullptr) {
            level.push_back(current->val);
            if (nextStart == nullptr) {
                if (current->left != nullptr) {
                    nextStart = current->left;
                } else if (current->right != nullptr) {
                    nextStart = current->right;
                }
            }
            current = current->next;
        }
        levels.push_back(level);
        levelStart = nextStart;
    }

    return levels;
}


class Solution {
public:
    Node* connect(Node* root) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 先想清楚当前节点是在递归前、中、后哪个阶段处理。
        // - 明确递归函数对“一个子树”返回的含义是什么。

        (void)root;
        return nullptr;
    }
};


int main() {
    Solution solution;
    cout << "练习目标：116. Populating Next Right Pointers in Each Node" << '\n';
    cout << "只需要补全 connect() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    {
        Node* root = buildNextTree({"1", "2", "3", "4", "5", "6", "7"});
        Node* actual = solution.connect(root);
        cout << "示例 1" << '\n';
        cout << "当前结果：";
        printValue(nextLevelsToVector(actual));
        cout << '\n';
        cout << "预期结果：";
        printValue(vector<vector<int>>{{1}, {2, 3}, {4, 5, 6, 7}});
        cout << "\n\n";
    }
    return 0;
}
