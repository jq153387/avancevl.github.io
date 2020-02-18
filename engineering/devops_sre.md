---
layout: default
title:  網頁可靠性
description: DevOps & Site Reliability
---

* 生產監控和故障排除是DevOps / SRE的責任。
* DevOps負責將問題和錯誤上報給相關工程師。

# 工具

主要工具類別包括：

* **版本控制：**跟踪軟件版本的工具，無論是手動還是自動。這意味著對版本進行編號，並跟踪配置和存在的任何環境相關性，例如數據庫的類型，品牌和版本。操作系統詳細信息；甚至是所需的物理或虛擬服務器的類型。此類別與變更管理工具有關。
* **構建和部署：**用於在整個DevOps流程中自動構建和部署軟件的工具，包括持續開發和持續集成。
* **功能和非功能測試：**提供自動測試的工具，包括上面列出的最佳實踐。測試工具應提供集成的單元，性能和安全性測試服務。目標應該是端到端自動化。
* **供應和變更管理：**用於提供部署軟件所需平台的工具，以及監視和記錄配置，數據或軟件發生的任何變更的工具。這些工具確保無論發生什麼情況都可以使系統恢復穩定狀態。

# 最佳做法

## 1.測試自動化

為了編寫高質量的代碼，開發人員需要定期測試軟件。 DevOps允許進行早期測試，這使開發人員有機會在軟件開發過程中而非過程的後期識別和解決問題。

與手動測試相比，自動測試可以更快地執行SDLC（軟件開發生命週期）。使用回歸測試和負載測試，可以將測試自動化應用於數據庫和網絡更改，中間件配置以及代碼開發。

可以通過執行各種活動來完成測試自動化，例如識別測試場景和案例，選擇正確的自動化工具集，設置適當的測試環境，運行測試案例以及分析結果。

## 2.集成配置管理

配置和變更管理是操作的組成部分。配置管理涉及跨網絡，服務器，應用程序，存儲和其他託管服務進行的系統範圍配置的自動化，監視，管理和維護。

集成的配置管理使開發團隊具有更廣闊的視野。它允許在軟件開發過程中利用現有服務，而不用花費時間和精力從頭開始重新發明新服務。

## 3.集成變更管理

變更管理是一個過程，在其中更改和重新定義配置以滿足動態情況和新要求的條件。在配置管理過程中，如果需要進行任何更改，那麼更改管理就會進入畫面。運營團隊就變更可能在更大的範圍內暴露出哪些機會和後果以及可能影響到哪些其他系統提供意見。

## 4.持續集成

這是DevOps軟件開發實踐，開發團隊會定期更新存儲庫中的代碼更改，然後運行自動構建和測試。持續集成實踐使開發人員可以更快，更頻繁地進行集成。 CI工具可幫助他們檢測新代碼和現有代碼中的集成挑戰，並僅在早期階段解決它們。因此，CI改善了團隊之間的協作，並最終構建了高質量的軟件產品。

## 5.持續交付

持續交付是DevOps的一種實踐，其中新開發的代碼由開發人員更新，通過自動和手動測試在不同階段由QA團隊進行測試，一旦案例通過所有測試，便進入生產。它使開發團隊可以在短週期內更快，更頻繁地構建，測試和發布應用程序。

它可以幫助組織增加交付數量，減少人工工作，將生產過程中發生故障的風險降到最低等。

## 6.持續部署

部署過程包含各種子過程，例如代碼創建，測試，版本控制，部署，後部署等。在連續部署過程中，一旦代碼成功通過了QA中的所有測試用例，代碼就會自動部署到生產環境中。 ，UAT和其他環境。許多執行連續部署的工具從階段到生產都需要最少的人工干預。

## 7.應用程序監視

無論是將其部署在雲還是本地數據中心上，應用程序基礎結構監視對於優化應用程序性能都至關重要。如果在發布過程中有bug擊中了應用程序，那麼它將變成失敗。因此，對於開發團隊和運營團隊而言，考慮主動監視並檢查應用程序的性能非常重要。各種工具可用於應用程序監視，這些工具提供了許多與應用程序，基礎架構，銷售，圖形，分析等相關的指標。

## 8.自動化儀表板

通過自動儀表板利用DevOps智能。它將提供數據以及每項操作的詳細見解和報告，例如運行的測試數量，測試的持續時間，測試失敗和成功的數量。它允許查看對數據庫和服務器所做的配置更改以及在系統中進行的部署。

儀表板充當集中式樞紐，使運營團隊能夠獲得實時數據見解，從而幫助他們選擇正確的自動化工具測試集。此外，還有各種日誌，圖形和度量標準，使操作團隊可以全面了解系統中發生的更改。

<br>

---

<br>

* Production monitoring and troubleshooting is the responsibility of DevOps / SRE.
* DevOps is responsible for escalating issues and bugs to the relevant engineer.

# Tools

The major tool categories include: 

* **Version control:** Tools that track software versions as they are released, whether manually or automatically. This means numbering versions, as well as tracking the configuration and any environmental dependencies that are present, such as the type, brand, and version of the database; the operating system details; and even the type of physical or virtual server that’s needed. This category is related to change management tools.
* **Build and deploy:** Tools that automate the building and deployment of software throughout the DevOps process, including continuous development and continuous integration.
* **Functional and non-functional testing:** Tools that provide automated testing, including best practices listed above. Testing tools should provide integrated unit, performance, and security testing services. The objective should be end-to-end automation.
* **Provisioning and change management:** Tools to provision the platforms needed for deployment of the software, as well as monitor and log any changes occurring to the configuration, the data, or the software. These tools ensure that you can get the system back to a stable state, no matter what occurs. 

# Best Practices

## 1. Test Automation
In order to compose quality code, developers need to test the software regularly. DevOps allows for early testing that gives developers an opportunity to identify and resolve the issue during software development rather than later in the process.

Automated testings allow for quicker execution of SDLC (Software Development Life Cycle) in comparison to manual testings. Test automation can be applied to the database and networking changes, middleware configurations, and code development using regression testing and load testing.

Test automation can be accomplished by performing varied activities such as identifying test scenarios and cases, choosing the right set of tools for automation, setting up an appropriate test environment, running test cases and analyzing results.  

## 2. Integrated Configuration Management
Configuration and change management are integral parts of the operations. Configuration management is about automation, monitoring, management and maintenance of system-wide configurations that take place across networks, servers, application, storage, and other managed services.

Integrated configuration management enables the development teams with a bigger picture. It allows to utilize the existing services during the software development rather than investing time and efforts in reinventing the new services from scratch.

## 3. Integrated Change Management
Change management is a process in which configurations are changed and redefined to meet the conditions of dynamic circumstances and new requirements. During the configuration management, if any changes are required then change management comes into the picture. The operations teams provide their inputs on what opportunities and consequences the change might expose at the wider level and what other systems could be impacted.  

## 4. Continuous Integration
It is a DevOps software development practice where the development team regularly updates the code changes in the repository after which the automated builds and tests run. Continuous Integration practices allow developers to carry out integrations sooner and frequently. Whereas CI tools help them to detect the integration challenges in new and existing code and solve them at the earlier phase only. Thus, CI improves collaborations amongst the teams and ultimately builds a high-quality software product.

## 5. Continuous Delivery
Continuous Delivery is a DevOps practice where the newly developed code is updated by developers, get tested by the QA team at the different stages by applying both automated and manual testings, and once the case passes all the testings, it gets into the production. It allows the development team to build, test and release the application faster and frequently, in short cycles.

It helps organizations to increase the number of deliveries, reduce manual works, minimize the risk of failure during production, and more.

## 6. Continuous Deployment
The deployment process contains varied sub-processes such as code creation, testing, versioning, deployment, post-deployment, etc. In the continuous deployment process, the code is automatically deployed in the production environment once it successfully passes all the test cases in QA, UAT, and other environments. A lot of tools available that perform continuous deployment start from staging to production with minimum human intervention.  

## 7. Application Monitoring
App infrastructure monitoring is very crucial to optimize the application performance, whether it is deployed on the cloud or local data center. If a bug hits the application during the release process, then it will be turned into the failure. So, it is very important for the development teams and operations teams to consider proactive monitoring and check the performance of the application. Various tools are available for application monitoring that offer a lot of metrics related to applications, infrastructure, sales, graphs, analytics, etc.

## 8. Automated Dashboards
Leverage the DevOps intelligence with the automated dashboard. It will provide the data along with detailed insights and reports of every operation such as the number of tests run, tests’ durations, the number of failure and success in testing. It allows to review configuration changes made to the database and server and deployments that have taken place across the system.  

The dashboard acts as a centralized hub that enables the operations team with real-time data insights which help them in selecting the right set of automation tools testings. Moreover, there are varied logs, graphs, and metrics that enable operations teams with a holistic view of changes happening in the system. 