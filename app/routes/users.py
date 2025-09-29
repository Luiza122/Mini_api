from flask.views import MethodView
from flask_smorest import Blueprint, abort
from ..schemas.user import UsuarioCreateSchema, UsuarioSchema
from ..services.user_service import criar_usuario, listar_usuarios, buscar_usuario_por_id

blp = Blueprint("usuarios", __name__, url_prefix="/usuarios", description="Operações de usuários")

@blp.route("")
class UsuariosListResource(MethodView):

    @blp.response(200, UsuarioSchema(many=True))
    def get(self):
        """Listar todos os usuários"""
        return [u.to_dict() for u in listar_usuarios()]

    @blp.arguments(UsuarioCreateSchema)
    @blp.response(201, UsuarioSchema)
    def post(self, dados):
        """Criar um novo usuário"""
        try:
            u = criar_usuario(dados["nome"], dados["email"])
            return u.to_dict()
        except ValueError as e:
            abort(409, message=str(e))

@blp.route("/<int:usuario_id>")
class UsuarioResource(MethodView):

    @blp.response(200, UsuarioSchema)
    def get(self, usuario_id):
        """Buscar usuário por ID"""
        u = buscar_usuario_por_id(usuario_id)
        if not u:
            abort(404, message="Usuário não encontrado.")
        return u.to_dict()
