# Mdtero: Academic Markdown & Translation Engine 📄✨

[**🌍 访问官网 / Visit the Website: mdtero.pages.dev**](https://mdtero.pages.dev) 
**API 状态 / API Status**: `LIVE` (api.mdtero.com)

[English](#english) | [中文说明](#chinese)

---

<a name="english"></a>
## 🇬🇧 English: Mdtero Extension & Open API

**Mdtero** is a powerful web platform, Chrome Extension, and API toolkit designed to seamlessly convert dense academic research papers into clean, beautifully structured Markdown—all without losing scientific rigor.

This repository hosts the **public open-source Chrome extension** and **developer API integration guides**, demonstrating our commitment to transparency and empowering developers to build custom academic AI workflows.

### 🌟 Key Features

- **🌐 The Web Dashboard**: Manage your parsed papers, account credits, and view authentic demos natively on our [official website](https://mdtero.pages.dev).
- **🖱️ One-Click Parsing (Extension)**: Detects DOIs natively from academic publishers (e.g., ScienceDirect) and extracts the full paper payload directly in your browser.
- **🔬 True Scientific Accuracy**: Preserves LaTeX equations, distinct data tables, and authentic figure references that regular scraping tools destroy.
- **🤖 AI-Powered Translations**: Offers fully integrated English-to-Chinese academic translations using optimized LLM prompts without losing markup structure.
- **🔌 Agent Integrations**: Built-in API support for Claude Code, OpenClaw, and other Model Context Protocol (MCP) clients.

### 🛠️ Installation (Chrome Extension)

1. Download the latest `mdtero-extension-beta.zip` from our [Homepage](https://mdtero.pages.dev) or build it from this repository.
2. Unzip the file into a folder.
3. Open Google Chrome and navigate to `chrome://extensions`.
4. Enable **Developer mode** in the top-right corner.
5. Click **Load unpacked** and select the folder where you extracted the extension.
6. Click the Mdtero icon in your toolbar, enter your API Key safely generated from the Account Dashboard, and start parsing!

### 💻 Developer API & Agent Integrations

Mdtero is built for developers. Generate an API key from your [Account Dashboard](https://mdtero.pages.dev/account), then refer to our [API Documentation](https://mdtero.pages.dev/api) for endpoints.

- **OpenClaw / MCP Integration**: Give your local AI Assistant (like Cursor) the ability to read papers natively. Check the [OpenClaw Guide](./openclaw/INSTALL.md).
- **Claude Code Integration**: Check the [Claude Code Guide](./codex/INSTALL.md).
- **Direct REST API**: Use `cURL` or Python to trigger jobs directly against `api.mdtero.com`.

### 🔒 Privacy Architecture
This repository contains the **client-side extension code**, open-sourced for your security audit. The heavy lifting—proprietary chunking, LLM translation pipelines, Stripe billing, and LaTeX reconstruction—is securely hosted on our closed-source API backend.

---

<a name="chinese"></a>
## 🇨🇳 中文：Mdtero 浏览器插件与开放 API

**Mdtero** 是一款强大的全栈学术平台、Chrome 浏览器插件和开放 API 工具包。它被设计用于将密集的学术论文无缝转换为结构清晰、排版精美的 Markdown 格式，同时绝对保证科研数据的严谨性。

本仓库托管了 **开源的 Chrome 浏览器插件代码** 以及 **开发者 API 接入指南**。我们致力于全景化透明的隐私安全，并支持开发者在我们的解析引擎上构建定制化的 AI 学术工作流。

### 🌟 核心功能

- **🌐 网页端控制台**: 在我们的 [官方主页](https://mdtero.pages.dev) 统一管理您的解析文献、账户余额，并体验无损渲染效果。
- **🖱️ 一键快速解析 (插件端)**: 自动检测学术出版商（如 ScienceDirect）页面上的 DOI，并在浏览器内一键触发全文获取。
- **🔬 真正的科研级精度**: 完美保留原本会被普通爬虫破坏的 LaTeX 数学公式、复杂数据表格以及真实的图表文献引用。
- **🤖 AI 深度翻译**: 深度集成了英文至中文的学术级 AI 翻译，使用优化的 LLM 提示词矩阵，且保证 Markdown 排版结构完全不丢失。
- **🔌 前沿 Agent 接入**: 内置对 Claude Code, OpenClaw 以及其他 Model Context Protocol (MCP) 客户端的 API 原生支持。

### 🛠️ 插件安装说明 (Chrome Extension)

1. 从我们的 [主页](https://mdtero.pages.dev) 下载最新的 `mdtero-extension-beta.zip`，或直接克隆本仓库源码编译。
2. 将 ZIP 文件解压到一个固定文件夹中。
3. 打开 Google Chrome 浏览器并输入跳转至 `chrome://extensions`。
4. 打开右上角的 **“开发者模式 (Developer mode)”**。
5. 点击左上角的 **“加载已解压的扩展程序 (Load unpacked)”** 按钮，选中刚解压的文件夹。
6. 点击浏览器工具栏的 Mdtero 图标，粘贴您在账户后台安全生成的 API Key，即可开始学术解析！

### 💻 开发者 API 与 Agent 接入指南

Mdtero 是为开发者而生的。在您的 [个人账户 Dashboard](https://mdtero.pages.dev/account) 中生成 API 密钥后，即可参阅 [API 官方文档](https://mdtero.pages.dev/api) 获取所有能力接口。

- **OpenClaw / MCP 协议接入**: 赋予您本地的 AI 助手（如 Cursor）原生阅读顶级学术论文的能力。点此查看 [OpenClaw 接入配置说明](./openclaw/INSTALL.md)。
- **Claude Code 接入**: 点此查看 [Claude Code 接入说明](./codex/INSTALL.md)。
- **原生 REST API**: 您完全可以使用 `cURL` 或是 Python 直接向 `api.mdtero.com` 提交解析及翻译任务。

### 🔒 隐私与架构设计
本仓库提供的仅为**前端客户端与插件的开源源码**，目的是供学术用户进行隐私安全审计。真正繁重的计算任务——专有分块防断版算法、多路 LLM 翻译流水线、Stripe 安全支付以及核心的 LaTeX 解析重建引擎——均受到严格保护，且稳定运行在我们闭源的云端 API 服务器上。 

---
*Mdtero is a research workflow tool. We empower researchers to interact with science natively.*
