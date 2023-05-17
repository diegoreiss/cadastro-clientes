from ..Configs.connection import DBConnectionHandler
from ..Entities.cliente import Cliente


class ClienteRepository:
    @staticmethod
    def select_all():
        with DBConnectionHandler() as db:
            clientes = db.session.query(Cliente).all()

            return clientes

    @staticmethod
    def select_by_id(id):
        with DBConnectionHandler() as db:
            cliente = db.session.query(Cliente) \
                .filter(Cliente.id == id) \
                .first()

            return cliente

    @staticmethod
    def insert(**kwargs):
        with DBConnectionHandler() as db:
            cliente_create = Cliente(**kwargs)

            db.session.add(cliente_create)
            db.commit()

    @staticmethod
    def delete(id):
        with DBConnectionHandler() as db:
            db.session.query(Cliente) \
                .filter(Cliente.id == id) \
                .delete()
            db.session.commit()

    @staticmethod
    def update(**kwargs):
        with DBConnectionHandler() as db:
            db.session.query(Cliente) \
                .filter(Cliente.id == id) \
                .update(**kwargs)
            db.session.commit()
