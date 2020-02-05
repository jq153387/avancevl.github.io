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

## 支持AMP的React.js架構

| 架構 | HTML建立時刻 | 需要server? | 適合使用網頁 |
| --- | --- | --- | --- |
| Next.js | Real Time | 需要 | 比較複雜或多網頁時 |
| Gatsby.js | Build Time | 不需 | 比較小的網頁，blogs |

## 如何在Next.js架構裡實作AMP

* 雖然Next.js是個React.js的架構，當你用AMP時你的網頁就不可能是client side React了，因為兩個網頁的理念是完全衝突的。
* 當你用Next.js來顯示AMP網頁，Next.js已經比較像server side templating engine，而不是React前端component了。
* Next.js提供兩種建立AMP網頁的方式。

### Hybrid AMP

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

### AMP-only

`pages/index.js`

```javascript
import Nav from '../components/nav'
import { useAmp } from 'next/amp'

export const config = {
  amp: true
}
```

## 線上資源

* [Create AMP Pages](https://nextjs.org/learn/excel/amp){:target="_blank"}
* [How to use AMP in Next.js](https://web.dev/how-to-use-amp-in-nextjs/){:target="_blank"}
* [What is Next.js and how you can build an AMP page with it?](https://dev.to/quickly_react/what-is-next-js-and-how-you-can-build-an-amp-page-with-it-4g12){:target="_blank"}
* [Gatsby vs Next.JS](https://dev.to/jameesy/gatsby-vs-next-js-what-why-and-when-4al5){:target="_blank"}