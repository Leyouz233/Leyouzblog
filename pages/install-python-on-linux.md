title: Linux安装Python遇到的坑
date: 2021-3-01 17:31:52
introduce: 在Linux安装Python的时候，因为安装路径写错，导致了在使用Python出现了错误
tag: Python, Linux

### 前因后果
前几天元宵放假的时候，趁着有时间，把之前买的树莓派整了一下下。

主要是之前买了一台的树莓派zero w嘛，然后准备在上面部署我的[Flask项目](http://facker.herokuapp.com)，而之前用的一直都是Python3.9，而我的小派烧录的系统是Raspberry Pi Lite版的（好像是吧，此处待定）。

这个系统里面默认自带的Python是3.7版的和2.7版的，所以嘛，作为Linux小白的我，反手一顿操作

```Linux
rm python*
```

把（某目录，待定）下的python应用程序删除了。

删除了一回事，我就怕删除不干净😥，因为它们不是放在同一个文件位置，什么（balabala各类文件放着各个相关的东西）。

然后使用 `which`啊，`whereis`啊，搜索着Python有没有卸载干净，虽然吧，其实还是老感觉没有删除干净。

然后又在担心会不会像Windows那样会不会有那种环境变量之类的，emmm，毕竟~~强迫症~~嘛😅，所以。。。

最后，不管三七二十一，先安装了再说！！

### 安装Python3.9
来吧来吧，虽然是Python在Linux安装教程在网上一大堆，不过呢，嗯嘛，还是写写的啦，算做是做个记录吧。

#### 下载Python3.9
使用`wget`来把Python3.9下载到本地。

```Linux
wget https://（链接待定）
```

#### 解压Python3.9
解压Python使用的工具是`tar`。

```Linux
tar -zxvf(待定) （待定压缩包）
```
