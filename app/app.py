from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (DATABASE_URL)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersecretkey")

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text, nullable=True)
    done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Todo {self.id} {self.title}>"


@app.before_request
def create_tables():
    db.create_all()


@app.route("/")
def index():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return render_template("index.html", todos=todos)


@app.route("/new", methods=["GET", "POST"])
def new_todo():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        if not title:
            flash("Title is required.", "danger")
            return redirect(url_for("new_todo"))
        todo = Todo(
            title=title.strip(),
            description=description.strip() if description else None,
        )
        db.session.add(todo)
        db.session.commit()
        flash("Todo created!", "success")
        return redirect(url_for("index"))
    return render_template("new.html")


@app.route("/toggle/<int:todo_id>")
def toggle_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    flash("Todo deleted.", "info")
    return redirect(url_for("index"))


@app.route("/edit/<int:todo_id>", methods=["GET", "POST"])
def edit_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        if not title:
            flash("Title is required.", "danger")
            return redirect(url_for("edit_todo", todo_id=todo_id))
        todo.title = title.strip()
        todo.description = description.strip() if description else None
        db.session.commit()
        flash("Todo updated!", "success")
        return redirect(url_for("index"))
    return render_template("edit.html", todo=todo)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
