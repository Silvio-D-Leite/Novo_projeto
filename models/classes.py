from organic import db



class Consumidor(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(15), nullable=False)
    endereco = db.Column(db.String(60), nullable=False)
    usuario = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(25), nullable=False)

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

    def __init__(self, nome, cpf, endereco, usuario, senha, email):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.usuario = usuario
        self.senha = senha
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name    



