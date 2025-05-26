document.addEventListener("DOMContentLoaded", function () {
    const popup = document.getElementById("popup-banner");
    const closeButton = document.getElementById("close-popup");

    // Show the popup after 2 seconds
    setTimeout(() => {
        popup.style.display = "flex";
    }, 2000);

    // Close the popup when the close button is clicked
    closeButton.addEventListener("click", () => {
        popup.style.display = "none";
    });

    // Optional: Close the popup when clicking outside the content box
    popup.addEventListener("click", (event) => {
        if (event.target === popup) {
            popup.style.display = "none";
        }
    });
});