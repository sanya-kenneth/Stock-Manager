from app import create_app

# App entry point
app = create_app("Development")
  
if __name__ == '__main__':
    app.run()