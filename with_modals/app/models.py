# Aquí definiremos los modelos de datos que utilizaremos en nuestra aplicación.

from app import mysql


class Task:
    def create_task(self, title, description):
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO tasks (title, description) VALUES (%s, %s)",
            (title, description),
        )
        mysql.connection.commit()
        cur.close()

    def get_tasks(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tasks")
        tasks = cur.fetchall()
        cur.close()
        return tasks

    def get_task(self, id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tasks WHERE id = %s", (id,))
        task = cur.fetchone()
        cur.close()
        return task

    def update_task(self, id, title, description):
        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE tasks SET title = %s, description = %s WHERE id = %s",
            (title, description, id),
        )
        mysql.connection.commit()
        cur.close()

    def delete_task(self, id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM tasks WHERE id = %s", (id,))
        mysql.connection.commit()
        cur.close()
