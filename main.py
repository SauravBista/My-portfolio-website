from flask import Flask, render_template

app = Flask(__name__)

# Sample blog posts (you can uncomment this if you want to use it later)
# data = [
#     {"title": "My First Blog Post", "date": "2024-01-31", "content": "This is my first blog post content."},
#     {"title": "Exploring the Himalayas", "date": "2024-02-15", "content": "A journey through the Himalayas and what I learned."}
# ]

@app.route('/')
def home():
    profile = {
            "name": "Saurav Bista",
            "title": "Tech Enthusiast | StoryTeller",
            "linkedin": "https://www.linkedin.com/in/sauravbista",
            "email": "saurav@example.com",
            "instagram": "https://www.instagram.com/sauravbista",
        }
    return render_template('index.html', profile=profile)  # Renders the index page


@app.route('/gallery')
def gallery():
    
    profile = {
        "name": "Saurav Bista",
        "title": "Tech Enthusiast | StoryTeller",
        "linkedin": "https://www.linkedin.com/in/sauravbista",
        "email": "saurav@example.com",
        "instagram": "https://www.instagram.com/sauravbista",
    }

    gallery_images = [
        {"src": "/static/gallery-website/main1.JPG", "alt": "Gallery Image 1", "location": "Pumdikot, Pokhara", "description": "Shiva, the destroyer of the universe." },
        {"src": "/static/gallery-website/main2.JPG", "alt": "Gallery Image 2", "location": "Lete Mustang", "description": "Annapurna I, 8077M" },
        {"src": "/static/gallery-website/main3.jpg", "alt": "Gallery Image 3", "location": "Na Village, Rolwaling Valley", "description": "Will snow in about 10 minutes" },
        {"src": "/static/gallery-website/main4.jpg", "alt": "Gallery Image 4", "location": "Na Village, Rolwaling Valley", "description": "Ma ta Nepali Babu, Made in Nepal" },
        {"src": "/static/gallery-website/image1.jpg", "alt": "Gallery Image 5", "location": ", Muktinath", "description": "A beautiful view of the Eiffel Tower." },
        {"src": "/static/gallery-website/image2.jpg", "alt": "Gallery Image 6", "location": "Paris, France", "description": "A beautiful view of the Eiffel Tower." },
        {"src": "/static/gallery-website/image3.jpg", "alt": "Gallery Image 7", "location": "Sailung, Dolakha", "description": "Majestic sunrise from Sailung." },
        {"src": "/static/gallery-website/image4.jpg", "alt": "Gallery Image 8", "location": "Marpha, Mustang", "description": "Riding my way to Liberation" },
        {"src": "/static/gallery-website/image5.jpg", "alt": "Gallery Image 9", "location": "Paris, France", "description": "A beautiful view of the Eiffel Tower." },
        {"src": "/static/gallery-website/image6.JPG", "alt": "Gallery Image 1", "location": "Pumdikot, Pokhara", "description": "Shiva, the destroyer of the universe." },
        {"src": "/static/gallery-website/image7.JPG", "alt": "Gallery Image 2", "location": "Lete Mustang", "description": "Annapurna I, 8077M" },
        {"src": "/static/gallery-website/image15.jpg", "alt": "Gallery Image 3", "location": "Na Village, Rolwaling Valley", "description": "Will snow in about 10 minutes" },
        {"src": "/static/gallery-website/image9.jpg", "alt": "Gallery Image 4", "location": "Na Village, Rolwaling Valley", "description": "Ma ta Nepali Babu, Made in Nepal" },
        {"src": "/static/gallery-website/image10.jpg", "alt": "Gallery Image 5", "location": ", Muktinath", "description": "A beautiful view of the Eiffel Tower." },
        {"src": "/static/gallery-website/image11.jpg", "alt": "Gallery Image 6", "location": "Paris, France", "description": "A beautiful view of the Eiffel Tower." },
        {"src": "/static/gallery-website/image12.jpg", "alt": "Gallery Image 7", "location": "Sailung, Dolakha", "description": "Majestic sunrise from Sailung." },
        {"src": "/static/gallery-website/image13.jpg", "alt": "Gallery Image 8", "location": "Marpha, Mustang", "description": "Riding my way to Liberation" },
        {"src": "/static/gallery-website/image14.jpg", "alt": "Gallery Image 9", "location": "Paris, France", "description": "A beautiful view of the Eiffel Tower." },
       

    ]

    return render_template("gallery.html", profile=profile, gallery=gallery_images)

@app.route('/base')
def base():

    profile = {
            "name": "Saurav Bista",
            "title": "Tech Enthusiast | StoryTeller",
            "linkedin": "https://www.linkedin.com/in/sauravbista",
            "email": "saurav@example.com",
            "instagram": "https://www.instagram.com/sauravbista",
        }
    return render_template("base.html", profile=profile)


if __name__ == '__main__':
    app.run(debug=True)
