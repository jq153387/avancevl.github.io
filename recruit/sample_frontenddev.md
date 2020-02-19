---
layout: default
title: 前端測驗樣本
description: Front-End Sample Exam
---

<a name="zh-tw"></a>

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

<br>

## 考題大綱

請開發一個可以使用，有前端的網站。

| 滿分 | 網頁功能 |
| --- | --- |
| 30 | 呈現訊息 |
| 30 | 搜尋功能 |
| 45 | 訂位按鈕與 pop-up 視窗 |
| 65 | D3 畫圖 |
| 30 | 中/英文頁面 |

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
* 展開資訊有訂位按鈕和有圖示表示類型、米其林星、停車、外送、先繳訂金、評價。
* 表格共有2頁，可以前後去第一、二頁。

### 2. 搜尋功能

* 網頁最上方有搜尋功能，使用者可以輸入的欄位與搜尋按鈕：餐廳名字(輸入時，會有下拉式的建議)、訂位人數(使用下拉式選單)、日期(使用日曆選單)、時間(使用下拉式選單)。UI 請參考並盡量相似 [OpenTable](https://www.opentable.com/?lang=ja){:target="_blank"}

### 3. 訂位按鈕與 pop-up 視窗

* 展開餐廳資訊裡，有訂位按鈕
* 訂位按鈕會有 pop-up 視窗
* pop-up 視窗是一個讓使用者可以填寫的表格：名字、電話(輸入數字限制)、訂位人數(使用下拉式選單)、日期(使用日曆選單)、時間(使用下拉式選單)
* pop-up 視窗可以關閉的

### 4. D3 畫圖

* pop-up 視窗裡面使用 library [D3.js](https://d3js.org){:target="_blank"} 畫連接散點圖 [Connected scatterplot](https://www.d3-graph-gallery.com/connectedscatter.html){:target="_blank"} 顯示評價(x軸，0到5)和米其林星(y軸，0到3，推薦=0.5，無=0)的關係。


### 5. 中/英文頁面

* 有中/英文語言切換選擇。實際資料不需要翻譯，只需要有兩個 URL 分辨。
* 網頁版：右上方，使用語言切换按钮。
* 手機版：右上方有隱藏的三橫條線 hamburger menu 選單，選單裡面有語言切换按钮。

<br>

---

<br>

<a name="zh-cn"></a>

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


考题范围、分数计算，请参考**[全端测验样本]({{ site.link_sample_fullstackdev }})**。分数计算与考题会类似。

<br>

## 考题大纲

请开发一个可以使用，有前端的网站。

| 满分 | 网页功能 |
| --- | --- |
| 30 | 呈现讯息 |
| 30 | 搜寻功能 |
| 45 | 订位按钮与 pop-up 视窗 |
| 65 | D3 画图 |
| 30 | 中/英文页面 |

[测验分数评估]({{ site.baseurl }}/recruit/exam_rubric.html){: .btn#page-btn}

## 规则

1. **RWD.** Web 和 mobile browser 使用。
1. **必须使用 JavaScript.**
1. **JS 框架.** 您必须使用一个JS框架; 我们偏爱 React 或 Vue。如果需要，可以使用 Angular, Ember, Backbone, 或 Aurelia，但您需要有充分的理由选择它。不能使用 jquery。
1. **HTML 和 CSS.** 您必须证明对HTML和CSS的了解与熟悉。
	* 加分题：使用 preprocessors SCSS/Sass。
	* 加分题：我们鼓励您使用框架，譬如 Bootstrap。
1. ** RESTful.**
1. **有现代网页设计感.** 干净页面，字体、颜色容易读。

## 考题讲解

* 下载[csv档案](https://docs.google.com/spreadsheets/d/1OanzakC9Uuo6fLLLyKScTSWDH6twnPOrSN-uWvoTz-U/edit?usp=sharing){:target="_blank"}。
* 使用这个档案为需要显示的资料。

## 考题

请自由选择你想要开发的网页功能，没有先后次序。

### 1. 呈现讯息

* 在首页显示档案里面的资讯，表格的每一行是餐厅名字，使用者可以按/点，伸缩更多的餐厅资讯（展开、收起）。
* 展开资讯有订位按钮和有图示表示类型、米其林星、停车、外送、先缴订金、评价。
* 表格共有2页，可以前后去第一、二页。

### 2. 搜寻功能

* 网页最上方有搜寻功能，使用者可以输入的栏位与搜寻按钮：餐厅名字(输入时，会有下拉式的建议)、订位人数(使用下拉式选单)、日期(使用日历选单)、时间(使用下拉式选单)。 UI 请参考并尽量相似 [OpenTable](https://www.opentable.com/?lang=ja){:target="_blank"}

### 3. 订位按钮与 pop-up 视窗

* 展开餐厅资讯里，有订位按钮
* 订位按钮会有 pop-up 视窗
* pop-up 视窗是一个让使用者可以填写的表格：名字、电话(输入数字限制)、订位人数(使用下拉式选单)、日期(使用日历选单)、时间(使用下拉式选单)
* pop-up 视窗可以关闭的

### 4. D3 画图

* pop-up 视窗里面使用library [D3.js](https://d3js.org){:target="_blank"} 画连接散点图[Connected scatterplot](https://www.d3-graph- gallery.com/connectedscatter.html){:target="_blank"} 显示评价(x轴，0到5)和米其林星(y轴，0到3，推荐=0.5，无=0)的关系。


### 5. 中/英文页面

* 有中/英文语言切换选择。实际资料不需要翻译，只需要有两个 URL 分辨。
* 网页版：右上方，使用语言切换按钮。
* 手机版：右上方有隐藏的三横条线 hamburger menu 选单，选单里面有语言切换按钮。


