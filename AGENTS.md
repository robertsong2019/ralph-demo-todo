# AGENTS.md - Ralph Loop Agent 指令

## 项目信息
- **项目名称**: Todo CLI
- **技术栈**: Python 3, click/argparse, JSON
- **数据文件**: `~/.todo.json`

## 开发环境
```bash
# Python 版本
python3 --version

# 使用标准库 argparse（无需安装依赖）
# 代码使用 argparse 实现
```

## 测试命令（Backpressure）
每次实现功能后运行这些命令验证：

```bash
# 1. 测试添加任务
python3 todo.py add "学习 Ralph Loop"
python3 todo.py add "完成待办工具"

# 2. 测试列出任务
python3 todo.py list

# 3. 测试完成任务
python3 todo.py done 1

# 4. 测试删除任务
python3 todo.py delete 2

# 5. 测试清空已完成任务
python3 todo.py clear

# 6. 查看数据文件
cat ~/.todo.json
```

## 提交规范
- `feat: 添加新功能`
- `fix: 修复 bug`
- `refactor: 重构代码`
- `test: 添加测试`

## 注意事项
1. JSON 文件不存在时需要自动创建
2. 任务 ID 应该是递增的整数
3. 每个任务包含：id, content, completed, created_at
4. 错误处理：无效 ID、空任务列表等
