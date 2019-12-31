---
layout: default
title: 程式代碼規範
description: Coding Standards
---

> We are a strong adherent to coding standards, and code quality. 

## Automated Checks

We have **automated processes** for checking compliance with our coding standards. We use open source tools, web hooks that check source code for style and design problems post-commit. Commits with coding standard violations will auotmatically be rejected from the main branch.

## Google Style Guides by Default

We follow [**Google Style Guides**](https://google.github.io/styleguide/){:target="_blank"} for all langauges *UNLESS SPECIFIED OTHERWISE*. 

## Code Review

* Code reviews at done **BEFORE** the code is merged into main branch via a pull request.
* An engineer's direct manager should be added to **every pull request**.
* Code reviews are completed at the reviewer's own time.
* All reviewer's must approve before pull request can be approved.

### Motivation for Code Review

* Committers are motivated to write better code knowing if someone will look at it.
* Learning and sharing knowledge on how to write better code.
* Consistency in design and coding style.
* Catching bugs, anti-patterns, and design flaws early.