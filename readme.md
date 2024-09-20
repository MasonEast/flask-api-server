# 项目

## 创建虚拟环境

```bash
python -m venv venv

source venv/bin/activate # mac或unix

venv\Scripts\activate # windows
```

## 使用requirements.txt管理依赖

每次安装新的依赖包后，通过以下命令生成或更新 requirements.txt 文件：

```bash
pip freeze > requirements.txt

# 使用淘宝镜像
-i https://pypi.tuna.tsinghua.edu.cn/simple
```

一次性安装所有依赖

```bash
pip install -r requirements.txt
```

## 配置flask命令脚本

### 方法一：命令行

```bash
# mac
export FLASK_APP=run.py
export FLASK_ENV=development
flask run 

# window
set FLASK_APP=run.py
set FLASK_ENV=development
flask run

# PowerShell
$env:FLASK_APP = "run.py"
$env:FLASK_ENV = "development"
flask run
```

### 方法二：.env文件

1. 首先安装 python-dotenv
2. 在项目根目录创建 .env 文件
3. 修改 run.py 文件以加载 .env 中的环境变量

## 部署生产环境

Flask 自带的服务器适合开发时使用，但不适合生产环境。你可以使用 WSGI 服务器（如 Gunicorn）来部署你的应用：

```bash
pip install gunicorn
gunicorn -w 4 app:app
```

这行命令使用 4 个工作进程运行你的 Flask 应用。

## 连接数据库

安装SQLAlchemy和pymysql

通过pymysql建立连接

```bash
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Ljf941118@localhost:3306/flask-db'
```

通过SQLAlchemy创建db对象

```python
db = SQLAlchemy()
```

## api设计

1. 用户服务
   1. 注册，登录，查看，编辑，注销
   2. 用户资料（id，用户名，性别，头像，出生岁月，常住地址，电话，邮箱，消息）
   3. 用户宠物信息管理
2. 宠物服务
   1. 增删改查
   2. 档案管理（id，类型，名称，照片，性格，习惯
3. 帖子服务
   1. 发布，编辑，删除帖子
   2. 查看帖子详情（id，标题，时间，作者，标签，内容，浏览量，点赞量，收藏量，转发量，评论
4. 通知服务
   1. 系统通知
   2. 用户消息提醒
5. 搜索服务
   1. 综合搜索（全文搜索，标签搜索）
   2. 分类搜索
6. 社区管理服务
   1. 社区规则管理
   2. 管理员操作（帖子审核，举报处理等
7. 文件服务
   1. 文件上传下载
   2. 文件安全管理
8. 推荐服务
   1. 个性化内容推荐
   2. 热门内容推荐
9. 分析服务
   1. 用户行为分析
   2. 平台数据统计
10. 聊天服务
    1. 一对一聊天
    2. 群组聊天
    3. 消息推送
