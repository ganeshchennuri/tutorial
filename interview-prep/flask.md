# Flask
## Basic setup
- Flask is lightweight python web framework
    ```python
    from flask import Flask, render_template, url_for, redirect

    app = Flask(__name__)

    @app.run('/', methods=['GET', 'HEAD','POST'])
    def index():
        return redirect(url_for('about'))

    @app.route('/about') 
    def about():
        return render_template('about.html')
    ```