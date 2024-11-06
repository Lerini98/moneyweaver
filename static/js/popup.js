// script.js
document.getElementById("openPopup").addEventListener("click", function() {
    document.getElementById("popup").style.display = "block";
});

document.querySelector(".close-button").addEventListener("click", function() {
    document.getElementById("popup").style.display = "none";
});

window.onclick = function(event) {
    if (event.target == document.getElementById("popup")) {
        document.getElementById("popup").style.display = "none";
    }
}
