#

## 创建虚拟环境

```bash
python -m venv venv

source venv/bin/activate # mac或unix

venv\Scripts\activate # windows
```

### 使用requirements.txt管理依赖

每次安装新的依赖包后，通过以下命令生成或更新 requirements.txt 文件：

```bash
pip freeze > requirements.txt
```

一次性安装所有依赖

```bash
pip install -r requirements.txt
```
