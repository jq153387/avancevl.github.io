---
layout: default
title: 前端測驗樣本
description: Front-End Sample Exam
---


<a name="zh-tw"></a>

<br>

[立即申請]({{ site.job_form_url }}){: .btn#page-btn}{:target="_blank"}
[檢閱考試指示]({{ site.baseurl }}/recruit/webdev.html){: .btn#page-btn}
[測驗分數評估]({{ site.baseurl }}/recruit/exam_rubric.html){: .btn#page-btn}

## 考試

請實作依照設計圖**像素完美**桌面及手機前端介面。
* 必使用**React.js, Flexbox, 及React UI 零件架構。**
* 必使用static page方式（無後端）在**Firebase**或其他架構上架。

### 桌面介面

<img src='https://lh3.googleusercontent.com/SBQWfwg0cfPBcIyvuK1qAlIX3F3t25vj6uOVahV-E7Rhg-RTKJABufr4rYEHkLd3Cv35n3isUWyFwdEHMeIfsoQ3yDlKKqdhuWvSTz0JuAn3U92Y0nZ_7aC-_raJ9QdxmISoLb0GMw=w1417' />

### 手機介面

<img src='https://lh3.googleusercontent.com/d7JgqvyPNjQOZEZEoVyTMJcAHRnBTDIZDDJo9rjbIVU-dLiQ2SYOacqNqheAbNkK_A1DBHQS-7qNwkaAb4fvgUa-bx4pJcUOjS0lKGpcK0Dm32KjXLzy_M9yjVwkd1gopwESZau8iw=w308' />

## 需求規範

1. **RWD.** 桌面及手機Responsive Web Design。
1. 必使用**JavaScript.**
1. 必使用 **React.js.**
1. 必使用 **CSS Flexbox 
1. 必使用**React UI framework**，從以下賽選：
	1. Material UI
	1. Semantic UI
	1. React Bootstrap
	1. React Toolbox
	1. Elemental UI
1. **必使用static page方式（無後端）在雲端架構上架。**
	1. 請用雲端架構 Heroku, Firebase, ZEIT, 或 Netilfy 上架static page。
	1. 這不是後端測驗，所以網頁和使用者互動全在前端實作。

## 重要提醒

> * 我們並不期望你完整開發每個功能。重點不是要全部 “做完”，是要查看有嘗試部分的能力、進度，盡力而為就可以。
> * 請使用 GitHub/GitLab.
> * 這份線上測驗分數會決定您的職級與薪資範圍。每個網頁功能有分數。請必定要交卷。
> * 2.5小時到時：
>   * 有開發多少，就交卷多少，考試並沒有所謂的 “完成”。
>   * 請必定要上架，並提供網頁 URL.
>	* 請填寫測驗完成表格 [Exam Submission Form]({{ site.exam_submit_form_url }}).

## 考題大綱

1. 像素完美在一下狀態：
	1. 桌面（Chrome）
	1. 手機（Android, iOS）
	1. 沒設計圖的狀態
1. 效果
	1. Hover
	1. Selection
	1. Disable
1. 鍵盤及滑鼠動作

| 滿分 | 網頁功能 |
| --- | --- |
| 50 | 數據輸入格 |
| 50 | 圈圈表格及數據介面 |
| 60 | 選項介面（每種選項型20分） |
| 40 | 主頁及Hashtags |

[測驗分數評估]({{ site.baseurl }}/recruit/exam_rubric.html){: .btn#page-btn}

## 網頁功能

請以下表單選任網頁功能實作，不用照順序。

### 1. 數據輸入格

* 限制輸入數字 (0-9), 逗點 (.), 及符號 (/)
* 不行用左右鍵往前後
* 不行用滑鼠點輸入格
* 鍵盤自動專注在輸入格，不需點輸入格
* "Press Enter" 文字及 "Submit" 會在有輸入數字時出現

<img src='https://lh3.googleusercontent.com/ox5SLTTaUphHmgJiyjktWSEvtiw14pCxqL151hVq27BQbfuc2ur7X5B0UoFnIUwI6tGlxbKCD8WyGG1iszRx1h3JJBDDl9fFYEh2UXDIALI4JpIMmf24qqghg27Kp4hkt2Ed9qFUcQ=w386' />

<img src='https://lh3.googleusercontent.com/rB8z7QO1lzjB2QjQBmrjg1B9-hOkowQUVVwG-jHCGgqIWe-KFQ4dSkYWwYJvrZYOo9oPwr4Vd5PyW1oxF316LsNqys1Nw-Q8iXab-y5wBRoMthow3P_1ycTyt45RjouxjCUrH5QLTQ=w386' />

### 2. 圈圈表格及數據介面

* 桌面和手機介面像素完美
* 不能只是個畫面，需要跟著數據變動

#### 桌面介面

<img src='https://lh3.googleusercontent.com/zRIxNrIztI22WJYDs4EcrjnciyQ2ByIRVSu6R-JCpBCo0e2hT9_g1RwdcBbmyaSebQRUk06NscQ6waV0eiQZ1HTBjcVSg6Ildeo-sc9qhFLRnx1tKgK0u8tlKD0eyMMgMwNWp0cS4A=w260' />

#### 手機介面

<img src='https://lh3.googleusercontent.com/KgF-3-t90xkaH0efRhGiskSRs-lXZhbwQNtvL2GRiWiw76Os7hmvNe4T8kqSlbxNVDmqpUKDLPeODxVZk5P6yTqTiFYxqamU0GogSxARSAKaBy_lmLHnWNdgjw4oURMaxW5G4KBOtg=w358' />

### 3. 選項介面

* 桌面和手機介面像素完美
* 三種選項
	* 簡易選項
	* 多選項
	* 點勾選項

#### 簡易選項

<img src='https://lh3.googleusercontent.com/_Yq-Q8WnX2cV3y305Q4GbHNuugYC173fCTPixp3aigX7ZxKyf5ok1nRGoCQ1-ProqM2GNGr3VI0CyBTCkHCuSpie3yH8vGgY9AqfqRk6PL7Hx7fRf2QDpQoisxPgCQNwt5Jlzl3X4w=w288' />

<img src='https://lh3.googleusercontent.com/nclQ6N-I6LaATouvMOo2bFDGud5yWOteWi1uGUpWg-1rKdHo4yJGm5o-YiDERAMyi-Vm3ayJ48XavVloBfnKB7nInGjqN5ElQApx7f9e0dr3VrYusCoDLndZvHzzxikn29f6I3bqaw=w374' />

#### 多選項

<img src='https://lh3.googleusercontent.com/zeYaUx3W0Hb8yaiPLHyzTOI_ShGmEIQqTA_Q7b8hyGZ_bfeC8gSK4s6L1okbGhrFPf817zjp-RbRcDZzZ3p51Vv1QxUza9RGTDupaia0jRcepHtTUNAafjEXJBwhzKMnVC_az-nOAw=w370' />

<img src='https://lh3.googleusercontent.com/4YZ6BQyxTr0RiPlGIyASjeaO_M8B_Vv-pgTFn6yG2b_aGa8Fdvrwyru534ZnoeE_rG3Z5NPuZRKifDqvTYA51I0hkXYxO9Ga4VWjnB1uj8Z4R0jd-Ofha1no2LAaGXmmeutLMlcgJQ=w378' />

#### 點勾選項

<img src='https://lh3.googleusercontent.com/YhLAUXhAFGxs5GlJMv-HZB3i9Gji9TCU3RS8lxlrpKoGOyyBfT_xyEtM71a6hENCzCei1ZHsHSEtRWqLtnZsVgEOR-dFXQ1zmb9ysYYjsaKjuSsbpwagENtwmzcSiwvIXuc0Es2kSA=w379' />

<img src='https://lh3.googleusercontent.com/8HvHKaJr974UaC8OcbBfsL-VJGIELAvEmnGJBucCbLHK3kTvIdUXIErRK2yYn62YkVyC_k2dW-22w3SbyCM-hDXKNvQlntZzhw4MrlJqhrAXLfjGCR8qkJvOU6KLTz4cLiQizWp_Fw=w376' />

### 4. 主頁及Hashtags

* 桌面和手機介面像素完美

#### 桌面介面

<img src='https://lh3.googleusercontent.com/qwkODECKDvngf-i79qFqv83ecp5n2Bc0oYhJ2SWy1eaboJV8LE3GJTj-nr76GDRNwyKD0-Lob2K4r55SPHtIbbK3H3md-A_u1CoZ2aQ0cg7OTE55SaqrSblx_XZOJ-L4F5XuxsAKwQ=w443' />

#### 手機介面

<img src='https://lh3.googleusercontent.com/wcVF6A927hu43l1qtovepnmX-q7eQLjqwDfFSKnhqyl9mssrHnGKfdF3DzFk-HwJfybf1YVpSLqfk5SaYV6qtIMeivjkDiNiXJZltYqu3543svDGmjOHVaMw8R8KqAawvgm9oREf6A=w310' />


<br>

---

<a name="zh-cn"></a>

<br>

[立即申请]({{ site.job_form_url }}){: .btn#page-btn}{:target="_blank"}
[检阅考试指示]({{ site.baseurl }}/recruit/webdev.html){: .btn#page-btn}
[测验分数评估]({{ site.baseurl }}/recruit/exam_rubric.html){: .btn#page-btn}

## 考试

请实作依照设计图**像素完美**桌面及手机前端介面。
* 必使用**React.js, Flexbox, 及React UI 零件架构。 **
* 必使用static page方式（无后端）在**Firebase**或其他架构上架。


### 桌面介面

<img src='https://lh3.googleusercontent.com/SBQWfwg0cfPBcIyvuK1qAlIX3F3t25vj6uOVahV-E7Rhg-RTKJABufr4rYEHkLd3Cv35n3isUWyFwdEHMeIfsoQ3yDlKKqdhuWvSTz0JuAn3U92Y0nZ_7aC-_raJ9QdxmISoLb0GMw=w1417' />

### 手机介面

<img src='https://lh3.googleusercontent.com/d7JgqvyPNjQOZEZEoVyTMJcAHRnBTDIZDDJo9rjbIVU-dLiQ2SYOacqNqheAbNkK_A1DBHQS-7qNwkaAb4fvgUa-bx4pJcUOjS0lKGpcK0Dm32KjXLzy_M9yjVwkd1gopwESZau8iw=w308' />

## 需求规范

1. **RWD.** 桌面及手机Responsive Web Design。
1. 必使用**JavaScript.**
1. 必使用 **React.js.**
1. 必使用 **CSS Flexbox
1. 必使用**React UI framework**，从以下赛选：
1. Material UI
1. Semantic UI
1. React Bootstrap
1. React Toolbox
1. Elemental UI
1. **必使用static page方式（无后端）在云端架构上架。 **
1. 请用云端架构 Heroku, Firebase, ZEIT, 或 Netilfy 上架static page。
1. 这不是后端测验，所以网页和使用者互动全在前端实作。

## 重要提醒

> * 我们并不期望你完整开发每个功能。重点不是要全部 “做完”，是要查看有尝试部分的能力、进度，尽力而为就可以。
> * 请使用 GitHub/GitLab.
> * 这份线上测验分数会决定您的职级与薪资范围。每个网页功能有分数。请必定要交卷。
> * 2.5小时到时：
> * 有开发多少，就交卷多少，考试并没有所谓的 “完成”。
> * 请必定要上架，并提供网页 URL.
> * 请填写测验完成表格 [Exam Submission Form]({{ site.exam_submit_form_url }}).

## 考题大纲

1. 像素完美在一下状态：
1. 桌面（Chrome）
1. 手机（Android, iOS）
1. 没设计图的状态
1. 效果
1. Hover
1. Selection
1. Disable
1. 键盘及滑鼠动作

| 满分 | 网页功能 |
| --- | --- |
| 50 | 数据输入格 |
| 50 | 圈圈表格及数据介面 |
| 60 | 选项介面（每种选项型20分） |
| 40 | 主页及Hashtags |

[测验分数评估]({{ site.baseurl }}/recruit/exam_rubric.html){: .btn#page-btn}

## 网页功能

请以下表单选任网页功能实作，不用照顺序。

### 1. 数据输入格

* 限制输入数字 (0-9), 逗点 (.), 及符号 (/)
* 不行用左右键往前后
* 不行用滑鼠点输入格
* 键盘自动专注在输入格，不需点输入格
* "Press Enter" 文字及 "Submit" 会在有输入数字时出现

<img src='https://lh3.googleusercontent.com/ox5SLTTaUphHmgJiyjktWSEvtiw14pCxqL151hVq27BQbfuc2ur7X5B0UoFnIUwI6tGlxbKCD8WyGG1iszRx1h3JJBDDl9fFYEh2UXDIALI4JpIMmf24qqghg27Kp4hkt2Ed9qFUcQ=w386' />

<img src='https://lh3.googleusercontent.com/rB8z7QO1lzjB2QjQBmrjg1B9-hOkowQUVVwG-jHCGgqIWe-KFQ4dSkYWwYJvrZYOo9oPwr4Vd5PyW1oxF316LsNqys1Nw-Q8iXab-y5wBRoMthow3P_1ycTyt45RjouxjCUrH5QLTQ=w386' />

### 2. 圈圈表格及数据介面

* 桌面和手机介面像素完美
* 不能只是个画面，需要跟着数据变动

#### 桌面介面

<img src='https://lh3.googleusercontent.com/zRIxNrIztI22WJYDs4EcrjnciyQ2ByIRVSu6R-JCpBCo0e2hT9_g1RwdcBbmyaSebQRUk06NscQ6waV0eiQZ1HTBjcVSg6Ildeo-sc9qhFLRnx1tKgK0u8tlKD0eyMMgMwNWp0cS4A=w260' />

#### 手机介面

<img src='https://lh3.googleusercontent.com/KgF-3-t90xkaH0efRhGiskSRs-lXZhbwQNtvL2GRiWiw76Os7hmvNe4T8kqSlbxNVDmqpUKDLPeODxVZk5P6yTqTiFYxqamU0GogSxARSAKaBy_lmLHnWNdgjw4oURMaxW5G4KBOtg=w358' />

### 3. 选项介面

* 桌面和手机介面像素完美
* 三种选项
* 简易选项
* 多选项
* 点勾选项

#### 简易选项

<img src='https://lh3.googleusercontent.com/_Yq-Q8WnX2cV3y305Q4GbHNuugYC173fCTPixp3aigX7ZxKyf5ok1nRGoCQ1-ProqM2GNGr3VI0CyBTCkHCuSpie3yH8vGgY9AqfqRk6PL7Hx7fRf2QDpQoisxPgCQNwt5Jlzl3X4w=w288' />

<img src='https://lh3.googleusercontent.com/nclQ6N-I6LaATouvMOo2bFDGud5yWOteWi1uGUpWg-1rKdHo4yJGm5o-YiDERAMyi-Vm3ayJ48XavVloBfnKB7nInGjqN5ElQApx7f9e0dr3VrYusCoDLndZvHzzxikn29f6I3bqaw=w374' />

#### 多选项

<img src='https://lh3.googleusercontent.com/zeYaUx3W0Hb8yaiPLHyzTOI_ShGmEIQqTA_Q7b8hyGZ_bfeC8gSK4s6L1okbGhrFPf817zjp-RbRcDZzZ3p51Vv1QxUza9RGTDupaia0jRcepHtTUNAafjEXJBwhzKMnVC_az-nOAw=w370' />

<img src='https://lh3.googleusercontent.com/4YZ6BQyxTr0RiPlGIyASjeaO_M8B_Vv-pgTFn6yG2b_aGa8Fdvrwyru534ZnoeE_rG3Z5NPuZRKifDqvTYA51I0hkXYxO9Ga4VWjnB1uj8Z4R0jd-Ofha1no2LAaGXmmeutLMlcgJQ=w378' />

#### 点勾选项

<img src='https://lh3.googleusercontent.com/YhLAUXhAFGxs5GlJMv-HZB3i9Gji9TCU3RS8lxlrpKoGOyyBfT_xyEtM71a6hENCzCei1ZHsHSEtRWqLtnZsVgEOR-dFXQ1zmb9ysYYjsaKjuSsbpwagENtwmzcSiwvIXuc0Es2kSA=w379' />

<img src='https://lh3.googleusercontent.com/8HvHKaJr974UaC8OcbBfsL-VJGIELAvEmnGJBucCbLHK3kTvIdUXIErRK2yYn62YkVyC_k2dW-22w3SbyCM-hDXKNvQlntZzhw4MrlJqhrAXLfjGCR8qkJvOU6KLTz4cLiQizWp_Fw=w376' />

### 4. 主页及Hashtags

* 桌面和手机介面像素完美

#### 桌面介面

<img src='https://lh3.googleusercontent.com/qwkODECKDvngf-i79qFqv83ecp5n2Bc0oYhJ2SWy1eaboJV8LE3GJTj-nr76GDRNwyKD0-Lob2K4r55SPHtIbbK3H3md-A_u1CoZ2aQ0cg7OTE55SaqrSblx_XZOJ-L4F5XuxsAKwQ=w443' />

#### 手机介面

<img src='https://lh3.googleusercontent.com/wcVF6A927hu43l1qtovepnmX-q7eQLjqwDfFSKnhqyl9mssrHnGKfdF3DzFk-HwJfybf1YVpSLqfk5SaYV6qtIMeivjkDiNiXJZltYqu3543svDGmjOHVaMw8R8KqAawvgm9oREf6A=w310' />

<br>

---

<a name="en"></a>

<br>

[Apply Now]({{ site.job_form_url }}){: .btn#page-btn}{:target="_blank"}
[View Instructions]({{ site.baseurl }}/recruit/webdev.html){: .btn#page-btn}
[View Rubric]({{ site.baseurl }}/recruit/exam_rubric.html){: .btn#page-btn}

## Exam

Please build a **pixel-perfect** interactive desktop and mobile browser front-end of the following design mockups.
* Must use **React.js, Flexbox, and a React UI component library framework.**
* Host as static pages (no back-end) on **Firebase** or alternative free solution.

### Desktop UI

<img src='https://lh3.googleusercontent.com/SBQWfwg0cfPBcIyvuK1qAlIX3F3t25vj6uOVahV-E7Rhg-RTKJABufr4rYEHkLd3Cv35n3isUWyFwdEHMeIfsoQ3yDlKKqdhuWvSTz0JuAn3U92Y0nZ_7aC-_raJ9QdxmISoLb0GMw=w1417' />

### Mobile UI

<img src='https://lh3.googleusercontent.com/d7JgqvyPNjQOZEZEoVyTMJcAHRnBTDIZDDJo9rjbIVU-dLiQ2SYOacqNqheAbNkK_A1DBHQS-7qNwkaAb4fvgUa-bx4pJcUOjS0lKGpcK0Dm32KjXLzy_M9yjVwkd1gopwESZau8iw=w308' />

## Requirements

1. **RWD.** Responsive Web Design for both mobile and web.
1. Must use **JavaScript.**
1. Must use **React.js.**
1. Must use **CSS Flexbox 
1. Must use a **React UI framework** from this list:
	1. Material UI
	1. Semantic UI
	1. React Bootstrap
	1. React Toolbox
	1. Elemental UI
1. **Must host your site as a live static page.**
	1. Please use a free hosting service like Heroku, Firebase, ZEIT, or Netilfy to host your site as a live static page.
	1. This is a not a back-end exam. The web page interactions should all be client side.

## Reminders

> * We'd rather you do a few features well, rather than all the features poorly.
> * Please be sure to upload code to GitHub/GitLab.
> * At the 2.5-hour mark:
>   * Please submit however much you've completed, regardless of whether you've finished or not.
>   * Make sure your site is live, and submit URL.
>	* Make sure to complete [Exam Submission Form]({{ site.exam_submit_form_url }}).

## Features Rubric

1. Pixel perfect on:
	1. Desktop (Chrome)
	1. Mobile (Android, iOS)
	1. Fill in gaps not in the design mockups in a polished manner
1. Effects
	1. Hover
	1. Selection
	1. Disable
1. Keyboard and mouse events

| Score | Feature |
| --- | --- |
| 50 | Numbers Entry Box |
| 50 | Radial Chart and Stats Pane |
| 60 | Search Filters and Dropdown Menu (20 pts per type of selector) |
| 40 | Main Pane and Hashtags |

[View Exam Rubric]({{ site.baseurl }}/recruit/exam_rubric.html){: .btn#page-btn}

## Features List

Choose any of the following features to implement. There are no required ordering.

### 1. Numbers Entry Box

* Only numbers (0-9), period (.), and backslash (/) allowed in the numbers box.
* Right and left arrows disable for numbers box.
* Clicking disabled for numbers box.
* Keyboard is automatically in focus on the numbers box on page load. No need to click on numbers box to bring it in focus.
* "Press Enter" text and "Submit" button becomes enabled only when numbers are entered into numbers box.

<img src='https://lh3.googleusercontent.com/ox5SLTTaUphHmgJiyjktWSEvtiw14pCxqL151hVq27BQbfuc2ur7X5B0UoFnIUwI6tGlxbKCD8WyGG1iszRx1h3JJBDDl9fFYEh2UXDIALI4JpIMmf24qqghg27Kp4hkt2Ed9qFUcQ=w386' />

<img src='https://lh3.googleusercontent.com/rB8z7QO1lzjB2QjQBmrjg1B9-hOkowQUVVwG-jHCGgqIWe-KFQ4dSkYWwYJvrZYOo9oPwr4Vd5PyW1oxF316LsNqys1Nw-Q8iXab-y5wBRoMthow3P_1ycTyt45RjouxjCUrH5QLTQ=w386' />

### 2. Radial Chart and Stats Pane

* Pixel perfect desktop and mobile
* Not a static image, but real chart that could update if page is connected to server side.

#### Desktop UI

<img src='https://lh3.googleusercontent.com/zRIxNrIztI22WJYDs4EcrjnciyQ2ByIRVSu6R-JCpBCo0e2hT9_g1RwdcBbmyaSebQRUk06NscQ6waV0eiQZ1HTBjcVSg6Ildeo-sc9qhFLRnx1tKgK0u8tlKD0eyMMgMwNWp0cS4A=w260' />

#### Mobile UI

<img src='https://lh3.googleusercontent.com/KgF-3-t90xkaH0efRhGiskSRs-lXZhbwQNtvL2GRiWiw76Os7hmvNe4T8kqSlbxNVDmqpUKDLPeODxVZk5P6yTqTiFYxqamU0GogSxARSAKaBy_lmLHnWNdgjw4oURMaxW5G4KBOtg=w358' />

### 3. Search Filters and Dropdown Menu

* Pixel perfect desktop and mobile
* 3 types of filters
	* Simple Selector
	* Multiple Selector
	* Checkboxes

#### Simple Selector

<img src='https://lh3.googleusercontent.com/_Yq-Q8WnX2cV3y305Q4GbHNuugYC173fCTPixp3aigX7ZxKyf5ok1nRGoCQ1-ProqM2GNGr3VI0CyBTCkHCuSpie3yH8vGgY9AqfqRk6PL7Hx7fRf2QDpQoisxPgCQNwt5Jlzl3X4w=w288' />

<img src='https://lh3.googleusercontent.com/nclQ6N-I6LaATouvMOo2bFDGud5yWOteWi1uGUpWg-1rKdHo4yJGm5o-YiDERAMyi-Vm3ayJ48XavVloBfnKB7nInGjqN5ElQApx7f9e0dr3VrYusCoDLndZvHzzxikn29f6I3bqaw=w374' />

#### Multiple Selector

<img src='https://lh3.googleusercontent.com/zeYaUx3W0Hb8yaiPLHyzTOI_ShGmEIQqTA_Q7b8hyGZ_bfeC8gSK4s6L1okbGhrFPf817zjp-RbRcDZzZ3p51Vv1QxUza9RGTDupaia0jRcepHtTUNAafjEXJBwhzKMnVC_az-nOAw=w370' />

<img src='https://lh3.googleusercontent.com/4YZ6BQyxTr0RiPlGIyASjeaO_M8B_Vv-pgTFn6yG2b_aGa8Fdvrwyru534ZnoeE_rG3Z5NPuZRKifDqvTYA51I0hkXYxO9Ga4VWjnB1uj8Z4R0jd-Ofha1no2LAaGXmmeutLMlcgJQ=w378' />

#### Checkbox Selector

<img src='https://lh3.googleusercontent.com/YhLAUXhAFGxs5GlJMv-HZB3i9Gji9TCU3RS8lxlrpKoGOyyBfT_xyEtM71a6hENCzCei1ZHsHSEtRWqLtnZsVgEOR-dFXQ1zmb9ysYYjsaKjuSsbpwagENtwmzcSiwvIXuc0Es2kSA=w379' />

<img src='https://lh3.googleusercontent.com/8HvHKaJr974UaC8OcbBfsL-VJGIELAvEmnGJBucCbLHK3kTvIdUXIErRK2yYn62YkVyC_k2dW-22w3SbyCM-hDXKNvQlntZzhw4MrlJqhrAXLfjGCR8qkJvOU6KLTz4cLiQizWp_Fw=w376' />

### 4. Main Pane and Hashtags

* Pixel perfect desktop and mobile

#### Destkop UI

<img src='https://lh3.googleusercontent.com/qwkODECKDvngf-i79qFqv83ecp5n2Bc0oYhJ2SWy1eaboJV8LE3GJTj-nr76GDRNwyKD0-Lob2K4r55SPHtIbbK3H3md-A_u1CoZ2aQ0cg7OTE55SaqrSblx_XZOJ-L4F5XuxsAKwQ=w443' />

#### Mobile UI

<img src='https://lh3.googleusercontent.com/wcVF6A927hu43l1qtovepnmX-q7eQLjqwDfFSKnhqyl9mssrHnGKfdF3DzFk-HwJfybf1YVpSLqfk5SaYV6qtIMeivjkDiNiXJZltYqu3543svDGmjOHVaMw8R8KqAawvgm9oREf6A=w310' />


<br>