//Dropown menu animation

document.addEventListener("DOMContentLoaded", () => {
    const toggleBtn = document.querySelector(".toggle-btn");
    const dropdown = document.querySelector(".dropdown");

    toggleBtn.addEventListener("click", () => {
        dropdown.classList.toggle("open");
    });
});