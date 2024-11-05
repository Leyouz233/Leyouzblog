# -*- coding: utf-8 -*-
import sys  # 导入sys模块以便获取命令行参数
import os   # 导入os模块处理文件

def todo_page():
    print ('开始生成文章')
    print ("--------------------")
    print ("------写入数据------")
    print ("------确认时间------")
    date_year =  input("输入年份(2024)：")
    date_month = input("输入月份(06)：")
    date_day =   input("输入日期(06)：")
    data_time =  input("输入时间(11:22)：")
    print ("检定文件是否存在===>")
    exist = r"./pages/" + date_year + "/" + date_month + "/" + date_day + ".md"
    print("文件路径：" + exist)
    e_yn = input("确定此文件路径吗(y/n)：")
    if e_yn == 'y':
        pass
    else:
        exit(1)
    if os.path.exists(exist):
        yn = input("文件已存在，是否清除旧文件内容(y/n)：")
        if yn == "y":
            print("清除文件内容")
            with open(exist,'a+',encoding='utf-8') as test:
                test.truncate(0)
        else:
            exit(1)
    else:
        print("确定文件不存在，创建新文件")
        # 创建文件
        os.mknod(exist)    # 创建空文件
        print("--------创建完毕----------")

    print ("-------确认完毕----------")
    date_title = input("标题：") ; data_introduce = input("简介：")
    print ("-------开始写入内容------")
    with open(exist,'a+',encoding='utf-8') as text:
        w_title = "title: " + date_title
        w_date_time = "date: " + date_year + "-"+ date_month + "-"+ date_day +  " " + data_time + ":00"
        w_introduce = "introduce: " + data_introduce
        w_tag = "tag: " + "日记"
        text.write(w_title)
        text.write("\n")
        text.write(w_date_time)
        text.write("\n")
        text.write(w_introduce)
        text.write("\n")
        text.write(w_tag)
        text.write("\n")
        text.write("\n")
        print ("-------标题写入完成------")
        print ("-------开始写入内容------")
        text.write("#### 学习&记录")
        text.write("\n")
        p_nums = (input("图片数（请把视频包含在里）："))
        pv_group = list(range(1, int(p_nums) + 1))
        str_pv_group = map(str, pv_group)
        yn_vido = input("有视频吗(y/n)：")
        if yn_vido == "y":
            vido_num = input("第几个是视频：")
            for i in str_pv_group:
                if i == vido_num:
                    w_v_1 = "<div class=\"background-color: rgb(40, 46, 83);width: 100%;height: 100%;\">"
                    w_v_2 = "    <video class=\"object-fit: fill;\" src=\"/static/img/" + date_year + "/" + date_month + "/" + date_day + "/" + i + ".mp4\" controls"
                    w_v_3 = "                    preload=\"auto\" width=\"100%\" height=\"100%\">"
                    w_v_4 = "    </video>" 
                    w_v_5 = "</div>"
                    text.write(w_v_1)
                    text.write("\n")
                    text.write(w_v_2)
                    text.write("\n")
                    text.write(w_v_3)
                    text.write("\n")
                    text.write(w_v_4)
                    text.write("\n")
                    text.write(w_v_5)
                    text.write("\n")
                    text.write("\n")

                else:
                    w_p = "![" + i + "](/static/img/" + date_year + "/" + date_month + "/" + date_day + "/" + i + ".jpg)"
                    text.write(w_p)
                    text.write("\n")
                    text.write("\n")
        else:
            for i in str_pv_group:
                w_p = "![" + i + "](/static/img/" + date_year + "/" + date_month + "/" + date_day + "/" + i + ".jpg)"
                text.write(w_p)
                text.write("\n")
                text.write("\n")
    
def todo_freeze():
    print ('开始冻结文件')

def main(args):
    """ 主函数，接收参数并处理 """
    if args == 'page':
        todo_page()

    elif args == 'freeze':
        todo_freeze()

    else:
        print ('未知参数')


        

if __name__ == "__main__":
    main(sys.argv[1])  # sys.argv[1:]获取命令行参数（除去脚本名）
