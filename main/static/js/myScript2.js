const scholarshipData = {
  "PNB Global Scholarship Award": {
    deadline: "8 April 2026",
    location: "Overseas (UK, US, Australia)",
    level: "Pre-University (A-Levels) & Undergraduate",
    amount: "Full (Tuition, living allowance, flight, and visa fees)",
    type: "Full Scholarship",
    contract: "5 to 6 years with PNB or its group of companies",
    courses: ["Econimics", "PPE", "Finance", "Data Science", "AI", "Technology", "Acturial Science", "Mathematics", "Statistics", "Science Related"],
    criteria: [
      "Malaysia Citizen",
      "Minimum 8(A+/A) in SPM",
      "Aged 25 years and below",
      "Active in sports and co-curicullar activities",],
    link: "scholarshippnb.pnb.com.my"
  },

  "Bank Negara Malaysia Kijang Pre-Univesity Scholarship": {
    deadline: "8 April 2026",
    location: "Overseas",
    level: "Pre-University (A-Level/IB) & Undergraduate",
    amount: "Full coverage (Premium allowance)",
    type: "Full Scholarship",
    contract: "Service bond with BNM based on the duration of study",
    courses: ["Economics", "Accounting and Finance", "Acturial Science", "Mathematics", "Data Science", "Computer Science", "Law"],
    criteria: ["Malaysia Citizen", "Straight 8(A+/A) and CEFR in SPM"],
    link: "bnm.gov.my/careers/scholarships"
  },

  "PETRONAS Education Sponsorship": {
    deadline: "10 April 2026",
    location: "Local (UTP) and Overseas (USA, UK, Australia, etc.)",
    level: "Foundation & Undergraduate",
    amount: "Full sponsorship",
    type: "Full Scholarship",
    contract: "Employment bond with PETRONAS/A",
    courses: ["Engineering", "Geoscience", "Computer Science", "Acturial Science", "Business", "Accounting"],
    criteria: ["Malaysia Citizen", "Minimum 8A and CEFR (B1) in SPM for local", "Minimum 4A+, 4A and CEFR (C1) in SPM for overseas"],
    link: "educationsponsorship.petronas.com.my"
  },

  "Yayasan UEM Undergraduate Global Scholarship": {
    deadline: "12 April 2026",
    location: "Local (KYUEM for A-Levels) & Overseas for Degree",
    level: "Pre-University & Undergraduate",
    amount: "Full Scholarship",
    type: "Full Scholarship",
    contract: "Bonded with UEM Group",
    courses: ["Business", "Engineering", "IT and Computer Related", "Environmental Studies"],
    criteria: ["Malaysia Citizen", "Minimum 7(A+/A) in SPM"],
    link: "yayasanuem.com.my"
  },

  "Yayasan Khazanah Scholarship Programme": {
    deadline: "13 April 2026",
    location: "Local (Watan) & Overseas (Global)",
    level: "Foundation, Undergraduate, Postgraduate",
    amount: "Full Scholarship",
    type: "Prestigious Excellence Scholarship",
    contract: "N/Service bond with Khazanah Nasional or partner companies",
    courses: ["Arts and Humanities", "Engineering and Technology", "Life Sciences", "Natural Sciences", "Social Sciences", "Management"],
    criteria: ["Malaysia Citizen", "Minimum 8(A+/A) in SPM", "Extremely high academic standards and proven leadership potential"],
    link: "apply.yayasankhazanah.com.my"
  },

  "Shell Malaysia Scholarship Programme": {
    deadline: "20 June 2026",
    location: "Local & Overseas",
    level: "Undergraduate",
    amount: "Full sponsorship",
    type: "Full sponsorship",
    contract: "Employment bond with Shell Malaysia",
    courses: ["Engineering", "Science Related", "Business Related"],
    criteria: ["Malaysia Citizen", "Minimum 8(A+/A) in SPM"],
    link: "shell.com.my/careers/students-and-graduates"
  },

  "The Star Education Fund Scholarship Awards": {
    deadline: "15 April 2026",
    location: "Local (Partner Private Universities)",
    level: "Foundation, Diploma, Degree",
    amount: "Full or Partial Tuition Fee waiver",
    type: "Full or Partial Tuition Fee waiver",
    contract: "Bond-free (No service contract)",
    courses: ["Medicine", "Engineering", "Law"],
    criteria: ["Malaysia Citizen", "Minimum 9A+ in SPM"],
    link: "thestar.com.my/edufund"
  },

  "Axiata Foundation All-Star Bestari Scholarship": {
    deadline: "10 May 2026",
    location: "Local (Public & Private Universities)",
    level: "Undergraduate",
    amount: "Full Scholarship",
    type: "Scholarship with a mandatory leadership development program",
    contract: "No employment bond",
    courses: ["Medicine", "Engineering", "Law"],
    criteria: ["Malaysia Citizen", "Minimum 6(A+/A/A-) in SPM"],
    link: "axiata-foundation.com"
  },

  "Hong Leong Foundation Merit Scholarship": {
    deadline: "30 May 2026",
    location: "Local",
    level: "Undergraduate / Diploma",
    amount: "Full Scholarship",
    type: "Grant/Scholarship",
    contract: "No bond",
    courses: ["Medicine", "Engineering", "Law"],
    criteria: ["Malaysia Citizen", "Minimum 9A+ in SPM", "priority for those from lower-income backgrounds (B40)"],
    link: "hongleongfoundation.com.my"
  },

  "JPA Scholarship": {
    deadline: "20 June 2026",
    location: "Local & Overseas (Japan, Korea, France, Germany)",
    level: "Pre-University & Degree",
    amount: "Tuition fee and allowance",
    type: "Convertible Loan (Pinjaman Boleh Ubah)",
    contract: "Loan is forgiven if you work for the government upon graduation",
    courses: ["Medicine", "Engineering", "Law"],
    criteria: ["Malaysia Citizen", "Minimum 9A+ (for global programs)", "9As (for specific country programs)"],
    link: "penajaan.jpa.gov.my"
  },

  "Yayasan Telekom Malaysia": {
    deadline: "April 2026",
    location: "Local (MMU) & Overseas",
    level: "Foundation & Undergraduate",
    amount: "Full sponsorship",
    type: "Full sponsorship",
    contract: "Bonded with TM Group",
    courses: ["IT", "Creative Multimedia", "Engineering", "Data Analytics", "Computer Science"],
    criteria: ["Malaysia Citizen", "Minimum 8(A+/A) in SPM"],
    link: "tm.com.my/yayasantm"
  },

  "Yayasan Tenaga Nasional": {
    deadline: "April 2026",
    location: "Local (UNITEN) & Overseas",
    level: "Foundation & Undergraduate",
    amount: "Full sponsorship",
    type: "Full sponsorship",
    contract: "Bonded with Tenaga Nasional Berhad (TNB)",
    courses: ["Electrical/Mechanical Engineering", "Computer Science", "Accounting"],
    criteria: ["Malaysia Citizen", "Minimum 8(A+/A) in SPM"],
    link: "ytn.tnb.com.my"
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