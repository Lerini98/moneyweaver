/*!
* Start Bootstrap - Business Frontpage v5.0.9 (https://startbootstrap.com/template/business-frontpage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-frontpage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

document.getElementById("openPopup").addEventListener("click", function(event) {
    event.preventDefault(); // 기본 링크 동작 방지
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
