
from dotenv import load_dotenv

# 在加载flask应用之前加载.env文件
load_dotenv()
       
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)