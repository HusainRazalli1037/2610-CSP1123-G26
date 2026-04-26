// 1. Data Object (Expand this with more courses)
const advisorData = [
  {
    field: "engineering",
    location: "Selangor",
    uni: "UiTM Shah Alam",
    logo: "uitm_logo.png",
    code: "EE111",
    name: "DIPLOMA KEJURUTERAAN ELEKTRIK",
    level: "Diploma",
    merit: "75.40%",
    duration: "06 Semester",
    type: "Bukan TVET",
  },
  {
    field: "engineering",
    location: "Selangor",
    uni: "UiTM Shah Alam",
    logo: "uitm_logo.png",
    code: "EE111",
    name: "DIPLOMA KEJURUTERAAN MEKANIKAL",
    level: "Diploma",
    merit: "75.40%",
    duration: "06 Semester",
    type: "Bukan TVET",
  },
  {
    field: "it",
    location: "Selangor",
    uni: "UiTM Puncak Perdana",
    logo: "uitm_logo.png",
    code: "CS110",
    name: "DIPLOMA SAINS KOMPUTER",
    level: "Diploma",
    merit: "82.10%",
    duration: "05 Semester",
    type: "Bukan TVET",
  },
  {
    field: "it",
    location: "Johor",
    uni: "UiTM Segamat",
    logo: "uitm_logo.png",
    code: "CS110",
    name: "DIPLOMA SAINS KOMPUTER",
    level: "Diploma",
    merit: "78.50%",
    duration: "05 Semester",
    type: "Bukan TVET",
  },
];

// 2. Select Elements
const fieldSelect = document.querySelectorAll("select")[0];
const locationSelect = document.querySelectorAll("select")[1];
const btnGenerate = document.querySelector(".btn-generate");
const btnReset = document.querySelector(".btn-reset");
const modal = document.getElementById("pathwayModal");
const container = document.getElementById("modalPathways");
const dynamicTitle = document.getElementById("dynamicTitle");
const closeBtn = document.querySelector(".close-btn");

// 3. Main Generate Logic
btnGenerate.addEventListener("click", () => {
  // Get text for the heading
  const selectedFieldText = fieldSelect.options[fieldSelect.selectedIndex].text;
  const selectedLocationText =
    locationSelect.options[locationSelect.selectedIndex].text;

  // Get raw values for filtering the data
  const fieldValue = fieldSelect.value;
  const locationValue = locationSelect.value;

  // Validation: Ensure user picked something
  if (!fieldValue || !locationValue) {
    alert("Please select both a Field and a Location!");
    return;
  }

  // Update the Title at the top of the popup
  if (dynamicTitle) {
    dynamicTitle.innerText = `${selectedFieldText} in ${selectedLocationText}`;
  }

  // Filter Data
  const results = advisorData.filter(
    (item) => item.field === fieldValue && item.location === locationValue,
  );

  // Clear existing content and inject new results
  if (results.length === 0) {
    container.innerHTML = `<p style="text-align:center; padding: 40px; color: #666; width: 100%;">No courses found for this selection yet.</p>`;
  } else {
    container.innerHTML = results
      .map(
        (course) => `
      <div class="course-box">
        <div>
          <div class="course-code">${course.code}</div>
          <div class="course-name">${course.name}</div>
          <div class="course-uni">${course.uni}</div>
        </div>
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
  }

  // Show the modal and reset its scroll position to the top
  modal.style.display = "block";
  container.scrollTop = 0;
});

// 4. Reset Logic
btnReset.addEventListener("click", () => {
  fieldSelect.selectedIndex = 0;
  locationSelect.selectedIndex = 0;
});

// 5. Modal Close Logic
closeBtn.onclick = () => {
  modal.style.display = "none";
};

// Close when clicking outside the modal box
window.onclick = (event) => {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
