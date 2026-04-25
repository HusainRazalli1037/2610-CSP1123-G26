const scholarshipData = {
  "Yayasan Axiata": {
    deadline: "1 May 2030",
    location: "Local",
    level: "Post-SPM",
    amount: "Full Scholarship",
    type: "Need Based",
    contract: "N/A",
    courses: ["Arts", "Business", "Engineering", "IT"],
    criteria: [
      "Malaysia Citizen",
      "Minimum 7A in SPM",
      "Aged 25 years and below",
      "Active in sports and co-curicullar activities",
    ],
  },
  "Kijang Scholarship": {
    deadline: "15 May 2030",
    location: "Local/Overseas",
    level: "Post-SPM",
    amount: "Full Scholarship",
    type: "Need Based",
    contract: "N/A",
    courses: ["Economics", "Accounting", "Finance"],
    criteria: ["Malaysia Citizen", "Straight A+ in SPM"],
  },
  "JPA Scholarship": {
    deadline: "20 June 2026",
    location: "Local/Overseas",
    level: "Degree",
    amount: "Lump Sum / Variable",
    type: "Need Based",
    contract: "N/A",
    courses: ["Medicine", "Engineering", "Law"],
    criteria: ["Malaysia Citizen", "Minimum 9A+ in SPM"],
  },
};

const scholarshipKeys = Object.keys(scholarshipData);
let currentIndex = 0;

const modal = document.getElementById("scholarshipModal");
const closeBtn = document.querySelector(".close-btn");
const prevBtn = document.getElementById("prevScholarship");
const nextBtn = document.getElementById("nextScholarship");
const scrollArea = document.querySelector(".modal-scroll-area");

// SINGLE function to handle all updates
function updateModalContent(index) {
  const title = scholarshipKeys[index];
  const data = scholarshipData[title];

  if (data) {
    document.getElementById("modalTitle").innerText = title;
    document.getElementById("modalDeadline").innerText = data.deadline;
    document.getElementById("modalLocation").innerText = data.location;
    document.getElementById("modalLevel").innerText = data.level;
    document.getElementById("modalAmount").innerText = data.amount;
    document.getElementById("modalType").innerText = data.type;
    document.getElementById("modalContract").innerText = data.contract;

    // Fill Courses
    const courseContainer = document.getElementById("modalCourses");
    courseContainer.innerHTML = data.courses
      .map((c) => `<div>• ${c}</div>`)
      .join("");

    // Fill Criteria
    const criteriaContainer = document.getElementById("modalCriteria");
    criteriaContainer.innerHTML = data.criteria
      .map((c) => `<li>${c}</li>`)
      .join("");

    // Update Button States
    prevBtn.disabled = index === 0;
    nextBtn.disabled = index === scholarshipKeys.length - 1;

    // Reset Scroll Position
    scrollArea.scrollTop = 0;
  }
}

// Event Listeners for Grid Buttons
document.querySelectorAll(".btn2").forEach((button) => {
  button.addEventListener("click", () => {
    const title = button.querySelector("h3").innerText;
    currentIndex = scholarshipKeys.indexOf(title);

    if (currentIndex !== -1) {
      updateModalContent(currentIndex);
      modal.style.display = "block";
    }
  });
});

// Pagination Listeners
prevBtn.addEventListener("click", () => {
  if (currentIndex > 0) {
    currentIndex--;
    updateModalContent(currentIndex);
  }
});

nextBtn.addEventListener("click", () => {
  if (currentIndex < scholarshipKeys.length - 1) {
    currentIndex++;
    updateModalContent(currentIndex);
  }
});

// Close Logic
closeBtn.onclick = () => (modal.style.display = "none");
window.onclick = (event) => {
  if (event.target == modal) modal.style.display = "none";
};
