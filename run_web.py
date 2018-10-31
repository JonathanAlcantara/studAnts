import os

from web.app import create_app

if __name__ == '__main__':
    webs = create_app()
    webs.run('0.0.0.0', int(os.getenv('PORT', '8765')), debug=True)
