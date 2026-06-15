/**
 * pathwayScript.js
 * Dynamically fetches pathway/course data from the Django database
 * and displays it in a modal based on the selected University.
 */

const modal = document.getElementById("pathwayModal");
const closeBtn = document.querySelector(".close-btn");
const container = document.getElementById("modalPathways");
const modalLogo = document.getElementById("modalLogo");

// Global variable to store fetched data from the database
let allPathwayData = [];

/**
 * 1. FETCH ALL PATHWAY DATA ON PAGE LOAD
 * This targets the dedicated Pathway Hub API endpoint.
 */
async function loadAllPathwayData() {
    try {
        // Fetch from the API endpoint registered in your urls.py
        const response = await fetch("/api/pathway-hub/"); 
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        allPathwayData = await response.json();
        console.log("Pathway Hub data loaded successfully:", allPathwayData);
    } catch (error) {
        console.error("Error loading pathway data:", error);
        if (container) {
            container.innerHTML = `<div class="error-msg" style="color: white; text-align: center; padding: 20px;">
                Failed to connect to the database. Please ensure your Django server is running.
            </div>`;
        }
    }
}

/**
 * 2. OPEN MODAL & FILTER DATA BY UNIVERSITY
 * @param {string} uniName - The name of the university extracted from the image ALT text.
 */
function openPathwayModal(uniName) {
    if (!uniName) return;

    console.log("Searching for university:", uniName);

    // Filter the global data for courses belonging to the clicked university
    // Uses toLowerCase() and trim() to handle any formatting differences in the database
    const filteredCourses = allPathwayData.filter(course => 
        course.university && course.university.toLowerCase().trim() === uniName.toLowerCase().trim()
    );

    if (filteredCourses.length === 0) {
        // Helpful error message if no match is found
        container.innerHTML = `
            <div class="no-data" style="color: white; text-align: center; width: 100%; padding: 40px;">
                <h3>No courses found for "${uniName}".</h3>
                <p>Check if the University name in Django Admin matches the image ALT text exactly.</p>
            </div>`;
        modalLogo.src = ""; 
    } else {
        // Set the logo from the first course entry found for this university
        // If the logo field in Django is empty, it falls back to a placeholder
        modalLogo.src = filteredCourses[0].logo || "";

        // Map the filtered array into the horizontal scrollable course boxes
        container.innerHTML = filteredCourses.map(course => `
            <div class="course-box">
                <div class="course-code">${course.code || 'N/A'}</div>
                <div class="course-name">${course.name || 'Unknown Program'}</div>
                <div class="course-uni">${course.university}</div>
                <div class="course-details-grid">
                    <div class="detail-tag">${course.level || 'Degree/Diploma'}</div>
                    <div class="detail-tag">Merit: ${course.merit ? course.merit : '0.00'}%</div>
                    <div class="detail-tag">${course.duration || 'N/A'}</div>
                    <div class="detail-tag">${course.course_type || 'General'}</div>
                </div>
            </div>
        `).join("");
    }

    // Display the modal
    if (modal) {
        modal.style.display = "block";
        document.body.style.overflow = "hidden"; // Prevent background scrolling
    }
}

/**
 * 3. EVENT LISTENERS
 */

// Handle clicking on University Cards in the grid
document.querySelectorAll(".uni-card").forEach((card) => {
    card.addEventListener("click", () => {
        const imgElement = card.querySelector("img");
        if (imgElement) {
            const uniName = imgElement.alt;
            openPathwayModal(uniName);
        }
    });
});

// Close Modal Logic using the 'X' button
if (closeBtn) {
    closeBtn.onclick = () => {
        modal.style.display = "none";
        document.body.style.overflow = "auto"; // Restore scrolling
    };
}

// Close modal if the user clicks anywhere outside of the modal content area
window.onclick = (event) => {
    if (event.target == modal) {
        modal.style.display = "none";
        document.body.style.overflow = "auto";
    }
};

/**
 * 4. INITIALIZATION
 */
document.addEventListener("DOMContentLoaded", loadAllPathwayData);