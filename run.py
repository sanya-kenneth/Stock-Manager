from app import create_app
from app.auth.database import db_handler

# App entry point
app = create_app("Production")
db_handler().create_tables()
  
if __name__ == '__main__':
    app.run()