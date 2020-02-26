var button = $("#start_button");
var button2 = $("#playback_button");
var button3 = $("#send_text");

// start button, starts sound board
button.click(function() {
	console.log(button.text());
	if (button.text() === "Start Playing") {
		$.ajax({
			url: "/start_on",
			type: "post",
			success: function(response) {
				console.log(response);
				button.text("Stop Playing");
			}
		});
	} else {
		$.ajax({
			url: "/end_now",
			type: "post",
			success: function() {
				button.text("Start Playing");
			}
		})
	}
});

// Playback Sounds Button, plays back last recording
button2.click(function() {
	console.log(button2.text());
	if (button2.text() === "Playback Sounds") {
		$.ajax({
			url: "/playback",
			type: "post",
			success: function(response) {
				console.log(response);
				button2.text("Stop Play Back");
			}
		});
	} else {
		$.ajax({
			url: "/stop_playback",
			type: "post",
			success: function() {
				button2.text("Playback Sounds");
			}
		})
	}
});

// Send audio file as text message, gets user input as phone number, passes value to flask app
button3.click(function() {
	console.log(button3.text());
	if (button3.text() === "Send Audio File") {
		// get textmessage number value from html file, holds users phone number
		var phonenum = document.getElementById("textmessage").value;
		console.log(phonenum)
		$.ajax({
			url: "/sendtext",
			type: "get",
			data: {
				// passes phonenum as parameter
				phoneparam: phonenum
			},
			success: function(response) {
				console.log(response)
			}
		});
	}
});
