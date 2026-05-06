/**
 * pathwayScript.js
 * Dynamically fetches pathway/course data from the Django database
 * and displays it in a modal based on the selected University.
 */

const modal = document.getElementById("pathwayModal");
const closeBtn = document.querySelector(".close-btn");
const container = document.getElementById("modalPathways");
const modalLogo = document.getElementById("modalLogo");

// Global variable to store fetched data
let allPathwayData = [];

/**
 * 1. FETCH ALL PATHWAY DATA ON PAGE LOAD
 */
async function loadAllPathwayData() {
    try {
        // Fetch from the API endpoint defined in your urls.py
        const response = await fetch("/api/scholarships/"); // Ensure this endpoint returns your PathwayHub/Course data
        allPathwayData = await response.json();
        console.log("Pathway data loaded successfully.");
    } catch (error) {
        console.error("Error loading pathway data:", error);
    }
}

/**
 * 2. OPEN MODAL & FILTER DATA BY UNIVERSITY
 * @param {string} uniName - The name of the university (from img alt)
 */
function openPathwayModal(uniName) {
    // Filter the global data for courses belonging to the clicked university
    // We use .toLowerCase() and .trim() to ensure a match regardless of formatting
    const filteredCourses = allPathwayData.filter(course => 
        course.university.toLowerCase().trim() === uniName.toLowerCase().trim()
    );

    if (filteredCourses.length === 0) {
        container.innerHTML = `<div class="no-data">No courses found for ${uniName}.</div>`;
        modalLogo.src = ""; // Clear logo if no data
    } else {
        // Set the logo from the first course found for this university
        modalLogo.src = filteredCourses[0].logo || "";

        // Map the filtered array into HTML boxes
        container.innerHTML = filteredCourses.map(course => `
            <div class="course-box">
                <div class="course-code">${course.code}</div>
                <div class="course-name">${course.name}</div>
                <div class="course-uni">${course.university}</div>
                <div class="course-details-grid">
                    <div class="detail-tag">${course.level}</div>
                    <div class="detail-tag">Merit: ${course.merit}%</div>
                    <div class="detail-tag">${course.duration}</div>
                    <div class="detail-tag">${course.course_type}</div>
                </div>
            </div>
        `).join("");
    }

    modal.style.display = "block";
}

/**
 * 3. EVENT LISTENERS
 */

// Handle clicking on University Cards (the Grid)
document.querySelectorAll(".uni-card").forEach((card) => {
    card.addEventListener("click", () => {
        // The alt text of the image must match the 'university' field in your DB
        const uniName = card.querySelector("img").alt;
        openPathwayModal(uniName);
    });
});

// Close Modal Logic
if (closeBtn) {
    closeBtn.onclick = () => (modal.style.display = "none");
}

window.onclick = (event) => {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};

// Initial Load
document.addEventListener("DOMContentLoaded", loadAllPathwayData);