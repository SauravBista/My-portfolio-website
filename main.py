from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json
from datetime import datetime
app = Flask(__name__)

# Sample blog posts (you can uncomment this if you want to use it later)
# data = [
#     {"title": "My First Blog Post", "date": "2024-01-31", "content": "This is my first blog post content."},
#     {"title": "Exploring the Himalayas", "date": "2024-02-15", "content": "A journey through the Himalayas and what I learned."}
# ]
profile = {
            "name": "Saurav Bista",
            "title": "Tech Enthusiast | StoryTeller",
            "linkedin": "https://www.linkedin.com/in/sauravbista",
            "email": "saurav@example.com",
            "instagram": "https://www.instagram.com/sauravbista",
        }
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

METADATA_FILE = 'static/uploads/metadata.json'

def load_metadata():
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_metadata(metadata):
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f)

@app.route('/gallery')
def gallery():
    

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
    return render_template("base.html", profile=profile)

app.secret_key = 'your_secret_key'

# Upload folder for images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB size limit

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)



# Helper function to check file extensions
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/contribution', methods=['GET', 'POST'])
def contribution():
    # Load existing metadata
    contributed_images = load_metadata()

    if request.method == 'POST':
        image = request.files['image']
        location = request.form['location']
        description = request.form['description']

        if image and allowed_file(image.filename):
            # Generate unique filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
            secure_filename = timestamp + image.filename
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename)
            
            # Save the image
            image.save(image_path)

            # Create metadata entry
            new_image = {
                "src": f"/static/uploads/{secure_filename}",
                "alt": f"Uploaded Image - {location}",
                "location": location,
                "description": description,
                "timestamp": datetime.now().isoformat()
            }

            # Add to metadata and save
            contributed_images.append(new_image)
            save_metadata(contributed_images)

            flash('Your image has been successfully uploaded!', 'success')
            return redirect(url_for('contribution'))
        else:
            flash('Please upload a valid image file (JPG, PNG, GIF).', 'danger')

    return render_template('contribution.html', profile=profile, contributed_images=contributed_images)
if __name__ == '__main__':
    app.run(debug=True)
