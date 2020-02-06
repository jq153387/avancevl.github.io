---
layout: default
title: 桌面程式架構
description: Desktop App Stack
---

| 多桌面程式架構 | **Electron** |


## 多桌面程式架構 Cross Platform - Electron

* [Slack: Building Hybrid Applications with Electron](https://slack.engineering/building-hybrid-applications-with-electron-dc67686de5fb){:target="_blank"}
* [Learn to build your own desktop chat app with React and Electron](https://www.freecodecamp.org/news/build-a-desktop-chat-app-with-react-electron-and-chatkit-744d168e6f2f/){:target="_blank"}


#### Node.js跟OS如何連結

* [Node.js C++ Addons](https://nodejs.org/api/addons.html){:target="_blank"}
	* Addons are dynamically-linked shared objects written in C++. The require() function can load Addons as ordinary Node.js modules. Addons provide an interface between JavaScript and C/C++ libraries.
	* There are three options for implementing Addons:
		* [N-API](https://nodejs.org/api/n-api.html){:target="_blank"}
		* [V8](https://v8docs.nodesource.com/){:target="_blank"}
		* [libuv](https://github.com/libuv/libuv){:target="_blank"}
		* `node::ObjectWrap` class

<br>

---

<br>

## Windows

* [Using Native Windows Features from Electron](https://felixrieseberg.com/using-native-windows-features-from-electron/){:target="_blank"}
	* Calling Windows with Electron's APIs
	* Native Node Addons (without C++)
	* Native Node Addons (with C++)
* [SO: Why is it said that WinRT replaces the  Windows API](https://stackoverflow.com/questions/31273757/why-is-it-said-that-winrt-replaces-the-windows-api){:target="_blank"}


### Windows Native API
* [MS Docs: Choose your app platform](https://docs.microsoft.com/en-us/windows/apps/desktop/choose-your-platform#uwp){:target="_blank"}
	* Universal Windows Platform (UWMP)
	* WPF (.NET)
	* Windows Form (.NET)
	* Win32
* [MS Docs: `GetActiveWindow` function](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getactivewindow){:target="_blank"}
	* [SO: Get Active Window of .net application](https://stackoverflow.com/questions/12019524/get-active-window-of-net-application){:target="_blank"}
* [MS Docs: `GetForegroundWindow` function](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getforegroundwindow){:target="_blank"}
* [MS Docs: `GetWindowThreadProcessId` function](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowthreadprocessid){:target="_blank"}
* [MS Doc: Platform Invoke (P/Invoke)](https://docs.microsoft.com/en-us/dotnet/standard/native-interop/pinvoke){:target="_blank"}
* [Getting the Active Process](http://www.blackwasp.co.uk/GetActiveProcess.aspx){:target="_blank"}
	* When developing software that monitors running processes, it can be useful to obtain details of the currently active application. The .NET framework does not provide methods to permit this so Platform Invocation Services (P/Invoke) must be used.
	* When using Microsoft Windows, there can only be one active, or foreground, window. This is the window that can receive input from the user and whose owning thread has a slightly higher priority than other open windows. In some situations it can be useful to identify the active process that owns this window.
	* The .NET framework provides a class, named "Process", that allows you to examine the details of a running process. However, this class cannot be used to identify the program that is currently in use. In order to identify the foreground window and obtain a Process object linked to it, you must use Platform Invocation Services (P/Invoke) to call functions from the Windows API.
* [SO: How to track WinRT applications (in Win32 it was simple)?](https://stackoverflow.com/questions/13561975/how-to-track-winrt-applications-in-win32-it-was-simple){:target="_blank"}
	* `GetForegroundWindow`
	* `GetWindowThreadProcessId`
	* You see, in WinRT, your application is the top-most application. And when your app is not the top-most application then your threads are suspended and the kernel will not schedule any more operations for your app. End of story.
	* This means what you are wanting to accomplish cannot be done in WinRT. You are thinking more like a resident app or a service with access to the desktop. Those apps have two advantages. 1) they are always running. And, 2) they have the API to do what you are wanting.
	* WinRT intentionally puts apps in a sandbox so that the user's experience, performance and battery life are protected. Your scenario and scores more like yours underscore the continuing need for desktop apps. (as long as there is a continuing need for those types of apps. 



### Windows Node API

* 可以寫C++也可以不寫
* [npm: win32-api](https://www.npmjs.com/package/win32-api){:target="_blank"}
* [npm: nodert-win10](https://www.npmjs.com/~nodert-win10){:target="_blank"}
* [github: NodeRT](https://github.com/NodeRT/NodeRT){:target="_blank"}


### Windows Electron

* Electron有內建JavaScript API呼叫Windows功能
* [Slack: Introducing Electron to the Windows Runtime](https://slack.engineering/introducing-electron-to-the-windows-runtime-4fa789b93d90){:target="_blank"}
	* 簡單介紹如何包裝Eletrcon App上Windows App Store


<br>

---

<br>

## macOS

### macOS Node API

* [github: node-applescript](https://github.com/TooTallNate/node-applescript){:target="_blank"}
* [github: NodObjC](https://github.com/TooTallNate/NodObjC){:target="_blank"}