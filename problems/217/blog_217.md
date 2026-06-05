---
title: LeetCode 217. 存在重复元素（Contains Duplicate）—— 从哈希集合到布隆过滤器
slug: leetcode-217-contains-duplicate
status: draft
categories:
  - leetcode
tags:
  - hash-table
  - array
---

render{
## 1. 题目描述

[label color="blue" shape="round"]简单[/label]
[label color="indigo" shape="round"]数组[/label]
[label color="green" shape="round"]哈希表[/label]

给你一个整数数组 `nums` 。如果任一值在数组中出现 **至少两次** ，返回 `true` ；如果数组中每个元素互不相同，返回 `false` 。

### 示例 1
> **输入**：nums = [1,2,3,1]
> **输出**：true

### 示例 2
> **输入**：nums = [1,2,3,4]
> **输出**：false
}

## 2. 核心算法思维：哈希集合（Hash Set）

[admonition color="blue" title="从 Map 到 Set 的思维转变" icon="lightbulb-o"]
在 LeetCode 001「两数之和」中，我们需要同时知道**数值**和它对应的**数组下标**，因此使用了键值对映射的 `unordered_map`。

而在本题中，我们**只关心一个数字是否曾经出现过**，并不需要记录它出现的具体位置。因此，我们选择使用只存储键（Key）的**哈希集合（`std::unordered_set`）**。利用其 $O(1)$ 的查找效率，我们可以实现单遍扫描高效去重。
[/admonition]

render{
### 解题空间换时间策略
我们在线性遍历数组时，每遇到一个数字 `i`：
1. 检查**哈希集合**中是否已经存在数字 `i`（`map.find(i) != map.end()`）。
2. 如果存在，说明它之前已经出现过，直接返回 `true`（找到了重复元素）。
3. 如果不存在，说明这是第一次遇见它，将 `i` 存入集合中（`map.insert(i)`），然后继续检查下一个数字。

### 三种传统解法横向对比
除了哈希集合法，本题还有暴力双重循环和排序后邻项对比两种思路，它们各有优劣：

| 解法策略 | 时间复杂度 | 空间复杂度 | 优缺点分析 |
| :--- | :--- | :--- | :--- |
| **哈希集合法** (本解法) | $O(n)$ | $O(n)$ | **速度最快**，但消耗了额外的内存空间来存集合。 |
| **排序相邻对比法** | $O(n \log n)$ | $O(1)$ | 速度稍慢（受排序限制），但**极其节省内存**，不需要额外空间。 |
| **暴力双重循环法** | $O(n^2)$ | $O(1)$ | 速度极慢，在大数据集下会发生超时（TLE），不推荐。 |
}

## 3. 算法实现（C++）

code cpp{
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // 创建哈希集合，用于记录一次扫描过程中已经出现过的元素
        unordered_set<int> map;
        
        for (int i : nums) {
            // 在集合中查找当前元素是否已存在
            if (map.find(i) != map.end()) {
                return true; // 发现重复，及时返回
            }
            // 若不存在，则用额外空间换取速度，将其存入集合
            map.insert(i);
        }
        return false; // 扫描完毕，无重复
    }
};
}

## 4. 复杂度分析

render{
- **时间复杂度**：$O(n)$
  - 我们只需要对包含 $n$ 个元素的数组进行单次线性遍历。
  - 哈希集合 `unordered_set` 的底层基于哈希表实现，每次 `find` 和 `insert` 操作的平均时间复杂度均为 $O(1)$。因此整体时间复杂度为线性阶。
- **空间复杂度**：$O(n)$
  - 在最坏情况下（即数组中所有元素都互不相同），哈希集合需要存储数组中的全部 $n$ 个数字，因此需要消耗 $O(n)$ 的额外内存空间。
}

## 5. 进阶黑科技：大厂海量数据去重最优解 —— 布隆过滤器

[admonition color="indigo" title="什么是布隆过滤器（Bloom Filter）？" icon="info-circle"]
在 LeetCode 刷题时，我们的输入数组最多也就几万个元素。但在实际工业级后端开发中（例如：网页爬虫 URL 去重、垃圾邮件过滤、Redis 缓存穿透保护），数据量动辄是**几十亿**级别。

如果依然使用 `unordered_set` 存储几十亿个整数，会**吃掉极其恐怖的内存服务器带宽**。为了彻底压榨空间，工程师们通常会祭出神器 —— **布隆过滤器**。
[/admonition]

render{
### 布隆过滤器的原理
布隆过滤器是一个极其巧妙的**概率型数据结构**：
1. 它底层由一个**极长的二进制位数组（Bit Array，每个位置只有 0 或 1）**以及多个相互独立的**哈希函数**组成。
2. 当一个数字要存入时，通过多个哈希函数计算出多个位置，并将这些位置的 Bit 全部置为 `1`。
3. 当要查询一个数字是否存在时，再次计算这些位置。如果这些位置**有一个为 0**，那么这个数字**绝对不存在**；如果**全为 1**，说明这个数字**大概率存在**。

### 布隆过滤器的硬核优势
- **空间利用率达到极致**：它不存储原始数字本身（比如一个 `int` 需要 32 位），它只占用二进制数组里的几个 Bit 位！空间消耗只有哈希集合的几十分之一甚至几百分之一。
- **代价**：它存在极其微小的**误判率**（False Positive）。也就是说，如果它说一个元素“存在”，有极小的概率这个元素其实并不存在（因为哈希碰撞，这几个 Bit 被别的数字意外染成了 1）。但在绝大多数工程容错范围内，这个交换是极其划算的。
}

## 6. 易错点与避坑指南

shortcode{
[alert color="orange" title="代码细节：变量命名小贴士" icon="exclamation-triangle"]
在这段实现中，虽然变量名被定义成了 `map`（如 `unordered_set<int> map`），但它的实际数据结构是 **Set（集合）** 噢。在实际大厂面试或大型项目开发中，为了避免同行阅读代码时产生误解，更推荐将其命名为 `seen` 或 `hash_set`。
[/alert]
}

## 7. 互动与补充资料


如果你被限制：“不允许使用任何额外空间（空间复杂度必须为 $O(1)$）”，你可以使用以下排序解法：

```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // 先排序，时间复杂度 O(n log n)
        sort(nums.begin(), nums.end());
        // 线性扫描，检查相邻元素
        for (int i = 0; i < nums.size() - 1; ++i) {
            if (nums[i] == nums[i + 1]) {
                return true;
            }
        }
        return false;
    }
};
```

render{
本题的代码及更多算法题解均已同步至我的个人 GitHub 仓库。

[github author="FictionSky" project="LeetCode_Practice" size="mini"][/github]
}