/**
 * MyLuanier Homepage Logic
 * Handles the "What's Hot" Slider and Scholar Message Modals
 */

document.addEventListener("DOMContentLoaded", () => {
    // --- SLIDER LOGIC ---
    let currentIndex = 0;
    const track = document.querySelector(".hot-slider-track");
    const cards = document.querySelectorAll(".hot-card");
    const nextBtn = document.querySelector(".next");
    const prevBtn = document.querySelector(".prev");

    // Only run slider logic if elements exist on the page
    if (track && cards.length > 0) {
        function updateSlider() {
            const cardWidthWithGap = 220; // 200px card + 20px gap
            const moveDistance = currentIndex * cardWidthWithGap;

            // Move the track
            track.style.transform = `translateX(-${moveDistance}px)`;

            // Update which card looks "active" (centered)
            cards.forEach((card, index) => {
                card.classList.remove("active-card");
                // Highlights the second card in the current view
                if (index === currentIndex + 1) {
                    card.classList.add("active-card");
                }
            });
        }

        nextBtn.addEventListener("click", () => {
            if (currentIndex < cards.length - 3) {
                currentIndex++;
                updateSlider();
            }
        });

        prevBtn.addEventListener("click", () => {
            if (currentIndex > 0) {
                currentIndex--;
                updateSlider();
            }
        });

        // Initial call
        updateSlider();
    }
});

// --- MODAL FUNCTIONS ---
// These are kept in the global scope so the onclick="" in your HTML can find them
function showMessage(msg) {
    const modal = document.getElementById("scholarModal");
    const text = document.getElementById("scholarMessageText");
    if (modal && text) {
        text.innerText = msg;
        modal.style.display = "block";
    }
}

function closeScholarModal() {
    const modal = document.getElementById("scholarModal");
    if (modal) {
        modal.style.display = "none";
    }
}

// Close modal if user clicks outside the modal content
window.addEventListener("click", (event) => {
    const modal = document.getElementById("scholarModal");
    if (event.target === modal) {
        modal.style.display = "none";
    }
});