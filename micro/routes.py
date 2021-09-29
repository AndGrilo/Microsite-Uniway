from flask.globals import request
from micro import app, db
from flask import render_template, redirect, url_for, flash, request
from micro.forms import RegisterForm, IndicaForm, NaoIndicaForm, AmigoForm
from micro.models import User, Amigo
import datetime
from pytz import timezone

@app.route('/')
def nothing():
    return redirect(url_for('register_page'))
@app.route('/register', methods=["GET", "POST"])     #/register
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            Markt = request.form.get('mycheckbox')
            Marketing = "Nao"
            if Markt == "1":
                Marketing = "Sim"
            time_UTC = datetime.datetime.now(datetime.timezone.utc)
            Portugal = timezone('Portugal')
            timePt = time_UTC.astimezone(Portugal)
            a = str(timePt).partition('.')
        user_to_create = User(nome=form.nome.data, data_de_nascimento=form.data_de_nascimento.data, nif=form.nif.data, morada=form.morada.data, codigo_postal=form.codigo_postal.data, localidade=form.localidade.data, email=form.email.data, marketing = Marketing, tempo=a[0])
        db.session.add(user_to_create)
        db.session.commit()
        flash('Formulário preenchido com sucesso!', category='success')
        return redirect(url_for('indica_page'))

    if form.errors != {}:   #Se existirem erros
        for err_msg in form.errors.values():
            flash(f'Ocorreu um erro ao submeter o formulário: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/Indicar', methods=["GET", "POST"])      #Indicar um amigo
def indica_page():
    form = IndicaForm()
    
    if form.sim.data:
        return redirect(url_for('amigo_page'))
    if form.nao.data:
        return redirect(url_for('agradecimento_page'))
    return render_template('indicar.html', form=form)

@app.route('/Indicar2', methods=["GET", "POST"])
def indica_page_2():
    form = IndicaForm()
    
    if form.sim.data:
        return redirect(url_for('amigo_page'))
    if form.nao.data:
        return redirect(url_for('agradecimento_page'))
    return render_template('indicar2.html', form=form)

@app.route('/amigo', methods=["GET", "POST"])
def amigo_page():
    form = AmigoForm()
    if form.validate_on_submit():
        time_UTC = datetime.datetime.now(datetime.timezone.utc)
        Portugal = timezone('Portugal')
        timePt = time_UTC.astimezone(Portugal)
        b = str(timePt).partition('.')
        amigo = Amigo(nome=form.nome.data, telemovel=form.telemovel.data, email=form.email.data, tempo=b[0])
        db.session.add(amigo)
        db.session.commit()
        flash('Formulário preenchido com sucesso!', category='success')
        return redirect(url_for('indica_page_2'))

    if form.errors != {}:   #Se existirem erros
        for err_msg in form.errors.values():
            flash(f'Ocorreu um erro ao submeter o formulário: {err_msg}', category='danger')
        
    return render_template('amigo.html', form=form)

@app.route('/agradecimento')
def agradecimento_page():
    return render_template('agradecimento.html')