# 📝 Todo CLI - Ralph Loop 演示项目

一个简洁优雅的命令行待办事项管理工具，由 **Ralph Loop** 自动化开发流程生成。

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Ralph Loop](https://img.shields.io/badge/Generated%20by-Ralph%20Loop-purple.svg)](https://github.com/openclaw)

---

## ✨ 功能特性

- 📋 **添加任务** - 快速记录待办事项
- 📊 **列出任务** - 查看所有待办任务
- ✅ **完成任务** - 标记任务为已完成
- 🗑️ **删除任务** - 移除不需要的任务
- 🧹 **清空已完成** - 批量清理已完成的任务
- 💾 **JSON 存储** - 数据持久化到本地文件
- 🛡️ **错误处理** - 友好的错误提示

---

## 🚀 快速开始

### 安装

无需安装依赖！使用 Python 标准库 `argparse` 实现。

```bash
# 克隆仓库
git clone https://github.com/robertsong2019/ralph-demo-todo.git
cd ralph-demo-todo
```

### 基本使用

```bash
# 添加任务
python3 todo.py add "学习 Ralph Loop"

# 列出所有任务
python3 todo.py list

# 标记任务为完成
python3 todo.py done 1

# 删除任务
python3 todo.py delete 2

# 清空所有已完成的任务
python3 todo.py clear
```

---

## 📖 详细用法

### 添加任务

```bash
$ python3 todo.py add "完成项目文档"
✓ 已添加任务 #1: 完成项目文档

$ python3 todo.py add "提交代码到 GitHub"
✓ 已添加任务 #2: 提交代码到 GitHub
```

### 列出任务

```bash
$ python3 todo.py list
○ #1: 完成项目文档
○ #2: 提交代码到 GitHub
```

### 完成任务

```bash
$ python3 todo.py done 1
✓ 已完成任务 #1

$ python3 todo.py list
✓ #1: 完成项目文档
○ #2: 提交代码到 GitHub
```

### 删除任务

```bash
$ python3 todo.py delete 2
✓ 已删除任务 #2
```

### 清空已完成任务

```bash
$ python3 todo.py clear
✓ 已清空 1 个已完成任务
```

---

## 📁 数据存储

任务数据存储在 `~/.todo.json` 文件中：

```json
[
  {
    "id": 1,
    "content": "完成项目文档",
    "completed": true,
    "created_at": "2026-03-16T16:00:00.000000"
  }
]
```

---

## 🎯 Ralph Loop 工作流程

本项目完全由 **Ralph Loop** 自动生成，演示了自动化开发流程：

```
1. 需求分析 → 读取 PROMPT.md
2. 代码生成 → 使用 Claude Code (GLM-5) 生成 todo.py
3. 自动测试 → 运行 backpressure 测试验证功能
4. 问题修复 → 遇到依赖问题自动改用 argparse
5. 计划更新 → IMPLEMENTATION_PLAN.md 标记完成
6. 完成 ✅
```

**耗时**: 约 3 分钟  
**人工干预**: 0 次  
**代码行数**: 140 行

---

## 🏗️ 项目结构

```
ralph-demo-todo/
├── todo.py                 # 主程序（140行）
├── README.md               # 项目文档
├── PROMPT.md               # Ralph Loop 任务描述
├── AGENTS.md               # Agent 指令和测试命令
├── IMPLEMENTATION_PLAN.md  # 实施计划和进度
└── ralph-prompt.txt        # Ralph 执行提示
```

---

## 🔧 技术栈

- **Python 3.8+** - 主要编程语言
- **argparse** - 命令行参数解析（标准库）
- **json** - 数据持久化（标准库）
- **pathlib** - 路径处理（标准库）

**零外部依赖！**

---

## 🤖 关于 Ralph Loop

**Ralph Loop** 是一个自动化开发循环系统，特点：

- 🔄 **自主迭代** - 自动规划、构建、测试
- 🧠 **智能决策** - 遇到问题自动调整方案
- ✅ **自动验证** - 运行 backpressure 测试
- 📊 **进度跟踪** - IMPLEMENTATION_PLAN.md 记录进度
- 🎯 **完成检测** - 自动判断任务完成状态

---

## 📝 开发日志

### 2026-03-16

- ✅ 项目初始化
- ✅ 创建 todo.py 主程序
- ✅ 实现所有 CRUD 功能
- ✅ 添加 JSON 数据存储
- ✅ 实现错误处理
- ✅ 通过所有 backpressure 测试
- ✅ 更新项目文档

---

## 📄 License

MIT License

---

## 🙏 致谢

- **Ralph Loop** - 自动化开发框架
- **Claude Code** - AI 编码助手
- **智谱 AI (GLM-5)** - 提供智能支持
- **OpenClaw** - Agent 运行平台

---

<div align="center">

** Made with ❤️ by Ralph Loop**

[🌟 Star this repo](https://github.com/robertsong2019/ralph-demo-todo) if you find it useful!

</div>
