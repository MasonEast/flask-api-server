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
