---
layout: default
title: 前端測驗樣本
description: Front-End Sample Exam
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


考題範圍、分數計算，請參考**[全端測驗樣本]({{ site.link_sample_fullstackdev }})**。分數計算與考題會類似。

For exam topics and score calculation, please reference **[Full Stack Sample Exam]({{ site.link_sample_fullstackdev }})**. The scoring system and problems will be similiar.

<br>

---

<br>

## 考題大綱

請開發一個可以使用，有前端的網站：

| 滿分 | 網頁功能 |
| --- | --- |
| 40 |  |
| 60 |  |
| 50 |  |
| 50 |  |

[測驗分數評估]({{ site.baseurl }}/recruit/exam_rubric.html){: .btn#page-btn}


## 規則

1. **RWD.** Web 和 mobile browser 使用。
1. **必須使用 JavaScript.**
1. **JS 框架.** 您必須使用一個JS框架; 我們偏愛 React 或 Vue。如果需要，可以使用 Angular, Ember, Backbone, 或 Aurelia，但您需要有充分的理由選擇它。不能使用 jquery。
1. **HTML 和 CSS.** 您必須證明對HTML和CSS的了解與熟悉。
	* 加分題：使用 preprocessors SCSS/Sass。
	* 加分題：我們鼓勵您使用框架，譬如 Bootstrap。
1. ** RESTful.**
1. **有現代網頁設計感.** 乾淨頁面，字體、顏色容易讀。

## 考題講解

* 下載[csv檔案](https://docs.google.com/spreadsheets/d/1OanzakC9Uuo6fLLLyKScTSWDH6twnPOrSN-uWvoTz-U/edit?usp=sharing){:target="_blank"}。
* 使用這個檔案為需要顯示的資料。

## 考題

請自由選擇你想要開發的網頁功能，沒有先後次序。

### 1. 呈現訊息

* 在首頁顯示檔案裡面的資訊，表格的每一行是餐廳名字，使用者可以按/點，伸縮更多的餐廳資訊（展開、收起）。
* 展開資訊有訂位按鈕有圖標表示類型、米其林星、停車、外送、先繳訂金、評價。

### 2. 搜尋功能：

* 網頁最上方有搜尋功能，使用者可以輸入的欄位與搜尋按鈕：餐廳名字(輸入時，會有下拉式的建議)、訂位人數(使用下拉式選單)、日期(使用日曆選單)、時間(使用下拉式選單)

### 3. 訂位按鈕與 pop-up 視窗

* 展開餐廳資訊裡，有訂位按鈕
* 訂位按鈕會有 pop-up 視窗
* pop-up 視窗是一個讓使用者可以填寫的表格：名字、電話(輸入數字限制)、訂位人數(使用下拉式選單)、日期(使用日曆選單)、時間(使用下拉式選單)
* pop-up 視窗可以關閉的

### 4. 地理位子

* pop-up 視窗裡面使用
[Google Maps API](https://developers.google.com/maps/documentation/embed/start) 顯示小地圖（餐廳的地理位子）。


### 5. 中/英文頁面

* 有中/英文語言切換選擇。實際資料不需要翻譯，只需要有兩個 URL 分辨。
* 網頁版：右上方，使用語言切换按钮。
* 手機版：右上方有隱藏的三橫條線 hamburger menu 選單，選單裡面有語言切换按钮。

<br>

---

<br>

## Requirements

1. **RWD.**  Responsive and designed for cross-web development and mobile.
1. **JavaScript only.**
1. **JS frameworks.** You must use a JS framework; we prefer React or Vue. You may use Angular, Ember, Backbone, or Aurelia, if you must, but you need to have a good reason for choosing it. No jquery.
1. **HTML and CSS.** You must demonstrate your knowledge in HTML and CSS.
	* For bonus points, demonstrate your knowledge in preprocessors SCSS/Sass.
	* We encourage you to use frameworks, like Bootstrap.
1. **RESTful.**
1. **Modern web design sense**
