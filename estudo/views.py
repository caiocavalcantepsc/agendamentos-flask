from estudo import app, db
from flask import render_template, url_for, request, redirect
from estudo.models import Contato 
from estudo.forms import ContatoForm, Userform, LoginForm
from flask import request
from flask_login import login_user, logout_user, current_user, login_manager

@app.route('/', methods=['GET', 'POST'])
def homepage():

    form = LoginForm()
    if form.validate_on_submit():
        user=form.login()
        login_user(user, remember=True)
        return redirect(url_for('usuario'))

    return render_template('index.html', form=form)

@app.route('/usuario/')
def usuario():
    return render_template('usuario.html')

@app.route('/cadastro/', methods=['GET', 'POST'])
def cadastro():

    form = Userform()
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    return render_template('cadastro.html', form=form)

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    context = {}

    if form.validate_on_submit():
        form.save()
        return redirect(url_for('contato'))

    return render_template('contato.html', context=context, form=form)

@app.route('/contato/lista/')
def contatoLista():

    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')

    dados = Contato.query
    if pesquisa != '':
        dados = dados.filter_by(nome=pesquisa)

    
    context = {'dados': dados.all()}
    
    return render_template('contato_lista.html', context=context)

@app.route('/contato/deletar/<int:id>/', methods=['POST'])
def contatoDeletar(id):
    contato = Contato.query.get_or_404(id)

    db.session.delete(contato)
    db.session.commit()

    return redirect(url_for('contatoLista'))

@app.route('/contato/lista/<int:id>/')
def contatoDetalhe(id):

    objeto = Contato.query.get(id)

    context ={'objeto': objeto}
    
    return render_template('contato_detalhe.html', context=context, objeto=objeto, voltar=request.referrer)


#Forma não recomendada

# @app.route('/contato_old/', methods=['GET', 'POST'])
# def contato_old():
#     form = ContatoForm
#     context = {}

#     if request.method == 'POST':
#         nome = request.form['nome']
#         email = request.form['email']
#         assunto = request.form['assunto']
#         mensagem = request.form['mensagem']

#         contato = Contato(
#             nome=nome,
#             email=email,
#             assunto=assunto,
#             mensagem=mensagem
#         )

#         db.session.add(contato)
#         db.session.commit()

#         context['sucesso'] = True
#         return render_template('contato.html', context=context)

#     # GET
#     pesquisa = request.args.get('pesquisa')
#     context['pesquisa'] = pesquisa

#     return render_template('contato.html', context=context, fo