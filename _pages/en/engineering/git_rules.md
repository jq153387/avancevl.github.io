---
layout: default
title: Git管理規範
lang: en
description: Git Rules
---



# Development vs Main Branches

1. Develop in your local branch
1. Merge your local branch into the main branch at least once a week.
1. Once merge your local branch, make sure you delete your merged branch
1. Maintain only one local development branch.


# Git Issues Label Flow

<img src='https://lh3.googleusercontent.com/pJG_uZvQDA_el-zoA2jMNpwK44X2OmvoaLodGiueYrP3lt_lhtubqRUttT0vV-8lH8LmgM-oHHQEikI-7todMtxA5PBQVJwUVKJLFgeRLcUfQ3gZVGKiSZaU8X9r_nNao2pr3WNcDw=w400' />

## 1. Engineer Finishes Features

1. Engineer self-test feature you implemented.
1. Engineer paste demo URL link in git issue comment for manager to test.
1. Engineer set git issue to `Ready to Review`.

## 2. Manager Reviews Feature

1. Manager test feature engineer implemented.
1. Manager equest changes in git issue comment.
1. Manager will set git issue to `Make Change`.

## 3. Engineer Makes Changes

1. Engineer make changes requested by manager.
1. Engineer get git issue to `Ready to Review`.

## 4. Manager Reviews Changes

1. Manager test fixes.
1. Manager will set git issues to `Ready to Merge`.

## 5. Engineer Merges Changes to Master

1. Engineer merge changes to master branch.
1. Engineer deploy changes to master deployment.
1. Engineer closes git issue.