let btn = document.getElementById("send-data");
btn.addEventListener("click", () => {
	console.log("Sending data");
	btn.innerHTML = "refresh";
	btn.setAttribute("disabled", true);
	setTimeout(() => {
		btn.innerHTML = "send";
		btn.setAttribute("disabled", false);
	}, 1000);
})