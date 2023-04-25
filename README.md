# 新乡工程学院网站设计项目
> 本项目为设计大学实训项目，大学实训项目参照新乡工程学院官方网站以及北大清华等高校官网借鉴

# 项目介绍

# 项目呈现

# 关键技术
> migrations 数据库迁徙文件夹
> __init__.py 标识文件，Python模块
> template文件夹编辑前端HTML文件
> 在视图文件viewer.py创建并编辑视图处理函数
> urls绑定请求和对应的视图处理函数
> apps.py 应用配置文件，
> test测试文件
* 创建步骤
    * urls.py配置路由URL
# Python语法
## Python类
```python
class Student(object):
    def __init__(self,name,score): # 后面object表示从那个类继承过来 等价于C++的构造函数
        self.name = name  # self为第一个参数永远是self，代表创建对象的本身，
        self.score = score # 将外部变量传入类的内部
```
## Python闭包
> Python的闭包从形式上:在一个`内部函数`里，对在`外`部作用域的变量进行`引用`，并且外部函数将`此内部函数`作为`返回`值，那么这个`内部函`数就被认为是`闭包closure`
```python
def line_conf(a,b): # 采用闭包将line进一步进行封装
    def line(x):   # 调用line内部函数
        return a*x +b
    return line
line_A = line_conf(2,1)
line_B = line_conf(3,2)
line_C = line_conf(5,-3)
print(line_A(1))  # 输出3
print(line_A(1))  # 输出5
print(line_A(1))  # 输出2
```
## 装饰器
> 例如`@timer`
> 在并不修改原函数的代码也不修改函数调用形式实现功能的扩展
## 引用
```html
<!--引用css-->
<link href="" rel="stylesheet">
<!--引用js-->
<script src=""></script>
```
> [具体使用](use.md)
# 依赖环境（需要更新)
> bootstrap 5 + Django3.2.3 + Python3.6 +   DPlayer v1.27.1
> 安装DjangoUeditor==1.8.143：下载链接https://gitcode.net/mirrors/twz915/djangoueditor3?utm_source=csdn_github_accelerator
> D:\djangoueditor3>E:\新工项目\venv\Scripts\python.exe setup.py install
> 使用国内镜像 pip install 安装包名 -i https://pypi.tuna.tsinghua.edu.cn/simple
> 
* Django3去除six和urllib[解决](https://blog.csdn.net/zhch1979/article/details/104684122/)
> 报错: render() got an unexpected keyword argument 'renderer' [解决](https://www.jianshu.com/p/02cbb1b96c8f)