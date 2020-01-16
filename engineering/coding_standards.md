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

Prettier is an opinionated code formatter that will reprint your entire codebase so it conforms to your styling preferences. Once installed, you don’t ever have to think about styling again. The best part is it just works! You can push a button and all your code instantly looks professional. The logic lives in your package.json so no hounding teammates to install linters and githooks! Woohoo!! Lets get to it:

### 安裝
```
yarn add prettier --dev
```
Personally, I wouldn’t install it globally. It makes more sense to add it where you need it. Add it on a per project basis.

### 使用

Once installed an NPM script can be created to use the CLI. Here is a very basic script that formats your code, with a single rule change:
```
prettier --single-quote --write "src/**/*.js"
```

## 第二步驟：使用Husky加Lint-Staged來自動化Prettier的Git Hooks

**Husky** simplifies githooks, running a subroutine before adding to version control.

**Lint-Staged** and Husky go together like peas and carrots. It creates a script run against files that are ‘staged’ or ‘added’ in Git. Now prettier doesn’t need to parse your entire codebase; only the files that have changed.

### 安裝
```
yarn add husky lint-staged --dev
```

Add the precommit script to your package.json.
```
"scripts": {
    "precommit": "lint-staged"
},
```
The lint-stage script needs to be declared in your package.json. I left the precommit script in the example below to see the depth of the “lint-staged” script and how they work together.
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
Note: There may be some formatting rules that you may want to change. For instance, I like single quotes and trailing commas after all my object properties. If you want to get weird, the prettier docs list all the possible options to add to your script.

## 第三步驟：Eslint代碼警察

Linting is a vital tool in any programming language. When learning to code, it can prevent bad habits from forming.

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


## 第四步驟：Configuring ESLint to bend to our will (with React)

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