let cameraOn = false;



const toggleCamera = () => {
	let camReq = new XMLHttpRequest();
	camReq.open("GET", "/cam", true);

	camReq.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
		  console.log(this.responseText);
		  if (this.responseText === 'on') {
			  document.querySelector(".cam").classList.add("active");
		  }else{
			  document.querySelector(".cam").classList.remove("active");
		  }
		}
	};

	camReq.send();
};