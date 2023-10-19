document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll(".links a");

    links.forEach(link => {
        link.addEventListener("click", function(event) {
            // Prevent the default link behavior
            event.preventDefault();

            // Remove the "active" class from all links
            links.forEach(link => {
                link.classList.remove("active");
            });

            // Add the "active" class to the clicked link
            this.classList.add("active");
        });
    });
});