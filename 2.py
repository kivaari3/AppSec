from flask import Flask, request
import subprocess

app = Flask(name)

@app.route("/dns")
def dns_lookup():
    hostname = request.values.get('hostname')
    cmd = 'nslookup ' + hostname
    output = subprocess.check_output(cmd, shell=True, text=True)  # Уязвимость
return output

if name == "main":
    app.run(debug=True)


"""
Уязвимости в коде:
    Использование небезопасного выполнения системных команд через модуль subprocess. Это может привести к выполнению произвольных команд на сервере.

Строки с уязвимостями:
    Строка 10:
    output = subprocess.check_output(cmd, shell=True, text=True)

Последствия эксплойтации уязвимостей:
    Злоумышленник может выполнить произвольные системные команды на сервере, что может привести к полному контролю над сервером, утечке конфиденциальных данных, удалению или изменению файлов.

Способы исправления уязвимостей:
    Использовать безопасные методы для выполнения системных команд.

Исправление:

import socket

@app.route("/dns")
def dns_lookup():
    hostname = request.values.get('hostname')
    try:
        ip_address = socket.gethostbyname(hostname)
        output = f'IP address of {hostname} is {ip_address}'
    except socket.gaierror:
        output = f'Unable to resolve hostname: {hostname}'
    return output
"""