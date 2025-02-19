from flask import Blueprint
from init import db
from models.student import Student

cli_bp = Blueprint("db", __name__)

@cli_bp.cli.command('init')
def create_tables():
    db.drop_all()
    db.create_all()
    print('Tables Creates')
    
@cli_bp.cli.command('seed')
    def