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


struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};


ListNode* buildList(const vector<int>& values) {
    ListNode dummy;
    ListNode* tail = &dummy;
    for (int value : values) {
        tail->next = new ListNode(value);
        tail = tail->next;
    }
    return dummy.next;
}

vector<int> listToVector(ListNode* head, size_t limit = 100) {
    vector<int> values;
    while (head != nullptr && values.size() < limit) {
        values.push_back(head->val);
        head = head->next;
    }
    return values;
}

ListNode* buildCycleList(const vector<int>& values, int pos) {
    ListNode dummy;
    ListNode* tail = &dummy;
    ListNode* cycleEntry = nullptr;
    for (size_t i = 0; i < values.size(); ++i) {
        tail->next = new ListNode(values[i]);
        tail = tail->next;
        if (static_cast<int>(i) == pos) {
            cycleEntry = tail;
        }
    }
    if (tail != &dummy) {
        tail->next = cycleEntry;
    }
    return dummy.next;
}

ListNode* appendSharedTail(const vector<int>& prefix, ListNode* sharedTail) {
    if (prefix.empty()) {
        return sharedTail;
    }
    ListNode* head = buildList(prefix);
    ListNode* tail = head;
    while (tail->next != nullptr) {
        tail = tail->next;
    }
    tail->next = sharedTail;
    return head;
}


class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 如果链表结构会变化，建议先把指针移动过程画出来。
        // - 每次修改前后，都要明确每个指针到底指向哪里。

        (void)head;
        (void)x;
        return nullptr;
    }
};


int main() {
    Solution solution;
    cout << "练习目标：86. Partition List" << '\n';
    cout << "只需要补全 partition() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    {
        ListNode* list1 = buildList({1, 4, 3, 2, 5, 2});
        ListNode* actual = solution.partition(list1, 3);
        cout << "示例 1" << '\n';
        cout << "当前结果：";
        printValue(listToVector(actual));
        cout << '\n';
        cout << "预期结果：";
        printValue(vector<int>{1, 2, 2, 4, 3, 5});
        cout << "\n\n";
    }
    return 0;
}
