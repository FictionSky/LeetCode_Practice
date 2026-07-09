---
title: LeetCode 242. 有效的字母异位词题解
slug: leetcode-242-valid-anagram
status: draft
excerpt: LeetCode 242 有效的字母异位词，使用数组充当哈希表的解法思路与 C++ 代码实现。
categories:
  - leetcode
tags:
  - hash-table
  - string
---
render{
## 题目描述
}

shortcode{
[label color="blue" shape="round"]字符串[/label]
[label color="orange" shape="round"]哈希表[/label]
}

render{
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

**注意**：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

## 思路
}

shortcode{
[admonition color="blue" title="核心思路" icon="lightbulb-o"]
第一步：先判断两字符串长度是否相等，如果不等直接返回 false。
第二步：利用一个长度为 26 的数组作为哈希表。第一次遍历 s 时记录各字符出现的次数；第二次遍历 t 时扣减对应字符的次数。
第三步：如果在遍历 t 的过程中，对应字符的频次扣减后小于 0，说明 t 包含了一些额外的字符，可以直接返回 false。
[/admonition]
}

render{
## 代码
}

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        // 先判断长度是否一致，如果长度不同，绝对不可能是字母异位词
        if(s.size() != t.size())
        {
            return false;
        }

        // 使用长度为 26 的数组作为哈希表，统计每个字母出现的次数
        int count[26] = {0};
        
        // 遍历 s，增加对应字母的计数
        for (char c : s)
        {
            count[c - 'a']++;
        }

        // 遍历 t，减少对应字母的计数
        for (char c : t)
        {
            count[c - 'a']--;
            // 如果某个字母的计数小于 0，说明 t 中该字母比 s 中多，直接返回 false
            if (count[c - 'a'] < 0)
            {
                return false;
            }
        }
        
        // 遍历结束都没有返回 false，说明完全匹配
        return true;
    }
};
```

render{
## 复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为字符串的长度。需要分别遍历字符串 s 和 t 各一次。
- **空间复杂度**：$O(S)$，其中 $S$ 为字符集大小，本题中仅包含小写英文字母，所以 $S=26$。只需要常量级的额外空间。

## 仓库记录
}

shortcode{
[github author="FictionSky" project="LeetCode_Practice"][/github]
}