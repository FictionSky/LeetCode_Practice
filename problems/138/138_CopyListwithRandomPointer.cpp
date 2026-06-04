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
    Node* next;
    Node* random;
    Node(int value) : val(value), next(nullptr), random(nullptr) {}
};


Node* buildRandomList(const vector<pair<int, int>>& nodes) {
    if (nodes.empty()) {
        return nullptr;
    }

    vector<Node*> built;
    for (const auto& item : nodes) {
        built.push_back(new Node(item.first));
    }
    for (size_t i = 0; i + 1 < built.size(); ++i) {
        built[i]->next = built[i + 1];
    }
    for (size_t i = 0; i < nodes.size(); ++i) {
        int randomIndex = nodes[i].second;
        if (randomIndex >= 0) {
            built[i]->random = built[randomIndex];
        }
    }
    return built[0];
}

vector<vector<int>> randomListToPairs(Node* head, size_t limit = 100) {
    vector<Node*> nodes;
    unordered_map<Node*, int> indexByNode;
    Node* current = head;
    while (current != nullptr && nodes.size() < limit) {
        indexByNode[current] = static_cast<int>(nodes.size());
        nodes.push_back(current);
        current = current->next;
    }

    vector<vector<int>> result;
    for (Node* node : nodes) {
        int randomIndex = node->random == nullptr ? -1 : indexByNode[node->random];
        result.push_back({node->val, randomIndex});
    }
    return result;
}


class Solution {
public:
    Node* copyRandomList(Node* head) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 如果链表结构会变化，建议先把指针移动过程画出来。
        // - 每次修改前后，都要明确每个指针到底指向哪里。

        (void)head;
        return nullptr;
    }
};


int main() {
    Solution solution;
    cout << "练习目标：138. Copy List with Random Pointer" << '\n';
    cout << "只需要补全 copyRandomList() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    {
        Node* head = buildRandomList({{7, -1}, {13, 0}, {11, 4}, {10, 2}, {1, 0}});
        Node* actual = solution.copyRandomList(head);
        cout << "示例 1" << '\n';
        cout << "当前结果：";
        printValue(randomListToPairs(actual));
        cout << '\n';
        cout << "预期结果：";
        printValue(vector<vector<int>>{{7, -1}, {13, 0}, {11, 4}, {10, 2}, {1, 0}});
        cout << "\n\n";
    }
    return 0;
}
