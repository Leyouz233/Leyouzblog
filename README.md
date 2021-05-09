好累啊
===
欢迎来到Facker的博客站点的源代码仓库“facker-blog”。在每天的忙碌中，抽出一点时间来为这个博客网站添加新的内容。

~~感觉还是挺厉害的~~

（还是一点点的吧）弄了这么久了，学了Flask，CSS，BootStrap，Git，只不过。。。跑了好几次Freenode，感谢帮助回答我问题的大佬。

主题
===
由于项目是部署到Heroku的，所以域名确实不好看，可是，自定义域名又要绑定信用卡（实名制）0.0

+ [Facker博客](http://facker.herokuapp.com)：`http://facker.herokuapp.com`

不过，既然域名都买了，哪里有不用的道理，所以做了一个中转站，项目部署在了Github Pages上面，源代码链接戳[这里](https://github.com/f-boss/Transfer-station)

+ [中转站](http://facker.site): `http://facker.site`

如何在本地运行
===
+ git clone https://github.com/f-boss/facker-blog.git # 将项目克隆到本地
+ cd facker-blog # 进入项目的根目录
+ python -m venv venv # 创建虚拟环境
+ source venv/bin/activate # 进入虚拟环境
+ python -m pip install -r requirements.txt # 下载所需的第三方库
+ python app.py # 运行app.py，打开http://0.0.0.0:5000 

关于后期计划
===
+ ~~引入js文件，为页面添加样式~~
+ 为文章页面添加目录导航侧边栏
+ 添加回到顶部功能
+ 添加标签页面
+ 通过日期进行索引文章
+ 增加404错误页面

关于另外一个计划
===
等我某一天吃饱了没事干的时候，我会重新设计一个新的博客主题的，因为毕竟现在忙着学习也没什么时间，不过还是尽量挤一挤吧。

`别关顾着看啊，给我一个star！谢谢老板！`

加油！
