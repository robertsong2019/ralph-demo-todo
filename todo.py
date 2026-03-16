#!/usr/bin/env python3
"""待办事项命令行工具"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

DATA_FILE = Path.home() / ".todo.json"


def load_todos():
    """加载待办事项"""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_todos(todos):
    """保存待办事项"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def get_next_id(todos):
    """获取下一个任务 ID"""
    if not todos:
        return 1
    return max(t["id"] for t in todos) + 1


def cmd_add(content):
    """添加新任务"""
    todos = load_todos()
    todo = {
        "id": get_next_id(todos),
        "content": content,
        "completed": False,
        "created_at": datetime.now().isoformat(),
    }
    todos.append(todo)
    save_todos(todos)
    print(f"✓ 已添加任务 #{todo['id']}: {content}")


def cmd_list():
    """列出所有任务"""
    todos = load_todos()
    if not todos:
        print("暂无任务")
        return

    for todo in todos:
        status = "✓" if todo["completed"] else "○"
        print(f"{status} #{todo['id']}: {todo['content']}")


def cmd_done(task_id):
    """标记任务为完成"""
    todos = load_todos()
    for todo in todos:
        if todo["id"] == task_id:
            todo["completed"] = True
            save_todos(todos)
            print(f"✓ 已完成任务 #{task_id}")
            return
    print(f"✗ 未找到任务 #{task_id}")


def cmd_delete(task_id):
    """删除任务"""
    todos = load_todos()
    for i, todo in enumerate(todos):
        if todo["id"] == task_id:
            todos.pop(i)
            save_todos(todos)
            print(f"✓ 已删除任务 #{task_id}")
            return
    print(f"✗ 未找到任务 #{task_id}")


def cmd_clear():
    """清空所有已完成的任务"""
    todos = load_todos()
    original_count = len(todos)
    todos = [t for t in todos if not t["completed"]]
    removed = original_count - len(todos)
    save_todos(todos)
    print(f"✓ 已清空 {removed} 个已完成任务")


def main():
    parser = argparse.ArgumentParser(description="待办事项管理工具")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add 命令
    add_parser = subparsers.add_parser("add", help="添加新任务")
    add_parser.add_argument("content", help="任务内容")

    # list 命令
    subparsers.add_parser("list", help="列出所有任务")

    # done 命令
    done_parser = subparsers.add_parser("done", help="标记任务为完成")
    done_parser.add_argument("id", type=int, help="任务 ID")

    # delete 命令
    delete_parser = subparsers.add_parser("delete", help="删除任务")
    delete_parser.add_argument("id", type=int, help="任务 ID")

    # clear 命令
    subparsers.add_parser("clear", help="清空所有已完成的任务")

    args = parser.parse_args()

    if args.command == "add":
        cmd_add(args.content)
    elif args.command == "list":
        cmd_list()
    elif args.command == "done":
        cmd_done(args.id)
    elif args.command == "delete":
        cmd_delete(args.id)
    elif args.command == "clear":
        cmd_clear()


if __name__ == "__main__":
    main()
