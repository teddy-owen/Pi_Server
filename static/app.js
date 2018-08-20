let camReq = new XMLHttpRequest();
camReq.open("GET", "/cam", true);

camReq.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
	  console.log(this.responseText);
	}
};

const toggleCamera = () => camReq.send();