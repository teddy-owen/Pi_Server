
const toggleCamera = () => $.post( "/cam", {toggle:true}, (resp) => console.log(resp));