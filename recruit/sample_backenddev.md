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
> * 請使用 GitHub/GitLab.
> * 這份線上測驗分數會決定您的職級與薪資範圍。每個網頁功能有分數。請必定要交卷。
> * 2.5小時到時：
>   * 有開發多少，就交卷多少，考試並沒有所謂的 “完成”。
>   * 請必定要上架，並提供網頁 URL.
>	* 請填寫測驗完成表格 Exam Submission Form.

<br>

## 考題大綱

請開發一個可以使用，有前、後端的網站：

| 滿分 | 網頁功能 |
| --- | --- |
| 40 | 搜索一個過濾項目，支持多頁結果（pagination） |
| 60 | 搜索多個「及」過濾項目 |
| 50 | 搜索多個「或」過濾項目 |
| 50 | 搜索營業時間符合 |

[測驗分數評估]({{ site.baseurl }}/recruit/exam_rubric.html){: .btn#page-btn}

### 分數薪資計算例子

假設一位candidate的測驗，他完成以下：

- [x]  [填寫測驗完成表格]({{ site.exam_submit_form_url }}){:target="_blank"}
- [x]  有提供考試代碼GitHub/GitLab網址
- [x]  有提供網頁上架的live demo網址[（Heroku 免費）](https://medium.com/enjoy-life-enjoy-coding/heroku-搭配-git-在-heroku-上部署網站的手把手教學-bf4fd6f998b8){:target="_blank"}

分數如下：

| 滿分 | 分數 | 網頁功能 |
| --- | --- | --- |
| 40 | 72% | 搜索一個過濾項目，支持多頁結果（pagination） |
| 60 | 55% | 搜索多個「及」過濾項目 |
| 50 | 81% | 搜索多個「或」過濾項目 |
| 50 | 0% | 搜索營業時間符合 |

總分計算：
```
總分數 = 72% * 40 + 55% * 60 + 81% * 50 = 102.3
總分 = 102.3 / 200 * 100 = 51.15%
```

> **因為這位candidate分數是51%，他的工程階級考慮範圍就是 [Junior Engineer]({{ site.baseurl }}/people/engineering_level.html)。**

<br>

## 考題講解

* 請輸入提供的[csv檔案](https://docs.google.com/spreadsheets/d/1OanzakC9Uuo6fLLLyKScTSWDH6twnPOrSN-uWvoTz-U/edit?usp=sharing){:target="_blank"}進去資料庫，設計及實作後端搜索資料庫的RESTful-API。
	* 請使用relational的資料庫。
* 搜索RESTful-API需要直接對應後端資料庫的SQL query。
* [良好的API設計](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api){:target="_blank"}。
* 在`README.md`用markdown纖細解釋API。
	* 提供API query的樣本
	* 提供API query結果的樣本
* 搜索API需要考慮一張網頁最多可以顯示多少搜索結果，需要支持pagination。

## 考題細節：搜索API功能

### 1. 搜索一個過濾項目，支持多頁結果（pagination）

* 這個功能只能選一種條件。
* 過濾項目：
	* 星期幾
	* 類型
	* 米其林
	* 停車
	* 外送
	* 先繳訂金
	* 地理位子

### 2. 搜索多個「及」過濾項目（AND condition）

* 這個功能可以選多個過濾條件。
* 例如：
```
if ((類型 == 無菜單) && (米其林 == 1))
{
	// 找出全部米其林一星的無菜單餐廳
}
```

### 3. 搜索多個「或」過濾項目（OR condition）

* 這個功能可以選多個過濾條件。
* 例如：
```
if ((先繳訂金 == 否) || (停車 == 有))
{
	// 找出全部不用先繳訂金，或有停車位的餐廳
}
```

### 4. 搜索營業時間符合：

* 搜索結果是在指定的多個過濾條件當下，列出有營業的餐廳。
* 過濾條件：
	* 星期幾
	* 開始營業時間
	* 結束營業時間
* 例如：
```
if（星期幾 == 日 && 開始營業時間 >= 15:00 && 結束營業時間 <= 21:00)
{
	// 找出全部星期日下午3點至晚上9點有營業的餐廳
}
```

<br>

---

<br>

[立即申请]({{ site.job_form_url }}){: .btn#page-btn}{:target="_blank"}
[检阅考试指示]({{ site.baseurl }}/recruit/webdev.html){: .btn#page-btn}
[测验分数评估]({{ site.baseurl }}/recruit/exam_rubric.html){: .btn#page-btn}

## 考试指示

重要提醒：

> * 我们并不期望你完整开发每个功能。重点不是要全部 “做完”，是要查看有尝试部分的能力、进度，尽力而为就可以。
> * 请使用 GitHub/GitLab.
> * 这份线上测验分数会决定您的职级与薪资范围。每个网页功能有分数。请必定要交卷。
> * 2.5小时到时：
> 	* 有开发多少，就交卷多少，考试并没有所谓的 “完成”。
> 	* 请必定要上架，并提供网页 URL.
> 	* 请填写测验完成表格 Exam Submission Form.

<br>

## 考题大纲

请开发一个可以使用，有前、后端的网站：

| 满分 | 网页功能 |
| --- | --- |
| 40 | 搜索一个过滤项目，支持多页结果（pagination） |
| 60 | 搜索多个「及」过滤项目 |
| 50 | 搜索多个「或」过滤项目 |
| 50 | 搜索营业时间符合 |

[测验分数评估]({{ site.baseurl }}/recruit/exam_rubric.html){: .btn#page-btn}

### 分数薪资计算例子

假设一位candidate的测验，他完成以下：

- [x] [填写测验完成表格]({{ site.exam_submit_form_url }}){:target="_blank"}
- [x] 有提供考试代码GitHub/GitLab网址
- [x] 有提供网页上架的live demo网址[（Heroku 免费）](https://medium.com/enjoy-life-enjoy-coding/heroku-搭配-git-在-heroku-上部署网站的手把手教学-bf4fd6f998b8){:target="_blank"}

分数如下：

| 满分 | 分数 | 网页功能 |
| --- | --- | --- |
| 40 | 72% | 搜索一个过滤项目，支持多页结果（pagination） |
| 60 | 55% | 搜索多个「及」过滤项目 |
| 50 | 81% | 搜索多个「或」过滤项目 |
| 50 | 0% | 搜索营业时间符合 |

总分计算：
```
总分数 = 72% * 40 + 55% * 60 + 81% * 50 = 102.3
总分 = 102.3 / 200 * 100 = 51.15%
```

> **因为这位candidate分数是51%，他的工程阶级考虑范围就是 [Junior Engineer]({{ site.baseurl }}/people/engineering_level.html)。 **

<br>

## 考题讲解

* 请输入提供的[csv档案](https://docs.google.com/spreadsheets/d/1OanzakC9Uuo6fLLLyKScTSWDH6twnPOrSN-uWvoTz-U/edit?usp=sharing){:target="_blank"}进去资料库，设计及实作后端搜索资料库的RESTful-API。
* 请使用relational的资料库。
* 搜索RESTful-API需要直接对应后端资料库的SQL query。
* [良好的API设计](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api){:target="_blank"}。
* 在`README.md`用markdown纤细解释API。
	* 提供API query的样本
	* 提供API query结果的样本
* 搜索API需要考虑一张网页最多可以显示多少搜索结果，需要支持pagination。

## 考题细节：搜索API功能

### 1. 搜索一个过滤项目，支持多页结果（pagination）

* 这个功能只能选一种条件。
* 过滤项目：
	* 星期几
	* 类型
	* 米其林
	* 停车
	* 外送
	* 先缴订金
	* 地理位子

### 2. 搜索多个「及」过滤项目（AND condition）

* 这个功能可以选多个过滤条件。
* 例如：
```
if ((类型 == 无菜单) && (米其林 == 1))
{
// 找出全部米其林一星的无菜单餐厅
}
```

### 3. 搜索多个「或」过滤项目（OR condition）

* 这个功能可以选多个过滤条件。
* 例如：
```
if ((先缴订金 == 否) || (停车 == 有))
{
// 找出全部不用先缴订金，或有停车位的餐厅
}
```

### 4. 搜索营业时间符合：

* 搜索结果是在指定的多个过滤条件当下，列出有营业的餐厅。
* 过滤条件：
	* 星期几
	* 开始营业时间
	* 结束营业时间
* 例如：
```
if（星期几 == 日 && 开始营业时间 >= 15:00 && 结束营业时间 <= 21:00)
{
// 找出全部星期日下午3点至晚上9点有营业的餐厅
}
```

