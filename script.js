// Smooth scroll
document.querySelectorAll("a").forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href"))
        ?.scrollIntoView({ behavior: "smooth" });
    });
});

// Simple fade animation on scroll
const cards = document.querySelectorAll(".card");

window.addEventListener("scroll", () => {
    cards.forEach(card => {
        const top = card.getBoundingClientRect().top;
        if (top < window.innerHeight - 50) {
            card.style.opacity = 1;
            card.style.transform = "translateY(0)";
        }
    });
});

const btn = document.getElementById("projectBtn");
const section = document.getElementById("projectSection");

btn.addEventListener("click", () => {
    section.classList.toggle("hidden");

    if (!section.classList.contains("hidden")) {
        section.scrollIntoView({ behavior: "smooth" });
    }
});