// id kene sama mcm dekat alt html baru tak error

const pathwayData = {
  UiTM: {
    logo: "uitm_logo.png",
    courses: [
      {
        code: "UB4545001",
        name: "DIPLOMA PENDIDIKAN AWAL KANAK-KANAK",
        level: "Diploma",
        merit: "66.56%",
        duration: "05 Semester",
        type: "Bukan TVET",
      },
      {
        code: "UB4545001",
        name: "DIPLOMA PENDIDIKAN ISLAM",
        level: "Diploma",
        merit: "89.09%",
        duration: "05 Semester",
        type: "Bukan TVET",
      },
      {
        code: "UB4545002",
        name: "DIPLOMA TEATER",
        level: "Diploma",
        merit: "66.56%",
        duration: "05 Semester",
        type: "Bukan TVET",
      },
    ],
  },
  UPSI: {
    logo: "upsi_logo.png",
    courses: [
      {
        code: "UP123",
        name: "DIPLOMA PENDIDIKAN",
        level: "Diploma",
        merit: "70.00%",
        duration: "06 Semester",
        type: "Bukan TVET",
      },
    ],
  },
  // Add UniZA, UTeM, etc. here
};

const modal = document.getElementById("pathwayModal");
const closeBtn = document.querySelector(".close-btn");

function openPathwayModal(uniName) {
  const data = pathwayData[uniName];

  // If data doesn't exist for a clicked uni, alert the user so you know it's working
  if (!data) {
    console.error("No data found for: " + uniName);
    return;
  }

  document.getElementById("modalLogo").src = data.logo;
  const container = document.getElementById("modalPathways");

  container.innerHTML = data.courses
    .map(
      (course) => `
    <div class="course-box">
      <div class="course-code">${course.code}</div>
      <div class="course-name">${course.name}</div>
      <div class="course-uni">${uniName}</div>
      <div class="course-details-grid">
        <div class="detail-tag">${course.level}</div>
        <div class="detail-tag">Merit: ${course.merit}</div>
        <div class="detail-tag">${course.duration}</div>
        <div class="detail-tag">${course.type}</div>
      </div>
    </div>
  `,
    )
    .join("");

  modal.style.display = "block";
}

document.querySelectorAll(".uni-card").forEach((card) => {
  card.addEventListener("click", () => {
    const uniName = card.querySelector("img").alt;
    openPathwayModal(uniName);
  });
});

// Use the variable closeBtn you already defined
if (closeBtn) {
  closeBtn.onclick = () => (modal.style.display = "none");
}

window.onclick = (event) => {
  if (event.target == modal) modal.style.display = "none";
};
