from flask import Blueprint, render_template



# Create a Blueprint for menu-related routes
menu_bp = Blueprint("menu", __name__, )


@menu_bp.route("/dashboard", endpoint="dashboard")  # Explicitly set endpoint
def dashboard():
    return render_template("dashboard.html", title="Dashboard")

@menu_bp.route("/manage_users", endpoint="manage_users")
def manage_users():
    return render_template("manage_users.html", title="Manage Users")

@menu_bp.route("/create_user", endpoint="create_user", methods=['POST'])
def create_user():
    return render_template("create_user.html", title="Create User")

@menu_bp.route("/edit_user", endpoint="edit_user")
def edit_user():
    return render_template("edit_user.html", title="Edit User")

@menu_bp.route("/delete_user", endpoint="delete_user")
def delete_user():
    return render_template("delete_user.html", title="Delete User")

@menu_bp.route("/reports", endpoint="reports")
def reports():
    return render_template("reports.html", title="Reports")

@menu_bp.route("/sales_report", endpoint="sales_report")
def sales_report():
    return render_template("sales_report.html", title="Sales Report")

@menu_bp.route("/user_activity", endpoint="user_activity")
def user_activity():
    return render_template("user_activity.html", title="User Activity")

@menu_bp.route("/settings", endpoint="settings")
def settings():
    return render_template("settings.html", title="Settings")

@menu_bp.route("/general", endpoint="general")
def general():
    return render_template("general.html", title="General Settings")

@menu_bp.route("/security", endpoint="security")
def security():
    return render_template("security.html", title="Security Settings")

@menu_bp.route("/basic_reports", endpoint="basic reports")
def basic():
    return render_template("basic.html", title="basic reports")