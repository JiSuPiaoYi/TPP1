from flask import Flask
from flask_script import Manager, Server
from app import create_app
from flask_migrate import MigrateCommand

app = create_app('dev')

manage = Manager(app)

manage.add_command('start', Server(host='127.0.0.1', port=8888))
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
