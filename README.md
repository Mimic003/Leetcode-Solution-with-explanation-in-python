<h1 align="center">📘 LeetCode Python Solutions with Explanations</h1>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/AbhishekKumarTiwari/LeetCode-Python-Solutions?color=informational&style=flat-square" />
  <img src="https://img.shields.io/github/stars/AbhishekKumarTiwari/LeetCode-Python-Solutions?style=flat-square" />
  <img src="https://img.shields.io/github/last-commit/AbhishekKumarTiwari/LeetCode-Python-Solutions?style=flat-square" />
  <img src="https://img.shields.io/github/license/AbhishekKumarTiwari/LeetCode-Python-Solutions?style=flat-square" />
</p>

---

## 🧠 About This Repository

Welcome to the **LeetCode Python Solutions** repo!  
This repository contains:

- ✅ Clean and well-commented Python solutions to various LeetCode problems.
- 📌 Detailed **step-by-step explanations** for each problem.
- 📚 Categorized by topic (e.g., Arrays, Strings, Trees, DP, etc.)
- 🚀 Easy navigation for beginners and pros alike!

> 📍 Whether you're prepping for interviews or mastering DSA, this repo has you covered!

---

## 🗂️ Folder Structure

```
LeetCode-Solutions/
│
├── Arrays/
│   ├── Two_Sum.py
│   └── Best_Time_to_Buy_and_Sell_Stock.py
│
├── Strings/
│   ├── Valid_Anagram.py
│   └── Longest_Substring_Without_Repeating.py
│
├── Trees/
│   └── Invert_Binary_Tree.py
│
└── README.md
```

Each Python file contains:
- ✅ Full solution
- 📌 Comments for logic
- 💡 Explanation of approach and complexity

---

## 🛠️ Tech Stack

- 🐍 Python 3
- 📘 LeetCode Problems
- 🧾 Markdown
- 💻 Git & GitHub

---

## ✨ Sample Problem Format

```python
# 🔍 Problem: Two Sum (https://leetcode.com/problems/two-sum/)
# ✅ Difficulty: Easy

# 🧠 Approach:
# - Use a hashmap to store numbers and their indices
# - For each number, check if (target - number) is in the hashmap

def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i

# 🕒 Time Complexity: O(n)
# 🗃️ Space Complexity: O(n)
```

---

## 📈 Progress Tracker

| Category     | Problems Solved | Link                        |
|--------------|-----------------|-----------------------------|
| Arrays       | ✅ 10/50         | [View Folder](./Arrays)     |
| Strings      | ✅ 8/40          | [View Folder](./Strings)    |
| Trees        | ✅ 5/30          | [View Folder](./Trees)      |
| DP           | ✅ 4/50          | [Coming Soon]               |

> 🛠️ Actively being updated every week!

---

## 🤝 Contributing

Contributions are welcome!  
If you'd like to improve explanations, add problems, or fix bugs, feel free to open a PR.

1. Fork the repo 🍴
2. Create your feature branch (`git checkout -b new-feature`)
3. Commit your changes (`git commit -m 'Add explanation to X problem'`)
4. Push to the branch (`git push origin new-feature`)
5. Open a pull request 🚀

---

## 📬 Contact

Feel free to reach out via:
- 📧 Email: abhishekmimic@gmail.com
- 💼 LinkedIn: https://www.linkedin.com/in/abhishek-kumar-tiwari-2a569330b/
- 🌐 GitHub: https://github.com/Mimic003

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer"/>
</p>