from flask import render_template, request, jsonify, redirect, url_for, session, flash
from fully import app, db
from fully import login_manager
from .models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from permissions import USER_PERMISSIONS




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Helper function to check role permissions
def can_create(user_level, new_user_level):
    return new_user_level > user_level and new_user_level <= 10







# Home Page
@app.route('/home')
@app.route("/")
def home():
    return render_template('index.html')


@app.route('/restricted')
@login_required
def restricted():
    return render_template('ticket.html')


# Dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    user_level = session.get("user_level", current_user.level)  # Default to level 10 (public)
    menu_items = USER_PERMISSIONS.get(user_level, ["Public Home"])

    return render_template("dashboard.html", menu_items=menu_items, user=current_user)













# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        user = User.query.filter_by(username=data['username']).first()
        if user and check_password_hash(user.password, data['password']):
            login_user(user)
            print(user)
            flash('Your account has been logged in', 'success')
            return redirect(url_for('dashboard'))
        return "Invalid credentials", 401
    return render_template('login.html')



# Register User
@app.route('/register', methods=['POST'])
@login_required
def register():
    if request.method == 'POST':
        if current_user.level >= 10:
            return jsonify({'error': 'Permission denied'}), 403
    
        data = request.form
        username = data['username']
        password = generate_password_hash(data['password'])
        level = int(data['level'])
        
        if not can_create(current_user.level, level):
            flash("Invalid level selected!", "danger")
            #return jsonify({'error': 'You cannot create this user level'}), 403
            return redirect(url_for('dashboard'))
         
        new_user = User(username=username, password=password, level=level)
        db.session.add(new_user)
        db.session.commit()
        flash(f"User {username} created successfully!", "success")

        return redirect(url_for('dashboard'))
    return render_template('create_user.html')