from ISStreamer.Streamer import Streamer
from flask import *
import sys
import json
from playtest import *
from threading import Thread

app = Flask(__name__)

credentials = json.load(open("credentials.json", "r"))
# start button, starts playsound()
@app.route("/start_on", methods=["POST"])
def start_on():
	startPlaying = Thread(target=playsound)
	startPlaying.start()
	return "ok"

# end button, stops playsound() by endsound()
@app.route("/end_now", methods=["POST"])
def end_now():
	soundoff = Thread(target=endsound)
	soundoff.start()
	return "ok"

# playback sound, passes recordings list to playback()
@app.route("/playback", methods=["POST"])
def playbacksounds():
	startrecording = Thread(target=playback, args=(recordings,))
	startrecording.start()
	return "ok"

# stops playback, starts stopplayback()
@app.route("/stop_playback", methods=["POST"])
def stop_playback():
	stoprecording = Thread(target=stopplayback)
	stoprecording.start()
	return "ok"

# gets phone number from js file, passes to snedtext(), gets ride of
# any symbols in number
@app.route("/sendtext", methods=["GET"])
def send_text():
	phonenum = request.args.get('phoneparam')
	final_phonenum = " "
	for i in phonenum:
		if i.isdigit():
			final_phonenum = final_phonenum + i
	sendtext(final_phonenum)
	return "ok"

@app.route('/is_sound', methods=['GET'])
def is_sound():
	return render_template("is_sound.html", name="Lauren Paicopolis")

@app.route('/', methods=['GET'])
def default():
	return redirect(url_for('is_sound'))

