from flask import Flask, jsonify
import sqlite3
import requests  # Импортируем requests для синхронных HTTP-запросов

app = Flask(__name__)

@app.route('/api/tasks', methods=["GET"])
def get_tasks():
    try:
        # Путь к базе данных (предположим, она лежит в папке MyReviewPanel)
        conn = sqlite3.connect("C:/Users/mrn-v/MyReviewPanel/tasks.db")  # Убедись, что путь правильный
        cursor = conn.cursor()
        cursor.execute("SELECT id, platform, description, city, direction, price FROM task")
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            tasks.append({
                'id': row[0],
                'platform': row[1],
                'description': row[2],
                'city': row[3],
                'direction': row[4],
                'price': row[5]
            })
        conn.close()
        return jsonify(tasks)
    except Exception as e:
        return jsonify({"error": str(e)})

# Запуск приложения Flask
if __name__ == "__main__":
    app.run(debug=True)