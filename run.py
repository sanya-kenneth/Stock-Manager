from app import create_app



config_name = "Development"
app = create_app(config_name)

if __name__ == '__main__':
    app.run()