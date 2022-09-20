import os
from app import create_app

#conf = os.getenv('FLASK_CONFIG')
conf = os.environ.get('FLASK_CONFIG')
app = create_app(conf or 'default')

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(port=port,debug=True)