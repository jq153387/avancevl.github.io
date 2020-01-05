---
layout: default
title: 後端測驗樣本
description: Back-End Sample Exam
---

[立即申請]({{ site.job_form_url }}){: .btn#page-btn}{:target="_blank"}
[檢閱考試指示]({{ site.baseurl }}/recruit/webdev.html){: .btn#page-btn}
[測驗分數評估]({{ site.baseurl }}/recruit/exam_rubric.html){: .btn#page-btn}

## 考試指示 

重要提醒：

> * 我們並不期望你完整開發每個功能。重點不是要全部 “做完”，是要查看有嘗試部分的能力、進度，盡力而為就可以。
> * 請使用 GitHub/GitLab
> * 這份線上測驗分數會決定您的職級與薪資範圍。每個網頁功能有分數。請必定要交卷
> * 2.5小時到時，請：
>   * 請必定要上架，並提供 URL
>   * 有開發多少，就交卷多少，考試並沒有所謂的 “完成”

---

## 考題講解

* 請設計和實作後端搜索RESTful-API。
* 搜索RESTful-API需要直接對應後端資料庫的SQL query。
* 良好的[API設計](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api){:target="_blank"}。
* 在README.md用markdown纖細解釋API。
	* 提供API query的樣本
	* 提供API query結果的樣本
* 搜索API需要考慮一張網頁最多可以顯示多少搜索結果，需要支持pagination。

## 考題細節：搜索API功能

### 1. 搜索一個過濾項目

過濾項目：

* 星期幾
* 類型
* 停車
* 外送
* 先繳訂金
* 地理位子

### 2. 搜索多個「及」過濾項目

### 3. 搜索多個「或」過濾項目

### 4. 搜索營業時間符合：

* 星期幾
* 開始營業時間
* 結束營業時間
