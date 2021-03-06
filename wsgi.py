"""App entry point"""
from library import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='localhost', port=4000, threaded=False)