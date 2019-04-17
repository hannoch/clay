
function googleHack(){
    var doc =$("#resulte-div").html("");
	var v = $("#googlehack-input").val();
	var i = 0;
	var x = "";
	var hack = new Array(
		"https://www.google.com/search?q=site:" + v + "+intitle:index.of",
		"https://www.google.com/search?q=site:" + v + "+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini",
		"https://www.google.com/search?q=site:" + v + "+ext:sql+|+ext:dbf+|+ext:mdb",
		"https://www.google.com/search?q=site:" + v + "+ext:log",
		"https://www.google.com/search?q=site:" + v + "+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup",
		"https://www.google.com/search?q=site:" + v + "+inurl:login",
		"https://www.google.com/search?q=site:" + v + "+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mysql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warning:+pg_connect()%22",
		"https://www.google.com/search?q=site:" + v + "+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv",
		"https://www.google.com/search?q=site:" + v + "+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22",
        'https://www.google.com/search?q=intitle:'+ v + ' intext:"Login to the Administrative Interface"'

	)
	var txt = new Array(
		"Directory Traversal",
		"Config File Leak",
		"Data File Leak",
		"Log File Leak",
		"Backup && History",
		"Login Page",
		"SQL Error",
		"Public File",
		"phpinfo()",
        "Web2Py",

	)

	while (i<10)
	{
		doc.append("<br><br><a href='" + hack[i] + "' target='__blank'>" + txt[i] + "</a>");
		i++;
	}
	//alert(doc.html());
}