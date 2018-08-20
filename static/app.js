let camReq = new XMLHttpRequest();
camReq.open("GET", "/cam", true);

const toggleCamera = () => camReq.send().then(resp => console.log(resp));