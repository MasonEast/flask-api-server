from dotenv import load_dotenv

# 在加载flask应用之前加载.env文件
load_dotenv()

from api import app, db

# falsk shell环境增加上下文
@app.shell_context_processor
def make_shell_context():
    return {
        "app": app,
        "db": db
    }

if __name__ == '__main':
    app.run(debug=True)