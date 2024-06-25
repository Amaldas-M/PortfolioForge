document.addEventListener("DOMContentLoaded", () => {
    fetch('/service-names/')
        .then(response => response.json())
        .then(data => {
            var typed = new Typed(".typing", {
                strings: data,
                typeSpeed: 100,
                backSpeed: 50,
                loop: true
            });
        })
        .catch(error => console.error('Error fetching service names:', error));
});
