
from sqlalchemy.exc import IntegrityError
from ..core.extensions import db
from ..models.user import Usuario

def criar_usuario(nome: str, email: str) -> Usuario:
    u = Usuario(nome=nome.strip(), email=email.strip().lower())
    db.session.add(u)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise ValueError("Email já cadastrado.")
    return u

def listar_usuarios() -> list[Usuario]:
    return Usuario.query.order_by(Usuario.id.asc()).all()

def buscar_usuario_por_id(uid: int) -> Usuario | None:
    return Usuario.query.get(uid)
