
from marshmallow import Schema, fields, validate

class UsuarioCreateSchema(Schema):
    nome = fields.Str(required=True, validate=validate.Length(min=2, max=120))
    email = fields.Email(required=True)

class UsuarioSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str()
    email = fields.Email()
    data_criacao = fields.DateTime()
