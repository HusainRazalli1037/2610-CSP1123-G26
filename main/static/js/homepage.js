let currentIndex = 0;
const track = document.querySelector(".hot-slider-track");
const cards = document.querySelectorAll(".hot-card");
const nextBtn = document.querySelector(".next");
const prevBtn = document.querySelector(".prev");

function updateSlider() {
  const cardWidthWithGap = 220; // 200px card + 20px gap
  const moveDistance = currentIndex * cardWidthWithGap;

  // Move the track
  track.style.transform = `translateX(-${moveDistance}px)`;

  // Update which card looks "active" (the middle one)
  cards.forEach((card, index) => {
    card.classList.remove("active-card");
    // In a 3-card view, the active card is index + 1 relative to the current start
    if (index === currentIndex + 1) {
      card.classList.add("active-card");
    }
  });
}

nextBtn.addEventListener("click", () => {
  // We stop moving when the last 3 cards are visible
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

// Initial call to set the state
updateSlider();

/* --- KEEP YOUR EXISTING MODAL FUNCTIONS BELOW --- */
function showMessage(msg) {
  const modal = document.getElementById("scholarModal");
  const text = document.getElementById("scholarMessageText");
  text.innerText = msg;
  modal.style.display = "block";
}

function closeScholarModal() {
  document.getElementById("scholarModal").style.display = "none";
}

window.onclick = function (event) {
  const modal = document.getElementById("scholarModal");
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

// Function to handle the "From Scholars" Messages
function showMessage(msg) {
  const modal = document.getElementById("scholarModal");
  const text = document.getElementById("scholarMessageText");

  text.innerText = msg;
  modal.style.display = "block";
}

function closeScholarModal() {
  document.getElementById("scholarModal").style.display = "none";
}

// Close modal if user clicks outside of it
window.onclick = function (event) {
  const modal = document.getElementById("scholarModal");
  if (event.target == modal) {
    modal.style.display = "none";
  }
};


let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
