# LeetCode 3 轮刷题计划（2026-06-04）

## 结论先说

- 不建议把目标定成“1000 道全新题”。
- 对于“基础薄弱，但目标达到大厂算法面试标准”的同学，更合理的目标是：
  - `275` 道高质量、覆盖主流题型的题目
  - `3` 轮完整复刷
  - 总完成次数约 `825` 次
- 如果后期你要强冲某一家大厂，再额外补 `25-50` 道该公司的高频 company-tag 题即可。

## 为什么不是 500 或 1000

这次方案基于下面几类公开资料做了交叉：

- LeetCode 官方 `LeetCode 75`：定位是 `2 个月内` 的面试准备，完成后建议多次重复。
- LeetCode 官方 `Top Interview 150`：官方描述是 `150` 道经典题，适合 `3+ months of prep time`。
- Grind 75 作者说明：从更大的候选池中精选出 `169` 道，并明确写到“`probably don't need to do beyond the 169 questions`”。
- NeetCode 150：把 Blind 75 扩展到 `150` 道，强调更完整、更适合系统复习。

综合这些来源，可以得到一个很稳的判断：

- `75` 道：够入门，不够稳拿大厂。
- `150-170` 道：已经接近常见面试高频核心池。
- `250-300` 道：如果是精刷、复刷、会总结，已经能覆盖绝大多数大厂算法面试核心模式。
- `500-1000` 道新题：更像“刷数量”，对基础薄弱的人投入产出比并不高。

所以这份计划把“独立新题量”定在 `275`，把重点放在 `3 轮重复` 和题型迁移上。

## 3 轮目标

### 第 1 轮：打基础

- 目标：先建立题型识别能力
- 重点：数组、哈希、双指针、滑窗、二分、链表、树、基础图论、基础 DP
- 要求：
  - 每题先自己想 `20-30` 分钟
  - 不会就看题解
  - 做完必须复盘：这题属于什么模式、为什么这样做

题量：`75` 题

#### Round 1 题号

1. `1` Two Sum    √
2. `217` Contains Duplicate √
3. `242` Valid Anagram    √
4. `20` Valid Parentheses √
5. `121` Best Time to Buy and Sell Stock √
6. `53` Maximum Subarray
7. `238` Product of Array Except Self
8. `49` Group Anagrams
9. `347` Top K Frequent Elements
10. `128` Longest Consecutive Sequence
11. `125` Valid Palindrome
12. `167` Two Sum II - Input Array Is Sorted
13. `344` Reverse String
14. `283` Move Zeroes
15. `11` Container With Most Water
16. `15` 3Sum
17. `643` Maximum Average Subarray I
18. `209` Minimum Size Subarray Sum
19. `3` Longest Substring Without Repeating Characters
20. `567` Permutation in String
21. `438` Find All Anagrams in a String
22. `424` Longest Repeating Character Replacement
23. `704` Binary Search
24. `35` Search Insert Position
25. `278` First Bad Version
26. `374` Guess Number Higher or Lower
27. `33` Search in Rotated Sorted Array
28. `153` Find Minimum in Rotated Sorted Array
29. `206` Reverse Linked List
30. `21` Merge Two Sorted Lists
31. `141` Linked List Cycle
32. `876` Middle of the Linked List
33. `19` Remove Nth Node From End of List
34. `83` Remove Duplicates from Sorted List
35. `160` Intersection of Two Linked Lists
36. `234` Palindrome Linked List
37. `155` Min Stack
38. `150` Evaluate Reverse Polish Notation
39. `739` Daily Temperatures
40. `232` Implement Queue using Stacks
41. `225` Implement Stack using Queues
42. `1047` Remove All Adjacent Duplicates In String
43. `94` Binary Tree Inorder Traversal
44. `144` Binary Tree Preorder Traversal
45. `145` Binary Tree Postorder Traversal
46. `104` Maximum Depth of Binary Tree
47. `226` Invert Binary Tree
48. `100` Same Tree
49. `101` Symmetric Tree
50. `543` Diameter of Binary Tree
51. `102` Binary Tree Level Order Traversal
52. `112` Path Sum
53. `200` Number of Islands
54. `733` Flood Fill
55. `695` Max Area of Island
56. `994` Rotting Oranges
57. `542` 01 Matrix
58. `207` Course Schedule
59. `133` Clone Graph
60. `463` Island Perimeter
61. `70` Climbing Stairs
62. `509` Fibonacci Number
63. `1137` N-th Tribonacci Number
64. `198` House Robber
65. `746` Min Cost Climbing Stairs
66. `62` Unique Paths
67. `64` Minimum Path Sum
68. `322` Coin Change
69. `56` Merge Intervals
70. `57` Insert Interval
71. `435` Non-overlapping Intervals
72. `55` Jump Game
73. `452` Minimum Number of Arrows to Burst Balloons
74. `54` Spiral Matrix
75. `73` Set Matrix Zeroes

### 第 2 轮：提升主流面试能力

- 目标：把中频和高频中等题打通
- 重点：树/BST、堆、回溯、Trie、图最短路、经典 DP、单调栈、更难的滑窗
- 要求：
  - 限时做题
  - 开始训练“看到题就判断模式”
  - 对第 1 轮错题同步回刷

题量：`100` 题

#### Round 2 题号

1. `14` Longest Common Prefix
2. `28` Find the Index of the First Occurrence in a String
3. `58` Length of Last Word
4. `151` Reverse Words in a String
5. `189` Rotate Array
6. `169` Majority Element
7. `380` Insert Delete GetRandom O(1)
8. `12` Integer to Roman
9. `13` Roman to Integer
10. `36` Valid Sudoku
11. `42` Trapping Rain Water
12. `392` Is Subsequence
13. `16` 3Sum Closest
14. `18` 4Sum
15. `76` Minimum Window Substring
16. `239` Sliding Window Maximum
17. `904` Fruit Into Baskets
18. `1493` Longest Subarray of 1's After Deleting One Element
19. `1004` Max Consecutive Ones III
20. `1658` Minimum Operations to Reduce X to Zero
21. `74` Search a 2D Matrix
22. `875` Koko Eating Bananas
23. `162` Find Peak Element
24. `34` Find First and Last Position of Element in Sorted Array
25. `81` Search in Rotated Sorted Array II
26. `540` Single Element in a Sorted Array
27. `658` Find K Closest Elements
28. `1539` Kth Missing Positive Number
29. `92` Reverse Linked List II
30. `24` Swap Nodes in Pairs
31. `61` Rotate List
32. `143` Reorder List
33. `2` Add Two Numbers
34. `25` Reverse Nodes in k-Group
35. `138` Copy List with Random Pointer
36. `146` LRU Cache
37. `82` Remove Duplicates from Sorted List II
38. `86` Partition List
39. `22` Generate Parentheses
40. `71` Simplify Path
41. `394` Decode String
42. `496` Next Greater Element I
43. `503` Next Greater Element II
44. `735` Asteroid Collision
45. `402` Remove K Digits
46. `84` Largest Rectangle in Histogram
47. `98` Validate Binary Search Tree
48. `230` Kth Smallest Element in a BST
49. `235` Lowest Common Ancestor of a Binary Search Tree
50. `236` Lowest Common Ancestor of a Binary Tree
51. `199` Binary Tree Right Side View
52. `114` Flatten Binary Tree to Linked List
53. `105` Construct Binary Tree from Preorder and Inorder Traversal
54. `106` Construct Binary Tree from Inorder and Postorder Traversal
55. `437` Path Sum III
56. `124` Binary Tree Maximum Path Sum
57. `173` Binary Search Tree Iterator
58. `222` Count Complete Tree Nodes
59. `215` Kth Largest Element in an Array
60. `703` Kth Largest Element in a Stream
61. `973` K Closest Points to Origin
62. `692` Top K Frequent Words
63. `378` Kth Smallest Element in a Sorted Matrix
64. `295` Find Median from Data Stream
65. `621` Task Scheduler
66. `373` Find K Pairs with Smallest Sums
67. `39` Combination Sum
68. `40` Combination Sum II
69. `46` Permutations
70. `78` Subsets
71. `90` Subsets II
72. `79` Word Search
73. `208` Implement Trie (Prefix Tree)
74. `211` Design Add and Search Words Data Structure
75. `417` Pacific Atlantic Water Flow
76. `210` Course Schedule II
77. `684` Redundant Connection
78. `547` Number of Provinces
79. `841` Keys and Rooms
80. `127` Word Ladder
81. `752` Open the Lock
82. `399` Evaluate Division
83. `1091` Shortest Path in Binary Matrix
84. `743` Network Delay Time
85. `416` Partition Equal Subset Sum
86. `518` Coin Change II
87. `91` Decode Ways
88. `139` Word Break
89. `5` Longest Palindromic Substring
90. `647` Palindromic Substrings
91. `1143` Longest Common Subsequence
92. `72` Edit Distance
93. `213` House Robber II
94. `309` Best Time to Buy and Sell Stock with Cooldown
95. `714` Best Time to Buy and Sell Stock with Transaction Fee
96. `763` Partition Labels
97. `134` Gas Station
98. `406` Queue Reconstruction by Height
99. `646` Maximum Length of Pair Chain
100. `45` Jump Game II

### 第 3 轮：大厂冲刺

- 目标：补高级题型，形成稳定的面试输出能力
- 重点：高级 DP、最短路、并查集、Trie 进阶、设计题、Hard 题、复杂贪心
- 要求：
  - Medium 题尽量 `20-25` 分钟内解决
  - Hard 题允许看提示，但要二刷三刷到能复现
  - 每周至少做一次模拟面试

题量：`100` 题

#### Round 3 题号

1. `41` First Missing Positive
2. `31` Next Permutation
3. `50` Pow(x, n)
4. `135` Candy
5. `137` Single Number II
6. `260` Single Number III
7. `201` Bitwise AND of Numbers Range
8. `190` Reverse Bits
9. `191` Number of 1 Bits
10. `338` Counting Bits
11. `85` Maximal Rectangle
12. `316` Remove Duplicate Letters
13. `456` 132 Pattern
14. `862` Shortest Subarray with Sum at Least K
15. `907` Sum of Subarray Minimums
16. `1438` Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
17. `901` Online Stock Span
18. `918` Maximum Sum Circular Subarray
19. `1425` Constrained Subsequence Sum
20. `1673` Find the Most Competitive Subsequence
21. `297` Serialize and Deserialize Binary Tree
22. `212` Word Search II
23. `572` Subtree of Another Tree
24. `103` Binary Tree Zigzag Level Order Traversal
25. `116` Populating Next Right Pointers in Each Node
26. `117` Populating Next Right Pointers in Each Node II
27. `1026` Maximum Difference Between Node and Ancestor
28. `987` Vertical Order Traversal of a Binary Tree
29. `1372` Longest ZigZag Path in a Binary Tree
30. `648` Replace Words
31. `677` Map Sum Pairs
32. `820` Short Encoding of Words
33. `787` Cheapest Flights Within K Stops
34. `778` Swim in Rising Water
35. `1631` Path With Minimum Effort
36. `1514` Path with Maximum Probability
37. `1466` Reorder Routes to Make All Paths Lead to the City Zero
38. `886` Possible Bipartition
39. `1202` Smallest String With Swaps
40. `1319` Number of Operations to Make Network Connected
41. `934` Shortest Bridge
42. `1162` As Far from Land as Possible
43. `1293` Shortest Path in a Grid with Obstacles Elimination
44. `1971` Find if Path Exists in Graph
45. `990` Satisfiability of Equality Equations
46. `2092` Find All People With Secret
47. `2421` Number of Good Paths
48. `2492` Minimum Score of a Path Between Two Cities
49. `1129` Shortest Path with Alternating Colors
50. `802` Find Eventual Safe States
51. `10` Regular Expression Matching
52. `44` Wildcard Matching
53. `115` Distinct Subsequences
54. `97` Interleaving String
55. `120` Triangle
56. `221` Maximal Square
57. `494` Target Sum
58. `377` Combination Sum IV
59. `279` Perfect Squares
60. `740` Delete and Earn
61. `931` Minimum Falling Path Sum
62. `1155` Number of Dice Rolls With Target Sum
63. `474` Ones and Zeroes
64. `673` Number of Longest Increasing Subsequence
65. `1048` Longest String Chain
66. `368` Largest Divisible Subset
67. `790` Domino and Tromino Tiling
68. `1035` Uncrossed Lines
69. `639` Decode Ways II
70. `312` Burst Balloons
71. `17` Letter Combinations of a Phone Number
72. `51` N-Queens
73. `52` N-Queens II
74. `131` Palindrome Partitioning
75. `140` Word Break II
76. `126` Word Ladder II
77. `332` Reconstruct Itinerary
78. `68` Text Justification
79. `502` IPO
80. `857` Minimum Cost to Hire K Workers
81. `659` Split Array into Consecutive Subsequences
82. `871` Minimum Number of Refueling Stops
83. `123` Best Time to Buy and Sell Stock III
84. `188` Best Time to Buy and Sell Stock IV
85. `460` LFU Cache
86. `432` All O\`one Data Structure
87. `224` Basic Calculator
88. `227` Basic Calculator II
89. `30` Substring with Concatenation of All Words
90. `4` Median of Two Sorted Arrays
91. `23` Merge k Sorted Lists
92. `480` Sliding Window Median
93. `786` K-th Smallest Prime Fraction
94. `1011` Capacity To Ship Packages Within D Days
95. `410` Split Array Largest Sum
96. `1235` Maximum Profit in Job Scheduling
97. `1482` Minimum Number of Days to Make m Bouquets
98. `287` Find the Duplicate Number
99. `632` Smallest Range Covering Elements from K Lists
100. `1531` String Compression II

## 推荐刷法

### 第 1 轮刷法

- 每天 `3-5` 题
- 重点是“看懂模式”
- 不求速度，求理解

### 第 2 轮刷法

- 每天 `4-6` 题
- 开始限时
- 同类题连续练，建立模式感

### 第 3 轮刷法

- 每天 `3-4` 题高质量题
- 搭配每周 `1-2` 次模拟面试
- 错题优先复刷

## 推荐时间线

- 如果你每天能投入 `2-3` 小时：
  - 第 1 轮：`6-8` 周
  - 第 2 轮：`8-10` 周
  - 第 3 轮：`8-10` 周
- 总周期大约：`5-7` 个月

## 判定是否达到“大厂可面”标准

满足下面 4 条，基本就到了比较像样的面试状态：

1. 上面 `275` 题你至少完整刷过 `3` 轮。
2. `80%` 的中等题能在 `25-35` 分钟内独立做出。
3. 常见题型一看到题就能判断模式，比如滑窗、二分、回溯、拓扑、并查集、1D/2D DP。
4. 你能把自己做过的错题，用自己的话讲清楚“为什么这么做、为什么别的方法不如它”。

## 这份计划用到的公开来源

- LeetCode 官方 `LeetCode 75`
  - https://leetcode.com/study-plan/leetcode-75/
- LeetCode 官方说明：完成 LeetCode 75 后建议至少重复 3 次
  - https://leetcode.com/discuss/post/2163754/study-plan-75-questions-till-interview-ready/
- LeetCode 官方 `Top Interview 150`
  - https://leetcode.com/studyplan/top-interview-150/
- Tech Interview Handbook `Best practice questions`
  - https://www.techinterviewhandbook.org/best-practice-questions/
- Grind 75 官方说明
  - https://www.techinterviewhandbook.org/grind75/about
- NeetCode 150
  - https://neetcode.io/practice/practice/neetcode150

## 一句话建议

你的情况更适合：

- 不追 `1000` 道新题
- 先吃透 `275` 道高质量题
- 用 `3` 轮复刷把题型真正变成自己的能力
