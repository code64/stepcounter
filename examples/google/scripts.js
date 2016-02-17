function get_spreadsheet() {
	$.getJSON("https://spreadsheets.google.com/feeds/list/SPREADSHEET_KEY/WORKSHEED_ID/public/values?alt=json", function(data) {
		document.getElementById('steps').innerHTML = data.feed.entry[0]['gsx$steps']['$t'];
		document.getElementById('meters').innerHTML = data.feed.entry[0]['gsx$meters']['$t'];
  	});
}

setInterval(get_spreadsheet, 1000);