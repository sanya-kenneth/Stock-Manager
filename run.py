from app import create_app
from app.auth.database import Database
# App entry point
app = create_app("Production")
db = Database(app.config['DATABASE_URI'])
db.create_tables()
db.add_user('ben','ben@gmail.com',generate_password_hash('ben'),True)
  
if __name__ == '__main__':
    app.run()