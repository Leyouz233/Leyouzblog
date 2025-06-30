# -*- coding: utf-8 -*-
import sys
import os
from pathlib import Path
from typing import Optional, List
import git
from git.repo import Repo
from datetime import datetime  # 新增导入datetime模块


def get_current_time() -> dict:
    """获取当前时间并返回各部分"""
    now = datetime.now()
    return {
        'year': now.strftime("%Y"),
        'month': now.strftime("%m"),
        'day': now.strftime("%d"),
        'time': now.strftime("%H:%M")
    }


def get_user_input(prompt: str, default: Optional[str] = None) -> str:
    """获取用户输入，支持默认值"""
    if default:
        prompt = f"{prompt}(默认: {default})："
    else:
        prompt = f"{prompt}："
    user_input = input(prompt).strip()
    return user_input if user_input else default if default else ""


def confirm_action(prompt: str) -> bool:
    """确认用户是否要继续"""
    while True:
        answer = input(f"{prompt} (y/n): ").lower()
        if answer in ('y', 'yes'):
            return True
        elif answer in ('n', 'no'):
            return False
        print("请输入 y 或 n")


def create_file_if_not_exists(file_path: Path) -> None:
    """如果文件不存在则创建，存在则根据用户选择清空内容"""
    if file_path.exists():
        if not confirm_action("文件已存在，是否清除旧文件内容？"):
            print("操作取消")
            sys.exit(1)
        print("清除文件内容...")
        file_path.write_text('', encoding='utf-8')
    else:
        print("创建新文件...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch()


def write_metadata(file_handle, title: str, date_time: str, introduce: str, tag: str = "日记") -> None:
    """写入文章元数据"""
    metadata = [
        f"title: {title}",
        f"date: {date_time}",
        f"introduce: {introduce}",
        f"tag: {tag}",
        "\n"
    ]
    file_handle.write("\n".join(metadata))


def write_image(file_handle, year: str, month: str, day: str, index: str) -> None:
    """写入图片标记"""
    img_path = f"/static/img/{year}/{month}/{day}/{index}.jpg"
    file_handle.write(f"![{index}]({img_path})\n\n")


def write_video(file_handle, year: str, month: str, day: str, index: str) -> None:
    """写入视频标记"""
    video_html = f"""
<div class="background-color: rgb(40, 46, 83);width: 100%;height: 100%;">
    <video class="object-fit: fill;" src="/static/img/{year}/{month}/{day}/{index}.mp4" controls
                    preload="auto" width="100%" height="100%">
    </video>
</div>
"""
    file_handle.write(video_html + "\n")


def todo_page() -> None:
    """生成文章页面"""
    print("\n开始生成文章")
    print("--------------------")

    # 获取当前时间作为默认值
    current_time = get_current_time()

    # 获取日期信息，使用当前时间作为默认值
    date_year = get_user_input("输入年份", current_time['year'])
    date_month = get_user_input("输入月份", current_time['month'])
    date_day = get_user_input("输入日期", current_time['day'])
    data_time = get_user_input("输入时间", current_time['time'])

    # 构建文件路径
    file_path = Path(f"./pages/{date_year}/{date_month}/{date_day}.md")
    print(f"\n文件路径：{file_path}")

    if not confirm_action("确定此文件路径吗？"):
        print("操作取消")
        sys.exit(1)

    create_file_if_not_exists(file_path)

    # 获取文章内容
    print("\n-------确认完毕----------")
    date_title = get_user_input("标题")
    data_introduce = get_user_input("简介")

    # 写入内容
    print("\n-------开始写入内容------")
    with file_path.open('a+', encoding='utf-8') as f:
        # 写入元数据
        full_date = f"{date_year}-{date_month}-{date_day} {data_time}:00"
        write_metadata(f, date_title, full_date, data_introduce)

        # 写入内容部分
        f.write("#### 学习&记录\n")

        # 处理媒体文件
        try:
            p_nums = int(get_user_input("图片数（请把视频包含在内）", "0"))
        except ValueError:
            print("请输入有效的数字")
            sys.exit(1)

        if p_nums > 0:
            has_video = confirm_action("有视频吗")
            video_num = None
            if has_video:
                video_num = get_user_input("第几个是视频")

            for i in range(1, p_nums + 1):
                idx = str(i)
                if has_video and idx == video_num:
                    write_video(f, date_year, date_month, date_day, idx)
                else:
                    write_image(f, date_year, date_month, date_day, idx)

    print("\n文章生成完成！")


def git_status(repo: Repo) -> None:
    """显示Git仓库状态"""
    print("\n仓库变更状态:")
    diffs = repo.index.diff(None)
    if diffs:
        print("已修改文件:")
        for d in diffs:
            print(f"  - {d.a_path}")
    else:
        print("没有已修改文件")

    untracked = repo.untracked_files
    if untracked:
        print("\n未跟踪文件:")
        for u in untracked:
            print(f"  - {u}")
    else:
        print("\n没有未跟踪文件")


def todo_freeze() -> None:
    """冻结文件并处理Git操作"""
    print('\n开始冻结文件')
    os.system('python freeze.py')

    try:
        repo = git.Repo('../leyouz233')
    except git.InvalidGitRepositoryError:
        print("错误: 不是有效的Git仓库")
        sys.exit(1)

    git_status(repo)

    if confirm_action("\n是否需要提交更改？"):
        add_files = get_user_input("输入需要暂存的文件(如果为.表示全部)", ".")
        repo.git.add(add_files)
        
        commit_msg = get_user_input("输入提交消息")
        if commit_msg:
            repo.git.commit('-m', commit_msg)
            print("提交完成")
        else:
            print("提交消息为空，取消提交")

    if confirm_action("\n是否需要推送到远程仓库？"):
        print("推送中...")
        try:
            repo.git.push()
            print("推送完成")
        except git.GitCommandError as e:
            print(f"推送失败: {e}")


def main(args: str) -> None:
    """主函数，接收参数并处理"""
    if args == 'page':
        todo_page()
    elif args == 'freeze':
        todo_freeze()
    else:
        print(f'未知参数: {args}')
        print("可用参数: page, freeze")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请提供参数: page 或 freeze")
        sys.exit(1)
    main(sys.argv[1])