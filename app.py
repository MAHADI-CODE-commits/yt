from flask import Flask, request, jsonify
import youtube_dl

app = Flask(__name__)

# Endpoint to download video
@app.route('/download', methods=['POST'])
def download_video():
    url = request.json.get('url')
    # Code to download video
    with youtube_dl.YoutubeDL() as ydl:
        ydl.download([url])
    return jsonify({'message': 'Video downloaded successfully'}), 200

# Endpoint to get video information
@app.route('/get-info', methods=['POST'])
def get_video_info():
    url = request.json.get('url')
    with youtube_dl.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
    return jsonify(info_dict), 200

# Endpoint to check download status (Dummy Implementation)
@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'No downloads in progress'}), 200

if __name__ == '__main__':
    app.run(debug=True)