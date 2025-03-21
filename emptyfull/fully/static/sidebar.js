// Sidebar Dropdown Toggle
document.addEventListener("DOMContentLoaded", function () {
    let dropdowns = document.querySelectorAll(".dropdown-btn");

    dropdowns.forEach((btn) => {
        btn.addEventListener("click", function () {
            let dropdownContent = this.nextElementSibling;
            dropdownContent.style.display =
                dropdownContent.style.display === "block" ? "none" : "block";
        });
    });
});
