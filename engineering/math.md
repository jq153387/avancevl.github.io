---
layout: default
title: 數學公式前端
description: Math Latex
---

| 數學公式前端 | Katex |

## Katex

* Server-side rendering or rendering to a string
* To generate HTML on the server or to generate an HTML string of the rendered math, you can use 

```javascript
katex.renderToString:

var html = katex.renderToString("c = \\pm\\sqrt{a^2 + b^2}", {
    throwOnError: false
});
// '<span class="katex">...</span>'
```

* [Katex](https://katex.org/){:target="_blank"}
* [Katex Docs](https://katex.org/docs/api.html){:target="_blank"}


## MathJax

* You are correct that AMP doesn't support custom javascript.
* The AMP pages only allow third-party JavaScript but only in sandboxed iframes. By restricting them to iframes, they can’t block the execution of the main page. Even if they trigger multiple style re-calculations, their tiny iframes have very little DOM.
* [MathJax Docs](http://docs.mathjax.org/en/latest/){:target="_blank"}
* [SO: AMP support for Latex Maths](https://stackoverflow.com/questions/41095862/accelerated-mobile-pages-support-for-latex-maths){:target="_blank"}
* [How can we implement MathJax in AMP website](https://support.google.com/webmasters/thread/2334051?hl=en){:target="_blank"}
* [SO: How  can we implement MathJax in AMP website](https://stackoverflow.com/questions/55137996/how-can-we-implement-mathjax-in-amp-website){:target="_blank"}
* [Add support for MathML](https://github.com/ampproject/amphtml/issues/12800){:target="_blank"}


## MathML

* [Mathematical Markup Language](https://www.w3.org/Math/whatIsMathML.html){:target="_blank"}
* [`github: mathml.js`](https://github.com/ampproject/amphtml/blob/master/3p/mathml.js){:target="_blank"}
* [`amp-mathml`](https://amp.dev/documentation/components/amp-mathml/?referrer=ampproject.org){:target="_blank"}