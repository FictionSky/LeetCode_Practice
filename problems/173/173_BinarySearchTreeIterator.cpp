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


struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};


TreeNode* buildTree(const vector<string>& values) {
    if (values.empty() || values[0] == "null") {
        return nullptr;
    }

    TreeNode* root = new TreeNode(stoi(values[0]));
    queue<TreeNode*> pending;
    pending.push(root);
    size_t index = 1;

    while (!pending.empty() && index < values.size()) {
        TreeNode* node = pending.front();
        pending.pop();

        if (index < values.size() && values[index] != "null") {
            node->left = new TreeNode(stoi(values[index]));
            pending.push(node->left);
        }
        ++index;

        if (index < values.size() && values[index] != "null") {
            node->right = new TreeNode(stoi(values[index]));
            pending.push(node->right);
        }
        ++index;
    }

    return root;
}

vector<string> treeToLevelVector(TreeNode* root) {
    vector<string> values;
    if (root == nullptr) {
        return values;
    }

    queue<TreeNode*> pending;
    pending.push(root);
    while (!pending.empty()) {
        TreeNode* node = pending.front();
        pending.pop();
        if (node == nullptr) {
            values.push_back("null");
            continue;
        }
        values.push_back(to_string(node->val));
        pending.push(node->left);
        pending.push(node->right);
    }

    while (!values.empty() && values.back() == "null") {
        values.pop_back();
    }
    return values;
}

TreeNode* findNode(TreeNode* root, int value) {
    if (root == nullptr) {
        return nullptr;
    }
    if (root->val == value) {
        return root;
    }
    TreeNode* left = findNode(root->left, value);
    if (left != nullptr) {
        return left;
    }
    return findNode(root->right, value);
}

vector<int> rightChainToVector(TreeNode* root, size_t limit = 100) {
    vector<int> values;
    TreeNode* current = root;
    while (current != nullptr && values.size() < limit) {
        values.push_back(current->val);
        current = current->right;
    }
    return values;
}


class BSTIterator {
public:
    explicit BSTIterator(TreeNode* root) {
        (void)root;
        // TODO：初始化迭代器状态。
    }

    int next() {
        // TODO：返回下一个最小值。
        return 0;
    }

    bool hasNext() {
        // TODO：返回是否还有下一个值。
        return false;
    }
};

int main() {
    cout << "练习目标：173. Binary Search Tree Iterator" << '\n';
    cout << "只需要补全 BSTIterator 的 TODO 方法，再重新运行本地样例。" << "\n\n";
    cout << "示例 1" << '\n';
    TreeNode* root = buildTree({"7", "3", "15", "null", "null", "9", "20"});
    BSTIterator solution(root);
    vector<string> actual = {"null"};
    actual.push_back(to_string(solution.next()));
    actual.push_back(to_string(solution.next()));
    actual.push_back(solution.hasNext() ? "true" : "false");
    actual.push_back(to_string(solution.next()));
    actual.push_back(solution.hasNext() ? "true" : "false");
    actual.push_back(to_string(solution.next()));
    actual.push_back(solution.hasNext() ? "true" : "false");
    actual.push_back(to_string(solution.next()));
    actual.push_back(solution.hasNext() ? "true" : "false");
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(vector<string>{"null", "3", "7", "true", "9", "true", "15", "true", "20", "false"});
    cout << "\n\n";
    return 0;
}
