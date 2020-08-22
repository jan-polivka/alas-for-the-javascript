@echo off
echo Running Flask
D:
cd D:\alas-for-the-javascript
CALL venv\Scripts\activate
set FLASK_APP=main.py
flask run -h 10.0.0.74
pause