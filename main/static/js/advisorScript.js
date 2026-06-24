/**
 * advisorScript.js
 * Fetches advisor data from Django API and filters based on user input.
 */

// 1. Select Elements by ID
const fieldSelect = document.getElementById("fieldSelector");
const locationSelect = document.getElementById("locationSelector");
const btnGenerate = document.querySelector(".btn-generate");
const btnReset = document.querySelector(".btn-reset");
const modal = document.getElementById("pathwayModal");
const container = document.getElementById("modalPathways");
const dynamicTitle = document.getElementById("dynamicTitle");
const closeBtn = document.querySelector(".close-btn");

// Global variable to store database records
let advisorData = [];

/**
 * 2. FETCH DATA FROM DATABASE
 */
async function loadAdvisorData() {
    try {
        const response = await fetch("/api/pathway-advisor/");
        if (!response.ok) throw new Error("Network response was not ok");
        
        advisorData = await response.json();
        console.log("Database successfully synced:", advisorData);
    } catch (error) {
        console.error("Error loading advisor data:", error);
    }
}

/**
 * 3. MAIN GENERATE LOGIC
 */
btnGenerate.addEventListener("click", () => {
    if (!fieldSelect || !locationSelect) return;

    // Get display text for the title
    const selectedFieldText = fieldSelect.options[fieldSelect.selectedIndex].text;
    const selectedLocationText = locationSelect.options[locationSelect.selectedIndex].text;

    // Get values for filtering
    const fieldValue = fieldSelect.value;
    const locationValue = locationSelect.value;

    if (!fieldValue || !locationValue) {
        alert("Please select both a Field and a Location!");
        return;
    }

    /**
     * FILTER LOGIC (Improved)
     * .toLowerCase() and .trim() prevent mismatches between Admin input and HTML values.
     */
    const results = advisorData.filter((item) => {
        const dbField = String(item.field).toLowerCase().trim();
        const dbLocation = String(item.location).toLowerCase().trim();
        const uiField = String(fieldValue).toLowerCase().trim();
        const uiLocation = String(locationValue).toLowerCase().trim();

        return dbField === uiField && dbLocation === uiLocation;
    });

    // Update Modal Title
    if (dynamicTitle) {
        dynamicTitle.innerText = `${selectedFieldText} in ${selectedLocationText}`;
    }

    // Render Results
    if (results.length === 0) {
        container.innerHTML = `
            <div style="text-align:center; padding: 40px; color: white; width: 100%;">
                <p>No courses found for this selection yet.</p>
                <small>There is no data available for field "${fieldValue}" in "${locationValue}"</small>
            </div>`;
    } else {
        container.innerHTML = results.map(course => `
            <div class="course-box">
                <div class="course-main-info">
                    <div class="course-code">${course.code}</div>
                    <div class="course-name">${course.name}</div>
                    <div class="course-uni">${course.university || "Multiple Institutions"}</div>
                </div>
                <div class="course-details-grid">
                    <div class="detail-tag">${course.level}</div>
                    <div class="detail-tag">Merit: ${course.merit}%</div>
                    <div class="detail-tag">${course.duration}</div>
                    <div class="detail-tag">${course.course_type}</div>
                </div>
            </div>
        `).join("");
    }

    // Open Modal
    if (modal) {
        modal.style.display = "block";
        container.scrollTop = 0;
    }
});

/**
 * 4. RESET & CLOSE LOGIC
 */
btnReset.addEventListener("click", () => {
    if (fieldSelect) fieldSelect.selectedIndex = 0;
    if (locationSelect) locationSelect.selectedIndex = 0;
});

if (closeBtn) {
    closeBtn.onclick = () => { modal.style.display = "none"; };
}

window.onclick = (event) => {
    if (event.target == modal) { modal.style.display = "none"; }
};

document.addEventListener("DOMContentLoaded", loadAdvisorData);