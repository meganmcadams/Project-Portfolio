from flask import Flask, request, render_template, url_for, redirect

# Initialize Flask app
app = Flask(__name__)

# PAGES
@app.route('/')
def page_index():    
    return render_template('index.html')

@app.route('/projects')
def page_projects():
    return render_template('projects.html')

@app.route('/awards')
def page_awards():
    return render_template('awards.html')

@app.route('/professional-experience')
def page_professional_experience():
    return render_template('professional_experience.html')

# TESTING
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 2020))
    app.run(debug=True, threaded=False, host='0.0.0.0', port=port)
