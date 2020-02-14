---
layout: default
title: 資料庫架構
description: Database-as-a-Service
---

| Database-as-a-Service架構 | **Cloud Firestore** |

## Firebase - Cloud Firestore

### 比較好的讀取資料

While the Realtime Database is just a giant JSON tree, Cloud Firestore is a little more structured. All your data consists of documents (which are basically key-value stores) and collections (which are collections of documents). Documents will also frequently point to subcollections, which contain other documents, which themselves can contain other documents, and so on.

### 比較有結構的資料

This structured data helps you out in two ways. First, all queries are shallow, meaning that you can request a document without grabbing all the data underneath. This means you can keep your data stored hierarchically in a way that makes more sense to you without having to worry about keeping your database shallow. Second, you have more powerful queries. For instance, you can now query across multiple fields without having to create those "combo" fields that combine (and denormalize) data from other parts of your database. In some cases, Cloud Firestore will just run those queries directly, and in other cases, it will automatically create and maintain indexes for you.

### 比較強的擴充性能

Cloud Firestore will be able to scale better than the Realtime Database. It's important to note that your queries scale to the size of your result set, not your data set. So searching will remain fast no matter how large your data set might become.

### 比較容易手動取資料

Like the Realtime Database, you can set up listeners in Cloud Firestore to stream in changes in real-time. But if you don't want that kind of behavior, and just want a simple "fetch my data" call, Cloud Firestore has that as well, and it's built in as a primary use case. (They're much better than the once calls in Realtime Database-land)

### 資源多地區

This basically means more reliability, as your data is shared across multiple data centers at once. But you still have strong consistency, meaning you can always make a query and be assured that you're getting the latest version of your data.

### 不同的計價方式

While the Realtime Database primarily charges based on storage or network bandwidth, Cloud Firestore primarily charges based on the number of operations you perform. Will this be better, or worse? It depends on your app.

For powering a news app, turn-based multiplayer game, or something like your own version of Stack Overflow, Cloud Firestore will probably look pretty favorable from a pricing standpoint. For something like a real-time group drawing app where you're sending across multiple updates a second to multiple people, it probably will be more expensive than the Realtime Database.

### 線上資源

* [Cloud Firestore Data Model](https://firebase.google.com/docs/firestore/data-model){:target="_blank"}

<br>

## Firebase - Realtime Database

1. That whole "it'll probably be cheaper for apps that make lots of frequent updates"
1. It's been around for a long time and has been battle tested by thousands of apps (Cloud Firestore is still in beta)
1. It's got better latency and when you need something with reliably low latency for a real-timey feel, the Realtime Database might work better.

<br>

## 線上資源

* [SO: What's the difference between Cloud Firestore and the Firebase Realtime Database?](https://stackoverflow.com/questions/46549766/whats-the-difference-between-cloud-firestore-and-the-firebase-realtime-database){:target="_blank"}
* [Realtime Database vs. Cloud Firestore — Which Database is Suitable for your Mobile App](https://medium.com/datadriveninvestor/realtime-database-vs-cloud-firestore-which-database-is-suitable-for-your-mobile-app-87e11b56f50f){:target="_blank"}
* [Firebase Cloud Firestore v/s Firebase Realtime Database](https://medium.com/@beingrahul/firebase-cloud-firestore-v-s-firebase-realtime-database-931d4265d4b0){:target="_blank"}
* [Choose a Database: Cloud Firestore or Realtime Database](https://firebase.google.com/docs/database/rtdb-vs-firestore){:target="_blank"}