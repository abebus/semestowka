from flask import render_template, redirect, url_for, request, flash, session
from app.routes.auth import bp
from app.forms import RegistrationForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from app.models import User
from app.extensions import db, bcrypt

import app.routes.auth.github_utils as gh
import app.routes.auth.forgot_pswrd_utils as pf


@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if session.get('authorized'):
        return redirect(url_for('main.index'))
    user = pf.verify_reset_token(token)
    form = ResetPasswordForm()
    if not user:
        return redirect(url_for('main.index'))
    else:
        if form.validate_on_submit():
            password = bcrypt.generate_password_hash(form.password.data)
            user.password = password
            db.session.commit()
            flash('Your password has been reset.')
            return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.jinja2', form=form)


@bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm(request.form)
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user:
            # Генерация токена для сброса пароля и отправка письма
            token = pf.get_reset_token(user.email)
            pf.send_reset_email(user, token)
            flash('Email with password reset instructions has been sent.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('User with this email does not exist.', 'danger')
    return render_template('auth/forgot_password.jinja2', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('authorized'):
        return redirect(url_for('main.index'))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        session['authorized'] = True
        user = User.query.filter_by(email=form.email.data).first()
        session['user_id'] = user.id
        return redirect(url_for('main.index'))
    return render_template('auth/login.jinja2', form=form)


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        password = bcrypt.generate_password_hash(form.password.data)
        user = User(login=form.username.data, email=form.email.data, password=password)
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        session['remember_me'] = form.remember_me.data
        session['authorized'] = True
        return redirect(url_for('main.index'))
    return render_template('auth/signup.jinja2', form=form)

@bp.route('/logout')
def logout():
    session['authorized'] = False
    session.clear()
    return redirect(url_for('main.index'))

@bp.route('/redirect_to_github')
def redirect_to_github():
    link = gh.generate_link(url_for('auth.from_github', _external=True))
    return redirect(link)

@bp.route('/from_github')
def from_github():
    code = request.args.get("code")
    if code is None:
        return redirect(url_for('main.index'))
    token = gh.get_token_by_code(code, url_for('auth.from_github', _external=True))
    user_info = gh.get_user_info(token)
    user = User.query.filter_by(email=user_info['email']).first()
    if not user:
        user = User(login=user_info['login'], email=user_info['email'], has_token=True, has_additional_info=True, additional_info=user_info)
        db.session.add(user)
        db.session.commit()
    session['authorized'] = True
    session['user_id'] = user.id

    return redirect(url_for('main.index'))

@bp.route('/redirect_to_google')
def redirect_to_google():
    ...

@bp.route('/from_google')
def from_google():
    ...
