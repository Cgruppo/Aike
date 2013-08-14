###说明

#依赖库
* 依赖图像处理模块PIL `pip install PIL`
* 依赖二维码生成模块qrencode(已知问题，png格式不能正常保存，和环境有关)
> 编译安装需要libpng库
> 下载qrencode-3.1.1.tar.gz 解压，使用configure、make、make install安装
> 下载cython，编译安装
> 下载pyqrencode，使用cython安装，即`cython qrencode.pyx`
an
#运行说明
* 依赖Django
* `sudo apt-get install pip`
* `sudo pip install Django==1.4.2` (或者自己建一个Django专用python依赖环境)
* 项目目录下
* `python manage.py runserver`
* 点击 `127.0.0.1:8000`

#已实现的功能
* 注册、登陆，个人信息的更改，与个人相关的活动，留言板（还有一点小遗漏）
* 添加好友、好友分组显示、消息通知（不完善）
* 活动展示、添加活动、对活动评论[1.28]

* API请从view文件夹下的api.py处查看

# 8.14
* 迁移到Github

# 6月
* 地图定位
* API修正若干

#4.15
* 增加活动信息更改的功能与界面
* 修正活动简介显示格式问题

#4.13
* 为二维码添加访问控制权限
* 添加二维码获取API
* 添加api测试文件，位于apiApp的apiTest目录下,便于对API测试管理
* 对jQurey隐藏和显示动画测试，测试页面为注册页面

#4.8
* 调试模式仅限于freedom-PC，其余计算机请自行更改settings.py中的DEBUG参数
* 尝试为二维码静态文件添加访问权限（未完成）
# TODO 
* 二维码存放于缓存中

#3.28
* 添加二维码生成
* 添加活动管理页面（待完善）

#2.19
* 主页添加轮询插件
* 修正API登陆的一个错误
* 导航栏上的登陆改为登陆对话框

#2.17
* 添加用户访问模式界面，显示该用户最近参与和举办的活动，以及留言板功能
* 添加好友功能更改，主要为更改消息通知系统
* 修改部分样式
* 输出字符串大量更正为unicode类型，部分可能会有遗漏
* API部分做更正，更正一个函数名写错，更正一个不能json化的变量

#TODO
* 客户端无法正常登陆，错误信息为服务器端错误，但是使用python模拟登陆已经老版本登陆能够正常使用
* 其余项客户端未能正常测试，python端模拟正常

#2.14 构架大更新
* 将原有数据处理分离开来，成为userApp,activityApp,apiApp等多个应用，各自独立使用数据库和路由、视图
* 数据库多对多模型，特别事activityApp中的，做了较大更改，相应的视图以及模板也均更改了部分函数

# 原有日志请看master分支
