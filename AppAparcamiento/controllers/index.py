from flask import render_template
class index():
    def __init__(self):
        pass

    def index(self):
        return render_template('index.html')
