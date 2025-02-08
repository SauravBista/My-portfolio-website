from flask import Flask, render_template

app = Flask(__name__)

# Sample blog posts (you can uncomment this if you want to use it later)
# data = [
#     {"title": "My First Blog Post", "date": "2024-01-31", "content": "This is my first blog post content."},
#     {"title": "Exploring the Himalayas", "date": "2024-02-15", "content": "A journey through the Himalayas and what I learned."}
# ]

@app.route('/')
def home():
    return render_template('index.html')  # Renders the index page

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')  # Renders the gallery page

if __name__ == '__main__':
    app.run(debug=True)
