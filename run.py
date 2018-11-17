from app import create_app
from app.auth.database import Database
# App entry point
app = create_app("Production")
db = Database(app.config['DATABASE_URI'])
db.create_tables()
  
if __name__ == '__main__':
    app.run()