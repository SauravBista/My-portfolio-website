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
    profile = {
        "name": "Saurav Bista",
        "title": "Tech Enthusiast | StoryTeller",
        "linkedin": "https://www.linkedin.com/in/sauravbista",
        "email": "sauravbista10@gmail.com",
        "instagram": "https://www.instagram.com/saurav___bista",
    }

    gallery_images = [
        {"src": "/static/gallery-website/main1.JPG", "alt": "Gallery Image 1"},
        {"src": "/static/gallery-website/main2.JPG", "alt": "Gallery Image 2"},
        {"src": "/static/gallery-website/main3.jpg", "alt": "Gallery Image 3"},
        {"src": "/static/gallery-website/main4.jpg", "alt": "Gallery Image 4"},
        {"src": "/static/gallery-website/main4.jpg", "alt": "Gallery Image 4"},
        {"src": "/static/gallery-website/main4.jpg", "alt": "Gallery Image 4"},
        {"src": "/static/gallery-website/main4.jpg", "alt": "Gallery Image 4"},
        {"src": "/static/gallery-website/main4.jpg", "alt": "Gallery Image 4"},
    ]

    return render_template("gallery.html", profile=profile, gallery=gallery_images)

if __name__ == '__main__':
    app.run(debug=True)
