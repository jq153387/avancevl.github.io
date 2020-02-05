---
layout: default
title: AMP前端架構
description: Accelerated Mobile Pages
---

# AMP主要概念理想

* **AMP HTML:**A A restricted form of HTML that makes certain optimizations mandatory and prohibits architectural patterns that lead to slowness. See How AMP works for a high-level overview of the optimizations and restrictions.
**AMP Cache:**A A content cache used by some search engines, such as Google and Bing, that uses prerendering to speed up page loads. See Why AMP Caches exist to learn more about the benefits and tradeoffs of the caches and How does my AMP page get cached? to understand how your AMP pages get into the caches.


How you can use AMP in Next.js #
There are two ways to use AMP in Next.js:

The Hybrid AMP approach lets you create an accompanying AMP version of any Next.js page.
The AMP-only approach lets you make AMP the only option for a page.
Although Next.js is usually thought of as a React framework, it's important to understand that when you use Next.js to serve AMP pages, you can no longer run React components client-side because React components are not valid AMP components. In other words, Next.js is no longer a React framework but rather a server-side templating engine for generating AMP pages.