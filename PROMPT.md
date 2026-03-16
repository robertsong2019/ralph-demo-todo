# Ralph Loop: 待办事项 CLI 工具

## 目标
开发一个 Python 命令行待办事项管理工具。

## 功能需求
1. **添加任务** - `todo add "任务内容"`
2. **列出任务** - `todo list` （显示所有任务）
3. **完成任务** - `todo done <id>` （标记任务为完成）
4. **删除任务** - `todo delete <id>` （删除任务）
5. **清空任务** - `todo clear` （清空所有已完成的任务）

## 技术要求
- 使用 Python 3
- 使用 `click` 或 `argparse` 处理命令行参数
- 数据存储在 JSON 文件中（`~/.todo.json`）
- 代码结构清晰，易于维护
- 包含基本错误处理

## 上下文文件
- 规格说明：`specs/`
- 实施计划：`IMPLEMENTATION_PLAN.md`
- Agent 指令：`AGENTS.md`

## 完成标准
在 `IMPLEMENTATION_PLAN.md` 中添加 `STATUS: COMPLETE` 表示完成。
