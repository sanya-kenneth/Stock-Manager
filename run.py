from app import create_app
from app.auth.database import Database


app = create_app("Testing")
if __name__ == '__main__':
    app.run()