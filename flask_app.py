
from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask
import json
from flask import Response

def get_subtl(v_id):
        
    srt = YouTubeTranscriptApi.get_transcript(v_id)




    return srt


app = Flask(__name__)

@app.route("/<v_id>")
def hello_world(v_id):
    
    a =get_subtl(v_id)
    return Response(json.dumps(a),  mimetype='application/json')
    
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')    