from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database: 10 songs
songs = [
    {"id": 1, "title": "Royal Symphony", "artist": "John Doe", "duration": "3:45", "file_url": "song1.mp3"},
    {"id": 2, "title": "Golden Melody", "artist": "Jane Smith", "duration": "4:05", "file_url": "song2.mp3"},
    # Add 8 more songs similarly
]

# Route: Get all songs
@app.route('/songs', methods=['GET'])
def get_songs():
    return jsonify(songs)

# Route: Search for a song by title
@app.route('/search', methods=['GET'])
def search_song():
    query = request.args.get('q', '').lower()
    results = [song for song in songs if query in song["title"].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
