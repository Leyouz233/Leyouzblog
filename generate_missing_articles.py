# -*- coding: utf-8 -*-
import os
from pathlib import Path
from datetime import datetime
import calendar

# 配置路径
PAGES_DIR = Path("./pages/2025")
IMAGES_DIR = Path("./static/img/2025")

def get_weekday(year: int, month: int, day: int) -> str:
    """获取星期几的中文表示"""
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    weekday_index = datetime(year, month, day).weekday()
    return weekdays[weekday_index]

def get_current_time() -> str:
    """获取当前时间字符串 (HH:MM)"""
    return datetime.now().strftime("%H:%M")

def has_video_first(day_dir: Path) -> bool:
    """检查目录中第一个文件是否是视频"""
    files = sorted(day_dir.glob("*"))
    if files and files[0].suffix == ".mp4":
        return True
    return False

def generate_article(month: str, day: str, has_video_first: bool = False):
    """生成单篇文章"""
    year = 2025
    month_int = int(month)
    day_int = int(day)
    
    # 创建目录
    article_dir = PAGES_DIR / month
    article_dir.mkdir(parents=True, exist_ok=True)
    
    # 文章路径
    article_path = article_dir / f"{day}.md"
    
    # 获取星期几
    weekday = get_weekday(year, month_int, day_int)
    
    # 当前时间
    current_time = get_current_time()
    
    # 写入文章内容
    with open(article_path, 'w', encoding='utf-8') as f:
        # 元数据
        f.write(f"title: {month}月{day}日\n")
        f.write(f"date: {year}-{month}-{day} {current_time}:00\n")
        f.write(f"introduce: {weekday}\n")
        f.write("tag: 日记\n\n")
        
        # 内容部分
        if has_video_first:
            f.write('<h4 align="center">学习&记录</h4>\n')
        else:
            f.write("#### 学习&记录\n")
        
        # 获取图片和视频文件
        day_images_dir = IMAGES_DIR / month / day
        media_files = sorted(day_images_dir.glob("*"))
        
        for file in media_files:
            if file.suffix == ".mp4":
                f.write(f"""
<div class="background-color: rgb(40, 46, 83);width: 100%;height: 100%;">
    <video class="object-fit: fill;" src="/static/img/{year}/{month}/{day}/{file.name}" controls
                    preload="auto" width="100%" height="100%">
    </video>
</div>
""")
            elif file.suffix == ".jpg":
                file_num = file.stem
                f.write(f"![{file_num}](/static/img/{year}/{month}/{day}/{file.name})\n\n")

def find_missing_articles():
    """查找并生成缺失的文章"""
    print("开始检查缺失的文章...")
    
    # 遍历图片目录
    for month_dir in sorted(IMAGES_DIR.glob("*")):
        if not month_dir.is_dir():
            continue
            
        month = month_dir.name
        print(f"\n检查 {month} 月...")
        
        for day_dir in sorted(month_dir.glob("*")):
            if not day_dir.is_dir():
                continue
                
            day = day_dir.name
            # 检查是否有媒体文件
            media_files = list(day_dir.glob("*.jpg")) + list(day_dir.glob("*.mp4"))
            if not media_files:
                print(f"  {month}月{day}日: 无图片/视频，跳过")
                continue
                
            # 检查文章是否存在
            article_path = PAGES_DIR / month / f"{day}.md"
            if article_path.exists():
                print(f"  {month}月{day}日: 文章已存在")
                continue
                
            # 检查第一个文件是否是视频
            video_first = has_video_first(day_dir)
            
            # 生成文章
            print(f"  {month}月{day}日: 生成文章中...")
            generate_article(month, day, video_first)
            print(f"  {month}月{day}日: 文章生成完成")

    print("\n所有缺失文章检查完成!")

if __name__ == "__main__":
    find_missing_articles()