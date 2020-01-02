---
layout: default
title: 測驗樣本
description: Sample Exam
---

## 考試指示 

請檢閱[考試指示]({{ site.baseurl }}/recruit/webdev.html)。重要提醒：

* 我們並不期望你完整開發每個功能。重點不是要全部 “做完”，是要查看有嘗試部分的能力、進度。盡力而為就可以
* 請使用 GitHub/GitLab
* 請必定要上架，並提供 URL
* 這份線上測驗分數會決定您的職級與薪資範圍。每個網頁功能有分數。請必定要交卷
* 2.5小時到時，請：
  * 請必定要上架，並提供 URL
  * 並填寫[問卷](https://forms.gle/yJsvL3zyHJLWasQM8){:target="_blank"}
  * 有開發多少，就交卷多少，考試並沒有所謂的 “完成”

## 考題大綱

請開發一個可以使用，有前、後端的網站：
* 這是一個讓使用者可以搜尋有在營業餐廳的網頁：
  * 顯示現在有在營業的餐廳 - 下方提供.csv檔 (40分)
  * 使用者可以搜尋有在營業的餐廳 (60分)
  * Google OAuth 登記帳戶 (50分)
* 也有一個後台管理員系統 (50分)
  * 管理：餐廳資訊

## 考題細節：網頁功能
請自由選擇你想要開發的功能，沒有先後次序**（照片是參考，不是指示）：**

1. 表格顯示：網頁首頁顯示現在目前所有在營業的餐廳 (40分)
  1. 下載[**csv檔案**](https://docs.google.com/spreadsheets/d/1OanzakC9Uuo6fLLLyKScTSWDH6twnPOrSN-uWvoTz-U/edit?usp=sharing){:target="_blank"}（有餐廳名字，台北營業時間）(用您的Gmail帳號登入下載）
  1. 使用使用者的時間查看 “此刻現在時間”（手機時間為準）
  1. 網頁表格只要顯示現在有開的餐廳
  1. 注意不同使用者的手機時間、時區
  1. 這也是您要開發網頁的首頁。使用者到您的網頁首頁，就要能看到這個表格：只顯示現在此刻時間有在營業的餐廳名字清單

1. 搜尋功能：使用者可以用營業時段去搜尋有營業的餐廳 (60分)
  1. 使用者可以輸入天、時間，查看搜尋的時段有在營業的餐廳

    1. 搜尋結果是表格：顯示有在指定搜尋時段內，有營業的餐廳和餐廳營業時間（台北時間）

    1. 加分題: 用日曆 UI 讓 user 點選

1. 後端管理員控制台 (50分)
  1. 管理台有權限可以管理使用者和餐廳資訊  (15分)

    1. 設立一個管理員帳號
      1. Login 管理台帳戶 : admin
      1. Password 管理台密碼 : admin

  1. 管理餐廳資訊 (35分)
    1. 顯示所有DB裡面的餐廳
    1. 加新的餐廳與營業時間
    1. 刪除餐廳

1. Google OAuth 使用者登記帳戶功能 (50分)
  1. 使用 Google OAuth API 帳戶登入連結
  1. 新的使用者可以登記帳戶
  1. 有帳戶的使用者可登入。我們會以新使用者的身分測試。

<br>

---

<br>

## Instructions

See [instructions here]({{ site.baseurl }}/recruit/webdev.html). Important reminders:

* The goal is NOT for you to complete all features, or any feature. The goal is to see how far you get.
* Please use GitHub / GitLab as your code repo.
* Please run your site and provide us with URL **regardless of whether you've completed the exam or not.**
* After 2.5 hours,
  * Please launch live site, regardless of the current state
  * Complete the following [survey](https://forms.gle/yJsvL3zyHJLWasQM8){:target="_blank"}
  * The goal is not to "finish", only to assess your ability