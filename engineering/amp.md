---
layout: default
title: AMP前端架構
description: Accelerated Mobile Pages
---

## AMP主要概念理想

* **AMP HTML:** 簡化版的HTML讓網頁更快的呈現出來。
* **AMP Cache:** Google和Bing會先cache好AMP在他們的伺服器上，讓尋找結果更快顯示。
* 在手機環境page load速度會提高
* Google SEO排名會提高

## 如何在Next.js架構裡實作AMP

* 雖然Next.js是個React.js的架構，當你用AMP時你的網頁就不可能是client side React了，因為兩個網頁的理念是完全衝突的。
* 當你用Next.js來顯示AMP網頁，Next.js已經比較像server side templating engine，而不是React前端component了。
* Next.js提供兩種建立AMP網頁的方式。

* **Hybrid AMP** 每個Next.js會自動產出相對應的網頁
`pages/home.js`
```javascript
import { useAmp } from 'next/amp'

export const config = {
  amp: 'hybrid'
}

export default () => {
  const isAmp = useAmp()
  return (
    <div>
      <p>{isAmp ? 'Not AMP Home Page' : 'Home Page'}</p>
    </div>
   )
}
```
* **AMP-only** 只有AMP版本的網頁
`pages/index.js`
```javascript
import Nav from '../components/nav'
import { useAmp } from 'next/amp'

export const config = {
  amp: true
}
```

Although Next.js is usually thought of as a React framework, it's important to understand that when you use Next.js to serve AMP pages, you can no longer run React components client-side because React components are not valid AMP components. In other words, Next.js is no longer a React framework but rather a server-side templating engine for generating AMP pages.


## 線上資源

* [How to use AMP in Next.js](https://web.dev/how-to-use-amp-in-nextjs/){:target="_blank"}
* [What is Next.js and how you can build an AMP page with it?](https://dev.to/quickly_react/what-is-next-js-and-how-you-can-build-an-amp-page-with-it-4g12){:target="_blank"}