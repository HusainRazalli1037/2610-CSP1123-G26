/**
 * myScript2.js
 * Manages caching scholarship data from the API and
 * handling the interactive UI modal windows cleanly.
 */

let scholarshipData = []; // Stores the array of scholarships from the API
let currentIndex = 0;

// Select DOM Elements
const modal = document.getElementById("scholarshipModal");
const closeBtn = document.querySelector(".close-btn");
const prevBtn = document.getElementById("prevScholarship");
const nextBtn = document.getElementById("nextScholarship");
const scrollArea = document.querySelector(".modal-scroll-area");

/**
 * 1. PRE-FETCH DATA FOR MODALS
 */
async function loadScholarshipDataSilently() {
  try {
    // Fetch data strictly to feed modal properties when buttons are clicked
    const response = await fetch("http://127.0.0.1:8000/api/scholarships/");
    if (!response.ok) throw new Error("Network response was not ok");
    scholarshipData = await response.json();
  } catch (error) {
    console.error("Error loading background modal data:", error);
  }
}

/**
 * UTILITY: Formats dates cleanly inside the popup window
 */
function formatDisplayDate(dateStr) {
  if (!dateStr) return "N/A";
  const cleanDate = dateStr.includes("T") ? dateStr.split("T")[0] : dateStr;
  const parts = cleanDate.split("-");
  if (parts.length !== 3) return cleanDate;

  const monthNames = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
  ];
  return `${monthNames[parseInt(parts[1], 10) - 1]} ${parseInt(parts[2], 10)}, ${parts[0]}`;
}

/**
 * 2. UPDATE MODAL CONTENT
 */
function updateModalContent(index) {
  const data = scholarshipData[index];
  if (!data) return;

  // Map API keys to the IDs safely
  const titleEl = document.getElementById("modalTitle");
  const deadlineEl = document.getElementById("modalDeadline");
  const locationEl = document.getElementById("modalLocation");
  const levelEl = document.getElementById("modalLevel");
  const amountEl = document.getElementById("modalAmount");
  const typeEl = document.getElementById("modalType");
  const contractEl = document.getElementById("modalContract");

  if (titleEl) titleEl.innerText = data.title || "N/A";
  if (deadlineEl) deadlineEl.innerText = formatDisplayDate(data.deadline);
  if (locationEl) locationEl.innerText = data.location || "N/A";
  if (levelEl) levelEl.innerText = data.level || "N/A";
  if (amountEl) amountEl.innerText = data.amount || "N/A";
  if (typeEl) typeEl.innerText = data.scholarship_type || "N/A";
  if (contractEl) contractEl.innerText = data.contract || "N/A";

  // Keep modal status uniform
  const modalStatus = document.getElementById("modalStatus");
  if (modalStatus) {
    modalStatus.innerText = "Accepting";
    modalStatus.className = "status-badge status-accepting large"; 
  }

  // Update Logo
  const modalLogo = document.getElementById("modalLogo");
  if (modalLogo) {
    modalLogo.src = data.logo || '/static/images/default-logo.jpeg';
  }

  // Update Application Button Link
  const linkElement = document.getElementById("modalLink");
  if (linkElement) {
    if (data.link) {
      linkElement.href = data.link;
      linkElement.style.pointerEvents = "auto";
      linkElement.style.opacity = "1";
      linkElement.innerText = "Apply Now";
      linkElement.style.display = "inline-block";
    } else {
      linkElement.style.display = "none";
    }
  }

  // Handle Courses
  const courseContainer = document.getElementById("modalCourses");
  if (courseContainer) {
    if (data.courses && Array.isArray(data.courses) && data.courses.length > 0) {
      courseContainer.innerHTML = data.courses.map((c) => `<div>• ${c.name}</div>`).join("");
    } else {
      courseContainer.innerHTML = "<div>Contact provider for details</div>";
    }
  }

  // Handle Criteria
  const criteriaContainer = document.getElementById("modalCriteria");
  if (criteriaContainer) {
    if (data.criteria && Array.isArray(data.criteria) && data.criteria.length > 0) {
      criteriaContainer.innerHTML = data.criteria.map((c) => `<li>${c.text || c}</li>`).join("");
    } else {
      criteriaContainer.innerHTML = "<li>Refer to official website for full criteria.</li>";
    }
  }

  // Update Pagination Button States
  if (prevBtn) prevBtn.disabled = index === 0;
  if (nextBtn) nextBtn.disabled = index === scholarshipData.length - 1;

  if (scrollArea) scrollArea.scrollTop = 0;
}

/**
 * 3. EVENT LISTENERS & NAVIGATION
 */
window.openModal = function (index) {
  currentIndex = index;
  // If the dataset fetched in the background isn't ready yet, fallback safe check
  if (scholarshipData.length === 0) {
    loadScholarshipDataSilently().then(() => updateModalContent(index));
  } else {
    updateModalContent(index);
  }
  if (modal) modal.style.display = "block";
};

// Pagination Controls
if (prevBtn) {
  prevBtn.addEventListener("click", () => {
    if (currentIndex > 0) {
      currentIndex--;
      updateModalContent(currentIndex);
    }
  });
}

if (nextBtn) {
  nextBtn.addEventListener("click", () => {
    if (currentIndex < scholarshipData.length - 1) {
      currentIndex++;
      updateModalContent(currentIndex);
    }
  });
}

if (closeBtn) {
  closeBtn.onclick = () => { if (modal) modal.style.display = "none"; };
}

window.onclick = (event) => {
  if (modal && event.target === modal) modal.style.display = "none";
};

// Fire silent background data load
document.addEventListener("DOMContentLoaded", loadScholarshipDataSilently);