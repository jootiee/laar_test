from sql import *
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tabler = Tabler()

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST" :
        request_keys_list = list(request.form.keys())
        # Проверяю, является ли запрос нажатием на кнопку
        if len(request_keys_list):
            # Проверяю, нажатием на какую кнопку является запрос
            if request_keys_list[0] == "address":
                tabler.add_entry(request.form["address"])
            elif request_keys_list[0].isdigit():
                tabler.remove_entry(request_keys_list[0])
                
    # Заношу содержимое таблицы в переменную data, с помощью которой строю таблицу в index.html
    data = tabler.get_table()
    
    # Форматирую данные для копирования в буфер обмена
    data_to_copy = ""
    for line in data:
        if data_to_copy: data_to_copy += ", "
        data_to_copy += line[2]
        if line[3]:
            data_to_copy += ", " + line[3]
    
    return render_template("index.html", data=data, data_to_copy=data_to_copy)


if __name__ == "__main__":
    app.run(port=8800, debug=DEBUG)
    
    
"""
(4, 'vk.com', '87.240.132.78, 87.240.129.133, 87.240.137.164, 87.240.132.67, 87.240.132.72, 93.186.225.194', '')
(5, 'youtube.com', '142.250.180.14', '2a00:1450:4009:819::200e')
(6, 'yandex.ru', '77.88.55.60, 5.255.255.70, 5.255.255.77, 77.88.55.88', '2a02:6b8:a::a')
"""