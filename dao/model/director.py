from setup_db import db
from marshmallow import Schema, fields


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)


class DirectorSchema(Schema):
    id = fields.Integer()
    name = fields.String()


director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)
