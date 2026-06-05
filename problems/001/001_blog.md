---
title: LeetCode 001. 两数之和（Two Sum）—— 从暴力枚举到高效哈希表
slug: leetcode-001-two-sum-hash-table
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

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** *`target`* 的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

### 示例 1
> **输入**：nums = [2,7,11,15], target = 9
> **输出**：[0,1]
> **解释**：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

}

## 2. 核心算法思维：哈希表（Hash Table）

[admonition color="blue" title="为什么引入哈希表？" icon="lightbulb-o"]
**暴力解法**需要使用双重循环，外层循环固定元素 $x$，内层循环去寻找 $target - x$。这种查找方式的本质是**线性查找**，每次查找的时间复杂度为 $O(n)$，导致整体复杂度飙升至 $O(n^2)$。

为了降低时间复杂度，我们需要优化“查找 $target - x$”这一步。**哈希表（散列表）**可以通过建立键（Key）与值（Value）的映射，将查找的时间复杂度降低到惊人的 $O(1)$！
[/admonition]

render{
### 什么是哈希表？
哈希表是一种通过**哈希函数（Hash Function）**将特定键（Key）映射到表中特定位置（Bucket/Slot）以进行快速访问的数据结构。
- **在本题中的映射关系**：
  - **键（Key）**：数组中元素的值。
  - **值（Value）**：该元素在数组中的下标。

### 解题空间换时间策略
我们在线性遍历数组时，每到一个新元素 `nums[i]`：
1. 计算当前所需的配对值：$complement = target - nums[i]$。
2. 检查**哈希表**中是否存在这个 `complement`。
3. 如果存在，说明找到了匹配对，直接返回 `[哈希表[complement], i]`。
4. 如果不存在，将当前元素及其下标存入哈希表 `hash_map[nums[i]] = i`，继续前进。
}

## 3. 算法实现（C++）

code cpp{
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // 创建哈希表：Key为数值，Value为对应的数组下标
        unordered_map<int, int> hash_map;
        
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            
            // 在哈希表中查找是否存在目标配对值
            if (hash_map.find(complement) != hash_map.end()) {
                return {hash_map[complement], i};
            }
            
            // 若不存在，则把当前元素和下标存入哈希表，供后续元素查找
            hash_map[nums[i]] = i;
        }
        return {};
    }
};
}

## 4. 复杂度分析

render{
- **时间复杂度**：$O(n)$ 
  - 我们只需要遍历包含 $n$ 个元素的数组一次。
  - 在哈希表中查找 $target - x$ 的时间复杂度为 $O(1)$。整体时间复杂度从暴力解法的 $O(n^2)$ 成功降低到 $O(n)$。
- **空间复杂度**：$O(n)$
  - 主要取决于哈希表的开销，哈希表最多需要存储 $n$ 个元素的键值对。
}

## 5. 易错点与避坑指南

shortcode{
[alert color="red" title="避坑：千万别重复使用自身" icon="exclamation-triangle"]
题目要求“数组中同一个元素在答案里不能重复出现”。如果先将整个数组一次性全部存入哈希表，再去查找，当 $target = 6$ 且数组中包含 `3` 时，`6 - 3 = 3` 会查找到 `3` 自身。
[/alert]
}

render{
**正确的处理方式（即上面的代码实现）**：采用**一边查询、一边入表**的“单遍哈希（One-pass Hash）”策略。查询时哈希表里只有当前元素*前方*的数字，绝不可能查到自己本身，天然避开了这个逻辑陷阱。
}


## 6. 互动与补充资料

shortcode{
[collapse title="点击查看哈希表碰撞机制补充（选读）" color="grey" icon="angle-right"]
哈希表在极罕见情况下会发生“哈希冲突”（即两个不同的 Key 计算出了相同的散列地址）。C++ 的 `std::unordered_map` 内部主要通过开链法（Separate Chaining）来解决冲突。虽然最坏情况下时间复杂度可能退化到 O(n)，但在平均情况下，其查找时间依旧稳定在常数阶 O(1)。
[/collapse]
}

render{
本题的代码已同步至我的个人 GitHub 仓库。

[github author="FictionSky" project="LeetCode_Practice" size="mini"][/github]
}