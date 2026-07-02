/**
 * pathwayScript.js
 * Manages background data operations and interactive popup modals for the Pathway Hub.
 */

const modal = document.getElementById("pathwayModal");
const closeBtn = document.querySelector(".close-btn");
const container = document.getElementById("modalPathways");
const modalLogo = document.getElementById("modalLogo");
const modalUniTitle = document.getElementById("modalUniTitle");

// Holds the global array from the database for model tracking indexing
let allPathwayData = [];

/**
 * 1. PRE-FETCH API DATA FOR MODALS SILENTLY
 */
async function loadAllPathwayData() {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/pathway-hub/"); 
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        
        // Save database payload globally ordered to match backend index keys
        allPathwayData = await response.json();
    } catch (error) {
        console.error("Error loading pathway background data:", error);
    }
}

/**
 * 2. OPEN MODAL BY SELECTED INDEX
 * Triggers directly from the HTML click layer safely.
 */
function openPathwayModal(uniName) {
    if (!uniName) return;

    // Update Modal Header layout targets
    if (modalUniTitle) modalUniTitle.innerText = uniName;

    // Filter your entire API dataset array for matches matching this university name
    const associatedCourses = allPathwayData.filter(course => 
        course.university && course.university.toLowerCase().trim() === uniName.toLowerCase().trim()
    );

    if (modalLogo && associatedCourses.length > 0) {
        modalLogo.src = associatedCourses[0].logo || "/static/images/default_uni.png";
    }

    // Map and inject ALL courses into the scroll area container simultaneously
    if (container) {
        container.innerHTML = associatedCourses.map(course => `
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

    if (modal) {
        modal.style.display = "block";
        document.body.style.overflow = "hidden";
    }
}
window.openPathwayModal = openPathwayModal;

/**
 * 3. CONTROL EVENT LISTENERS
 */
if (closeBtn) {
    closeBtn.onclick = () => {
        if (modal) modal.style.display = "none";
        document.body.style.overflow = "auto";
    };
}

window.onclick = (event) => {
    if (event.target == modal) {
        modal.style.display = "none";
        document.body.style.overflow = "auto";
    }
};

// Fire background tracking sequence 
document.addEventListener("DOMContentLoaded", loadAllPathwayData);