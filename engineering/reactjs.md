---
layout: default
title: React.js 架構
description: React.js Framework
---

| Server Side Rendering架構 | **Next.js** ｜

## React - Server Side Rendering (SSR)

### Client Side Rendering (CRS)

* Google和Facebook News Feed看到的網頁完全沒有內容，只有JavaScript檔案

```html

<!DOCTYPE html>
<html>
  <head>
    <title>My SPA APP Title</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="text/javascript" src="/bundle.js"></script>
  </body>
</html>
```

### Server Side Rendering (SSR)

### 技術考量於目標

1. 第一次網頁下載速度要快，CSR會有延遲
1. 為了SEO考量，網頁資料需要能被Google Crawler/Indexer容易找到，資料不能藏在JavaScript裡
1. 當網頁被分享到social media時（Facebook, LinkedIn news feeds)，HTML需要直接有網頁的內容，不然會沒有preview
1. 應用SSR程式複雜度不能太嚴重，維持開發程式的簡易及速度

### 線上資源

* [React DOM Server](https://reactjs.org/docs/react-dom-server.html){:target="_blank"}
* [JavaScrip SEO: SSR vs CSR](https://medium.com/@benjburkholder/javascript-seo-server-side-rendering-vs-client-side-rendering-bc06b8ca2383){:target="_blank"}
* [SSR with React](https://medium.com/@swazza85/ssr-with-react-9cb197cfe380){:target="_blank"}
* [Server Side Rendering with React](https://flaviocopes.com/react-server-side-rendering/){:target="_blank"}
* [Server Side Rendering with React, Redux, and React-Router](https://itnext.io/server-side-rendering-with-react-redux-and-react-router-fa5b67d4965e){:target="_blank"}
* [GitHub: Rendertron](https://github.com/GoogleChrome/rendertron){:target="_blank"}

<br>

## React - PWD

### 線上資源

* [Build a Realtime PWA with React](https://medium.com/better-programming/build-a-realtime-pwa-with-react-99e7b0fd3270){:target="_blank"}
* [GitHub: Create React App](https://github.com/facebook/create-react-app){:target="_blank"}


<br>

## React - Firebase

### 線上資源

* [GitHub: React Starter Kit for Firebase](https://github.com/kriasoft/react-firebase-starter){:target="_blank"}

<br>

## React - Native

### 線上資源

* [Should you use React Native to build your startup's mobile app?](https://medium.com/snipe-gg/should-you-use-react-native-to-build-your-startups-mobile-app-c0baf9f4d9ad){:target="_blank"}
* [React Native at Airbnb](https://medium.com/airbnb-engineering/react-native-at-airbnb-f95aa460be1c){:target="_blank"}
* [Why Discord is Sticking with React Native](https://blog.discordapp.com/why-discord-is-sticking-with-react-native-ccc34be0d427){:target="_blank"}