/**
 * myScript2.js
 * Manages fetching scholarship data from the Django API and 
 * handling the interactive UI (Grid & Modal).
 */

let scholarshipData = []; // Stores the array of scholarships from the API
let currentIndex = 0;

// Select DOM Elements
const modal = document.getElementById("scholarshipModal");
const closeBtn = document.querySelector(".close-btn");
const prevBtn = document.getElementById("prevScholarship");
const nextBtn = document.getElementById("nextScholarship");
const scrollArea = document.querySelector(".modal-scroll-area");
const scholarshipContainer = document.getElementById("scholarshipContainer");

/**
 * 1. FETCH DATA FROM DATABASE
 */
async function loadScholarships() {
    try {
        // Fetch from your Django API root
        const response = await fetch("http://127.0.0.1:8000/api/scholarships/");
        if (!response.ok) throw new Error("Network response was not ok");
        
        scholarshipData = await response.json();
        renderScholarshipCards();
    } catch (error) {
        console.error("Error loading scholarships from database:", error);
        scholarshipContainer.innerHTML = `<p style="color:red;">Failed to load scholarship data. Please try again later.</p>`;
    }
}

/**
 * 2. RENDER THE FRONTEND GRID
 */
function renderScholarshipCards() {
    scholarshipContainer.innerHTML = ""; // Clear placeholder content

    scholarshipData.forEach((item, index) => {
        // Injects buttons into the scholarship-grid defined in Scholarship_Information.html[cite: 1]
        scholarshipContainer.innerHTML += `
            <button class="btn2" onclick="openModal(${index})">
                <div class="scholarship-card">
                    <img src="${item.logo}" alt="${item.title}" class="card-logo" style="width:50px; height:50px; object-fit:contain;">
                    <h3>${item.title}</h3>
                    <div class="status-badge">Accepting</div>
                    <div class="date-text">Deadline: ${item.deadline}</div>
                </div>
            </button>
        `;
    });
}

/**
 * 3. UPDATE MODAL CONTENT
 */
function updateModalContent(index) {
    const data = scholarshipData[index];
    if (!data) return;

    // Map API keys to the IDs in Scholarship_Information.html[cite: 1, 2]
    document.getElementById("modalTitle").innerText = data.title;
    document.getElementById("modalDeadline").innerText = data.deadline;
    document.getElementById("modalLocation").innerText = data.location;
    document.getElementById("modalLevel").innerText = data.level;
    document.getElementById("modalAmount").innerText = data.amount;
    document.getElementById("modalType").innerText = data.scholarship_type;
    document.getElementById("modalContract").innerText = data.contract;
    
    // Update Logo
    const modalLogo = document.getElementById("modalLogo");
    if (data.logo) {
        modalLogo.src = data.logo;
    }

    // Update Application Link
    const linkElement = document.getElementById("modalLink");
    if (data.link) {
        linkElement.href = data.link;
        linkElement.style.display = "inline-block";
    } else {
        linkElement.style.display = "none";
    }

    // Handle Courses (Targeting 'name' property to avoid [object Object])
    const courseContainer = document.getElementById("modalCourses");
    if (data.courses && Array.isArray(data.courses) && data.courses.length > 0) {
        courseContainer.innerHTML = data.courses.map(c => `<div>• ${c.name}</div>`).join("");
    } else {
        courseContainer.innerHTML = "<div>Contact provider for details</div>";
    }

    // Handle Criteria (Targeting 'text' property to avoid [object Object])[cite: 2]
    const criteriaContainer = document.getElementById("modalCriteria");
    if (data.criteria && Array.isArray(data.criteria) && data.criteria.length > 0) {
        criteriaContainer.innerHTML = data.criteria.map(c => `<li>${c.text}</li>`).join("");
    } else {
        criteriaContainer.innerHTML = "<li>Refer to official website for full criteria.</li>";
    }

    // Update Pagination Button States[cite: 2]
    prevBtn.disabled = index === 0;
    nextBtn.disabled = index === scholarshipData.length - 1;

    // Reset scroll to top of modal[cite: 1]
    scrollArea.scrollTop = 0;
}

/**
 * 4. EVENT LISTENERS & NAVIGATION
 */

// Function called by the grid buttons
window.openModal = function(index) {
    currentIndex = index;
    updateModalContent(index);
    modal.style.display = "block";
};

// Pagination: Previous
prevBtn.addEventListener("click", () => {
    if (currentIndex > 0) {
        currentIndex--;
        updateModalContent(currentIndex);
    }
});

// Pagination: Next
nextBtn.addEventListener("click", () => {
    if (currentIndex < scholarshipData.length - 1) {
        currentIndex++;
        updateModalContent(currentIndex);
    }
});

// Close Modal Logic[cite: 2]
closeBtn.onclick = () => {
    modal.style.display = "none";
};

window.onclick = (event) => {
    if (event.target === modal) {
        modal.style.display = "none";
    }
};

// Start the process on page load
document.addEventListener("DOMContentLoaded", loadScholarships);