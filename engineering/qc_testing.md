---
layout: default
title: 品質管制及測試
description: Quality Control & Testing
---

## 一般原則

* 測試應該由與編寫代碼的人員不同的人員進行。
* 因此，測試是QC / QA工程師而非開發人員的責任。
* QC工程師將編寫自動測試，該測試將在每個請求請求進入主分支後運行。

<br>
<br>

## 測試金字塔

[**馬丁·福勒**]（https://martinfowler.com/bliki/TestPyramid.html）{：target =“ _blank”}

> 測試金字塔是一種思考方式，可以考慮使用各種自動測試來創建平衡的產品組合。關鍵點在於，通過GUI運行的高級**BroadStackTests**應該比高級**UnitTests**多得多。
>
> 在我的大部分職業生涯中，測試自動化意味著要通過用戶界面驅動應用程序的測試。此類工具通常會提供便利來記錄與應用程序的交互，然後允許您回放該交互，並檢查應用程序是否返回了相同的結果。最初這種方法行之有效。記錄測試很容易，並且測試人員可以在不了解編程的情況下進行記錄。
>
> 但是這種方法很快就會遇到麻煩，變成了“冰淇淋蛋筒”。像這樣通過UI進行測試很慢，從而增加了構建時間。通常，它需要安裝測試自動化軟件的許可證，這意味著只能在特定計算機上完成。通常，這些腳本無法輕鬆地在“無頭”模式下運行，並且無法通過腳本進行監視，以將其置於適當的部署管道中。

### 單元測試

單元測試是在命名及其含義上得到更廣泛接受的測試類別。它們是源代碼附帶的測試，可以直接訪問它們。通常，它們是通過**Unit framework**或類似的庫執行的。這些測試直接在源代碼上運行，並具有所有內容的完整視圖。測試了單個類/方法/功能（或該特定業務功能的最小可能工作單元），並且對其他任何事物進行了模擬/存根。

### 集成測試

集成測試（也稱為服務測試，甚至是組件測試）專注於整個組件。組件可以是一組類/方法/函數，一個模塊，一個子系統甚至是應用程序本身。他們通過傳遞輸入數據並檢查其產生的輸出數據來檢查組件。通常，首先需要某種部署/引導/設置。可以完全模擬，替換外部系統（例如，使用內存數據庫而不是真實的數據庫），或者可以根據業務情況使用實際的外部依賴關係。與單元測試相比，他們可能需要更專業的工具來準備測試環境或進行交互/驗證。

第二類遭受模糊的定義，有關測試的大多數命名爭議從此處開始。集成測試的“範圍”也極富爭議，尤其是訪問應用程序的性質（黑盒或白盒測試以及是否允許模擬）。

作為基本經驗法則

* 測試使用數據庫
* 測試使用網絡調用另一個組件/應用程序
* 測試使用外部系統（例如隊列或郵件服務器）
* 測試讀取/寫入文件或執行其他I / O
* 測試不依賴源代碼，而是使用應用程序的已部署二進製文件

…那麼這是一個集成測試，而不是一個單元測試。

有了命名方式，我們就可以進入列表了。反模式的順序大致遵循它們在野外時的外觀。頭等問題經常出現。

### 端到端（E2E）測試

即使使用單元測試和集成測試，您可能仍將需要少量的端到端測試來驗證整個系統。為了在所有三種測試類型之間找到適當的平衡，最好使用的視覺輔助是測試金字塔。

您的大部分測試都是金字塔底部的單元測試。當您向上移動金字塔時，測試會變大，但同時測試的數量（金字塔的寬度）會變小。

作為一個很好的初步猜測，Google通常會建議採用70/20/10的比例：70％的單元測試，20％的集成測試和10％的端到端測試。每個團隊的確切組合會有所不同，但通常，它應保持金字塔形狀。嘗試避免使用這些反模式：

* **倒金字塔/冰淇淋錐。**團隊主要依靠端到端測試，很少使用集成測試，甚至更少的單元測試。
* **沙漏。**團隊從大量的單元測試開始，然後使用端到端測試，應該使用集成測試。沙漏在底部有許多單元測試，在頂部有許多端到端測試，而在中間則沒有集成測試。

就像常規金字塔往往是現實生活中最穩定的結構一樣，測試金字塔也往往是最穩定的測試策略。

<br>
<br>

## 軟件測試反模式

首先，請閱讀[**Testing Anti-Patterns**](http://blog.codepipes.com/testing/software-testing-antipatterns.html){:target="_blank"}上的出色資源。

1. 進行單元測試而不進行集成測試
1. 進行集成測試而不進行單元測試
1. 測試類型錯誤
1. 測試錯誤的功能
1. 測試內部實施
1. 過度關注測試範圍
1. 具有片狀或緩慢的測試
1. 手動運行測試
1. 將測試代碼視為二等公民
1. 不將生產錯誤轉換為測試
1. 將測試驅動設計（TDD）視為一種宗教
1. 編寫測試而不先閱讀文檔
1. 出於無知而使不良聲譽受到考驗

<br>

---

<br>

## General Principles

* Testing should be done by a different person than the one who wrote the code.
* Therefore, testing is the responsiblity of QC / QA Engineers, and not the developers.
* QC Engineers will write automated tests that run after each pull request into the main branch.

<br>
<br>

## Test Pyramid

[**Martin Fowler**](https://martinfowler.com/bliki/TestPyramid.html){:target="_blank"}

> The test pyramid is a way of thinking about different kinds of automated tests should be used to create a balanced portfolio. Its essential point is that you should have many more low-level **UnitTests** than high level **BroadStackTests** running through a GUI.
>
> For much of my career test automation meant tests that drove an application through its user-interface. Such tools would often provide the facility to record an interaction with the application and then allow you to play back that interaction, checking that the application returned the same results. Such an approach works well initially. It's easy to record tests, and the tests can be recorded by people with no knowledge of programming.
> 
> But this kind of approach quickly runs into trouble, becoming an **ice-cream cone**. Testing through the UI like this is slow, increasing build times. Often it requires installed licences for the test automation software, which means it can only be done on particular machines. Usually these cannot easily be run in a "headless" mode, monitored by scripts to put in a proper deployment pipeline.

### Unit Tests

Unit tests are the category of tests that have wider acceptance regarding the naming and what they mean. They are the tests that accompany the source code and have direct access to it. Usually they are executed with an **Unit framework** or similar library. These tests work directly on the source code and have full view of everything. A single class/method/function is tested (or whatever is the smallest possible working unit for that particular business feature) and anything else is mocked/stubbed.

### Integration Tests

Integration tests (also called service tests, or even component tests) focus on a whole component. A component can be a set of classes/methods/functions, a module, a subsystem or even the application itself. They examine the component by passing input data and examinining the output data it produces. Usually some kind of deployment/bootstrap/setup is required first. External systems can be mocked completely, replaced (e.g. using an in-memory database instead of a real one), or the real external dependency might be used depending on the business case. Compared to unit tests they may require more specialized tools either for preparing the test environment, or for interacting/verifying it.

The second category suffers from a blurry definition and most naming controversies regarding testing start here. The “scope” for integration tests is also highly controversial and especially the nature of access to the application (black or white box testing and whether mocking is allowed or not).

As a basic rule of thumb if

* a test uses a database
* a test uses the network to call another component/application
* a test uses an external system (e.g. a queue or a mail server)
* a test reads/writes files or performs other I/O
* a test does not rely on the source code but instead it uses the deployed binary of the app

…then it is an integration test and not a unit test.

With the naming out of the way, we can dive into the list. The order of anti-patterns roughly follows their appearance in the wild. Frequent problems are gathered in the top positions.

### End-to-End (E2E) Tests

Even with both unit tests and integration tests, you probably still will want a small number of end-to-end tests to verify the system as a whole. To find the right balance between all three test types, the best visual aid to use is the testing pyramid.

The bulk of your tests are unit tests at the bottom of the pyramid. As you move up the pyramid, your tests gets larger, but at the same time the number of tests (the width of your pyramid) gets smaller.

As a good first guess, Google often suggests a 70/20/10 split: 70% unit tests, 20% integration tests, and 10% end-to-end tests. The exact mix will be different for each team, but in general, it should retain that pyramid shape. Try to avoid these anti-patterns:

* **Inverted pyramid/ice cream cone.** The team relies primarily on end-to-end tests, using few integration tests and even fewer unit tests. 
* **Hourglass.** The team starts with a lot of unit tests, then uses end-to-end tests where integration tests should be used. The hourglass has many unit tests at the bottom and many end-to-end tests at the top, but few integration tests in the middle.

Just like a regular pyramid tends to be the most stable structure in real life, the testing pyramid also tends to be the most stable testing strategy.

<br>
<br>

## Software Testing Anti-pattern

Read this excellent resource on [**Testing Anti-Patterns**](http://blog.codepipes.com/testing/software-testing-antipatterns.html){:target="_blank"} first.

1. Having unit tests without integration tests
1. Having integration tests without unit tests
1. Having the wrong kind of tests
1. Testing the wrong functionality
1. Testing internal implementation
1. Paying excessive attention to test coverage
1. Having flaky or slow tests
1. Running tests manually
1. Treating test code as a second class citizen
1. Not converting production bugs to tests
1. Treating Test Driven Design (TDD) as a religion
1. Writing tests without reading documentation first
1. Giving testing a bad reputation out of ignorance
