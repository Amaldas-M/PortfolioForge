// Toggle Style Switcher
const styleSwitcherToggle = document.querySelector(".style-switcher-toggler");
styleSwitcherToggle.addEventListener("click", () => {
    document.querySelector(".style-switcher").classList.toggle("open");
});

// Hide Style Switcher on Scroll
window.addEventListener("scroll", () => {
    if (document.querySelector(".style-switcher").classList.contains("open")) {
        document.querySelector(".style-switcher").classList.remove("open");
    }
});

// Theme Colors
const alternateStyles = document.querySelectorAll(".alternate-style");

function setActiveStyle(color) {
    alternateStyles.forEach((style) => {
        if (color === style.getAttribute("title")) {
            style.removeAttribute("disabled");
            // Save the selected color in localStorage
            localStorage.setItem("theme-color", color);
        } else {
            style.setAttribute("disabled", "true");
        }
    });
}

// Check if a theme color is already set in localStorage and apply it
const savedColor = localStorage.getItem("theme-color");
if (savedColor) {
    setActiveStyle(savedColor);
}


document.addEventListener("DOMContentLoaded", () => {
    const dayNight = document.querySelector(".day-night");
    const icon = dayNight.querySelector("i");

    // Check localStorage for dark mode preference
    if (localStorage.getItem("darkMode") === "enabled") {
        document.body.classList.add("dark");
        icon.classList.add("fa-sun");
        icon.classList.remove("fa-moon");
    } else {
        document.body.classList.remove("dark");
        icon.classList.add("fa-moon");
        icon.classList.remove("fa-sun");
    }

    dayNight.addEventListener("click", () => {
        document.body.classList.toggle("dark");

        if (document.body.classList.contains("dark")) {
            icon.classList.add("fa-sun");
            icon.classList.remove("fa-moon");
            localStorage.setItem("darkMode", "enabled");
        } else {
            icon.classList.add("fa-moon");
            icon.classList.remove("fa-sun");
            localStorage.setItem("darkMode", "disabled");
        }
    });
});
