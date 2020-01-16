---
layout: default
title: 程式代碼規範
description: Coding Standards
---

# 程式代碼規範的重要性

* **會加強工程師品質。**習慣寫好程式格式，規範一致會讓你變成更好的軟體工程師。
* **當程式代碼容易閱讀開發時間會自然縮短。**比較容易讀懂程式在做什麼。
* **提高程式效能。**JavaScript有時後是個蠻奇怪的語言。代碼格式一致會讓效能提高。

<br>

# 代碼格式自動檢查工具

| 工具 | 用途 |
| --- | --- |
| Prettier | 完全幫你把代碼formatting弄一致 |
| ESLint | 代碼品質，自動找bug |
| Linting rule sets, plugins, and extensions | 決定代碼規範 |
| Git hooks | 自動化程式規範 |

## 第一步驟：和解Prettier和自動代碼格式

[Prettier GitHub Repo & Docs](https://github.com/prettier/prettier){:target="_blank"}

Prettier會依照指定的規範把你的代碼全部從新整合。當你安裝後就不用在考慮代碼規範了。安裝在package.json裡所以不用一直提醒團員安裝。

### 安裝
```
yarn add prettier --dev
```
建議針對專案安裝。

### 使用

用這行代碼來整合你的代碼格式。
```
prettier --single-quote --write "src/**/*.js"
```

## 第二步驟：使用Husky加Lint-Staged來自動化Prettier的Git Hooks

**Husky**用來吧githooks簡化，在代碼加入version control之前跑個subroutine。

**Lint-Staged**及Husky需要一起用。 會只跑在‘staged’或‘added’的Git branch。這樣prettier就不用每次跑你整個專案的代碼，只需要跑有更改過或新加的檔案。

### 安裝
```
yarn add husky lint-staged --dev
```

加precommit script到你的package.json。
```
"scripts": {
    "precommit": "lint-staged"
},
```
要確保lint-stage script也加入你的package.json。
```
{
  "scripts": {
    "precommit": "lint-staged"
  },
  "lint-staged": {
    "*.js": [
      "prettier --write",
      "git add"
    ]
  }
}
```

## 第三步驟：Eslint代碼警察

Linting是可以結合任何程式語言的小工具。可以避免工程師團隊行程不好的習慣。

ESLint is a popular tool for javascript developers. One great advantage; it is highly configurable. Even though opinionated libraries can be easier, ESLint’s customizability enables it to play nice with others. If you aren’t familiar with ESLint there are a lot of resources out there and their website has some really great documentation.

### 安裝

First, install ESLint locally. Again, I don’t like installing it globally since I have to install all the plugins globally too. It also ensures the latest versions are being used.
```
yarn add eslint --dev
```

Integrate ESLint with your code editor. For VS Code install the ESLint Extension.

Follow the extension documentation. It will use your ESLint settings defined in your project to provide feedback when your code has errors. When looking for a configuration it looks first in your project, then globally.

Create the ‘.eslintrc.json’ to define the project’s eslint settings.
```
// run this command in the terminal:
./node_modules/.bin/eslint --init
// Or you can just add a .eslintrc.json to your project
//Note: you may also want to add a .eslintignore . It works just like a .gitignore
```

There are many preconfigured style guides that integrate with ESLint:
* [Airbnb Sytle Guide](https://github.com/airbnb/javascript){:target="_blank"}


## 第四步驟：Eslint和React.js的結合

The majority of my community likes React so this section is specific to it. Sorry Angular guys.

Since we only care about code-quality rules, we don’t need any of the robust configurations above. Lucky for us, Facebook created a set of rules without devoid of styling. The react-app configuration is hidden in the depths of Facebook’s create-react-app repository. Best part: it only enforces code quality. Prettier should marry this configuration.

Install the plugins & extensions
```
yarn add --dev eslint-config-react-app babel-eslint eslint-plugin-flowtype eslint-plugin-import eslint-plugin-jsx-a11y eslint-plugin-react
```
For information on each of these configurations, you can google them to see all the rules.
Adding the extentions and plugins to ‘.eslintrc.json’
```
{
  "extends": ["react-app", "plugin:jsx-a11y/recommended"],
  "plugins": ["jsx-a11y"]
}
```

## 第五步驟：Configure ESLint to play nice with Prettier

Since we have rules coming from ESLint and Prettier, we need to make sure that we don’t have rule conflicts. This is especially important if you want to use Airbnb or Standard styling.

eslint-config-prettier: Turns off all rules that are unnecessary or might conflict with prettier.
yarn add eslint-config-prettier --dev
Now add the plugins and rules to your .eslintrc:
```
{
  "extends": [
    "prettier",
    "prettier/flowtype",  // if you are using flow
    "prettier/react"
  ]
}
```

Check out the eslint-config-prettier documentation for more details.

## 第六步驟： Other personal configurations

Add the prettier ESLint plugin to see formatting errors。

eslint-plugin-prettier gives you the ability to see feedback in your code editor when styling is incorrect. It’s not important, but some people like to see that.
```
yarn add eslint-plugin-prettier --dev
```
Now add the plugins and rules to your .eslintrc:
```
// .eslinrc.json
{
  "plugins": [
    "prettier"
  ],
  "rules": {
    "prettier/prettier": "error"
  }
}
```
To further configure this see the eslint-plugin-prettier documentation

<br>

# 格式規範 Style Guides

## 基礎格式

| JavaScript | [Airbnb Sytle Guide](https://github.com/airbnb/javascript){:target="_blank"} |
| C++ | [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html){:target="_blank"} |
| Python | [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html){:target="_blank"} |


## 例外格式

* tab一定要用space取代。

<br>

---

<br>

# 代碼審核 Code Review

* Code reviews at done **BEFORE** the code is merged into main branch via a pull request.
* An engineer's direct manager should be added to **every pull request**.
* Code reviews are completed at the reviewer's own time.
* All reviewer's must approve before pull request can be approved.

<br>

# 代碼審核的重要性

* Committers are motivated to write better code knowing if someone will look at it.
* Learning and sharing knowledge on how to write better code.
* Consistency in design and coding style.
* Catching bugs, anti-patterns, and design flaws early.