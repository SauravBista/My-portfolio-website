from flask import Flask, render_template

app = Flask(__name__)

# Sample blog posts
# data = [
#     {"title": "My First Blog Post", "date": "2024-01-31", "content": "This is my first blog post content."},
#     {"title": "Exploring the Himalayas", "date": "2024-02-15", "content": "A journey through the Himalayas and what I learned."}
# ]

@app.route('/')
def home():
    return render_template('index.html')
    # return render_template('index.html', posts=data)

if __name__ == '__main__':
    app.run(debug=True)

# Ensure the templates directory exists and add an index.html file with Tailwind CSS
