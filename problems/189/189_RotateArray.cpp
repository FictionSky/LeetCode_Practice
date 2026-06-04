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


class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 从左到右扫描时，先找出最关键、必须维护的状态量。
        // - 思考是否可以在每一步 O(1) 地更新当前最优答案。

        (void)nums;
        (void)k;
        return;
    }
};

void runCase(const string& label, vector<int> nums, int k, vector<int> expected) {
    Solution solution;
    solution.rotate(nums, k);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(nums);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：189. Rotate Array" << '\n';
    cout << "只需要补全 rotate() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {1, 2, 3, 4, 5, 6, 7}, 3, {5, 6, 7, 1, 2, 3, 4});
    return 0;
}
