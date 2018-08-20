let cameraOn = false;



const toggleCamera = () => {
	let camReq = new XMLHttpRequest();
	camReq.open("GET", "/cam", true);

	camReq.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
		  console.log(this.responseText);
		  cameraOn = !cameraOn;
		  let active = cameraOn ? "active":"";
		  document.querySelector(".cam").classList.add(active);
		}
	};
	
	camReq.send();
};