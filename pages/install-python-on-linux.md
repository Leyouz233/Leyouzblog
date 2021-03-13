title: Linux安装Python遇到的坑
date: 2021-3-01 17:31:52
introduce: 在Linux安装Python的时候，因为安装路径写错，导致了在使用Python出现了错误
tag: Python, Linux

### 前因后果
前几天元宵放假的时候，趁着有时间，把之前买的树莓派整了一下下。

主要是之前买了一台的树莓派zero w嘛，然后准备在上面部署我的[Flask项目](http://facker.herokuapp.com)，而之前用的一直都是Python3.9，而我的小派烧录的系统是Raspbian Lite。

这个系统里面默认自带的Python是3.7版的和2.7版的，所以嘛，作为Linux小白的我，反手一顿操作

```Linux
rm python*
```

把/usr/bin下的python应用程序删除了。

删除了一回事，我就怕删除不干净😥，因为它们不是放在同一个文件位置，什么（balabala各类文件放着各个相关的东西）。

然后使用 `which`啊，`whereis`啊，搜索着Python有没有卸载干净，虽然吧，其实还是老感觉没有删除干净。

然后又在担心会不会像Windows那样会不会有那种环境变量之类的，emmm，毕竟~~强迫症~~嘛😅，所以。。。

最后，不管三七二十一，先安装了再说！！

### 安装Python3.9
来吧来吧，虽然是Python在Linux安装教程在网上一大堆，不过呢，嗯嘛，还是写写的啦，算做是做个记录吧。

#### 下载Python3.9
使用`wget`来把Python3.9下载到本地。

```Linux
wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tgz
```

#### 解压Python3.9
因为下载好的是归档文件tarball，所以解压Python使用的工具是`tar`。

```Linux
tar -zxvf Python-3.9.2.tgz
```

#### 编译并安装
使用`cd`进入到解压好的Python文件里面，可以用`ls`命令查看其中的文件，

```Linux
cd Python-3.9.2
ls
```
Linux对源代码的安装分为两步：编译，安装

##### 编译源代码
通过`ls`查看Python源代码目录下有没有`configure`文件
然后执行编译

```Linux
./configure --prefix=/usr/local/python39
```

`注意注意`，这里的路径千万千万别写错，之前在树莓派安装3.9的时候，就是因为local写成了loacl，导致环境变量PATH没有这个路径，然后在命令行里面输入python3.9的时候报错是找不到，后来的解决方案是把安装错的Python移到local上面，然后就就可以用了。

##### 安装
没报错的话就说明好了（废话）
然后执行安装命令

```Linux
make
make install
```

如果这个时候报错就要注意了，一般是缺少依赖环境，我的树莓派上好像当时就缺少个openssl，反正安装的时候报错缺啥apt-get就安装啥，然后再重新make一下就行，实在不会也可以自行百度。

#### 解决pip报错问题
因为上面那一段提到说路径写错，然后重新修改路径后，其实际上pip是不能用的，当在命令行输入`pip3`会报错找不到pip，一般是路径错误，这个时候对应上文我们把Python3.9移到了local上面，这时可以通过vim来修改pip的路径

```Linux
sudo vim /usr/local/python39/bin/pip3.9
```

因为路径错误，所以在第一行我们看到的是`#!/usr/loacl/python39/bin/python3.9`，其中是loacl而不是local😢所以修改保存就可以了😁

### 总结
在树莓派安装Python不难，不过因为是树莓派zero w，所以在编译安装那一环节CPU温度飙升就是挺心疼的，毕竟也是头一回在Linux上面安装Python，有不懂的还是慢慢摸索着过去，算作是一次不错的学习经验吧！
