# Aquí definiremos las rutas de nuestra aplicación y las funciones controladoras.

from flask import render_template, request, redirect, url_for
from app import app
from app.models import Task

task = Task()


@app.route("/")
def index():
    try:
        tasks = task.get_tasks()
        return render_template("index.html", tasks=tasks)
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route("/create", methods=["GET", "POST"])
def create():
    try:
        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            task.create_task(title, description)
            return redirect(url_for("index"))
        return render_template("create.html")
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route("/read/<int:id>")
def read(id):
    try:
        task_info = task.get_task(id)
        return render_template("read.html", task=task_info)
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    try:
        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            task.update_task(id, title, description)
            return redirect(url_for("index"))
        task_info = task.get_task(id)
        return render_template("update.html", task=task_info)
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    try:
        if request.method == "POST":
            task.delete_task(id)
            return redirect(url_for("index"))
        task_info = task.get_task(id)
        return render_template("delete.html", task=task_info)
    except Exception as e:
        return f"An error occurred: {str(e)}"
