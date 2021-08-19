
from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask
import json
from flask import Response

def get_subtl(v_id):
        
    srt = YouTubeTranscriptApi.get_transcript(v_id)




    return srt


app = Flask(__name__)

@app.route("/")
def hello_world(v_id):
    
    return "hi"
    
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')    
