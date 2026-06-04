#include <iostream>
#include <queue>
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


class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 先想清楚当前节点是在递归前、中、后哪个阶段处理。
        // - 明确递归函数对“一个子树”返回的含义是什么。

        (void)root;
        return {};
    }
};


int main() {
    Solution solution;
    cout << "练习目标：102. Binary Tree Level Order Traversal" << '\n';
    cout << "只需要补全 levelOrder() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    {
        TreeNode* root = buildTree({"3", "9", "20", "null", "null", "15", "7"});
        auto actual = solution.levelOrder(root);
        cout << "示例 1" << '\n';
        cout << "当前结果：";
        printValue(actual);
        cout << '\n';
        cout << "预期结果：";
        printValue(vector<vector<int>>{{3}, {9, 20}, {15, 7}});
        cout << "\n\n";
    }
    return 0;
}
