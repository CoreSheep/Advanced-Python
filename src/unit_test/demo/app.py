from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Initialize posts as an empty list
posts = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET'])
def get_posts():
    # STEP 3: Return all posts as JSON with status code 200
    return jsonify(posts), 200

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()

    # STEP 4.2: Validate the data to ensure it exists, it has a 'title' and a 'content'
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    # STEP 4.3: Create a new post dictionary with an ID, title, and content from the data variable
    new_post = {
        'id': len(posts) + 1,
        'title': data['title'],
        'content': data['content']
    }
    
    # Append the new post to the 'posts' list
    posts.append(new_post)
    
    # Return the new post as JSON with a 201 Created status code
    return jsonify(new_post), 201

if __name__ == '__main__':
    app.run(debug=True)