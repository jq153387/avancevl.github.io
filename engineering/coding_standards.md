---
layout: default
title: 程式代碼規範
description: Coding Standards
---

# 程式代碼規範的重要性

* **會加強工程師品質。**習慣寫好程式格式，規範一致會讓你變成更好的軟體工程師。
* **當程式代碼容易閱讀開發時間會自然縮短。**比較容易讀懂程式在做什麼。
* **提高程式效能。**JavaScript有時後是個蠻奇怪的語言。代碼格式一致會讓效能提高。

# 代碼格式自動檢查工具

| 工具 | 用途 |
| --- | --- |
| Prettier | 完全幫你把代碼formatting弄一致 |
| ESLint | 代碼品質，自動找bug |
| Linting rule sets, plugins, and extensions | 決定代碼規範 |
| Git hooks | 自動化程式規範 |

## 第一步驟：和解Prettier和自動代碼格式


## 第二步驟：使用Husky加Lint-Staged來自動化Prettier的Git Hooks


## 



# Sytle Guides

## 基礎格式

| JavaScript | [Airbnb Sytle Guide](https://github.com/airbnb/javascript){:target="_blank"} |
| C++ | [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html){:target="_blank"} |
| Python | [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html){:target="_blank"} |


## 例外格式

* tab一定要用space取代。

<br>

# Code Review

* Code reviews at done **BEFORE** the code is merged into main branch via a pull request.
* An engineer's direct manager should be added to **every pull request**.
* Code reviews are completed at the reviewer's own time.
* All reviewer's must approve before pull request can be approved.

<br>

# Code Review的重要性

* Committers are motivated to write better code knowing if someone will look at it.
* Learning and sharing knowledge on how to write better code.
* Consistency in design and coding style.
* Catching bugs, anti-patterns, and design flaws early.