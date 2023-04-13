from flask import render_template, redirect, flash, url_for, request
from flask_login import login_user, logout_user
from organic import app, lm, db
from models.forms import LoginForm
from models.classes import Consumidor

@lm.user_loader
def load_user(id):
    return Consumidor.query.filter_by(id=id).first()



#----------------------INDEX-------------------------#

@app.route('/', methods=["POST", "GET" ])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Consumidor.query.filter_by(email = form.email.data).first()
        if user and user.senha == form.senha.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("loja"))       
        else:
            flash("Invalid Login.")
        
    return render_template('index.html', form = form)  



#------------Rotas das páginas de erros--------------#

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500




#--------------Rotas para contas novas------------------#

@app.route('/novo_consumidor')
def novo_consumidor():
    return render_template('novo_consumidor.html')


# Criar consumidor novo
@app.route("/criar", methods=['POST', 'GET'])
def criar():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        endereco = request.form['endereco']
        usuario = request.form['usuario']
        senha = request.form['senha']
        email = request.form['email']
        consumidor = Consumidor.query.filter_by(usuario=usuario).first()
        if consumidor:
            flash("Usuário já existe.")
            return redirect(url_for('novo_consumidor'))
        else:
            new_consumidor = Consumidor(nome=nome, cpf=cpf, endereco=endereco, usuario=usuario, senha=senha, email=email )
            db.session.add(new_consumidor)
            db.session.commit()
            flash("Usuário cadastrado com sucesso.")
            return redirect(url_for('loja'))








@app.route('/novo_produtor')
def novo_produtor():
    return render_template('novo_produtor.html')


#--------------Rotas de testes------------------#


@app.route('/loja')
def loja():
    lista = Consumidor.query.order_by(Consumidor.nome)
    return render_template('loja.html', consumidores=lista )


