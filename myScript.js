// 1. Setup the data
const subjectsByStream = {
  stem_a: ["Biology", "Physic", "Chemistry", "Additional Mathematics"],
  stem_b: [
    "Asas Kelestarian",
    "Biology",
    "Physic",
    "Grafik Komunikasi Teknikal",
    "Chemistry",
    "Lukisan Kejuruteraan",
    "Additional Mathematics",
    "Pengajian Kejuruteraan Awam",
    "Pengajian Kejuruteraan Elektrik & Elektronik",
    "Pengajian Kejuruteraan Mekanikal",
    "Pertanian",
    "Reka Cipta",
    "Science Computer",
    "Sains Rumah Tangga",
    "Sains Sukan",
    "Sains Tambahan",
  ],
  stem_c: [
    "Akuakultur & Haiwan Rekreasi",
    "Asas Kelestarian",
    "Asuhan & Pendidikan Awal Kanak-Kanak",
    "Gerontologi Asas Dan Geriatrik",
    "Grafik Komunikasi Teknikal",
    "Hiasan Dalaman",
    "Katering Dan Penyajian",
    "Kerja Paip Domestik",
    "Kimpalan Arka dan Gas",
    "Landskap dan Nurseri",
    "Lukisan Kejuruteraan",
    "Menservis Automobil",
    "Menservis Motosikal",
    "Menservis Peralatan Penyejukan & Penyamanan Udara",
    "Pembinaan Perabot",
    "Pemprosesan Makanan",
    "Pendawaian Makanan",
    "Pendawaian Domestik",
    "Pengajian Kejuruteraan Awam",
    "Pengajian Kejuruteraan Elektrik & Elektronik",
    "Pengajian Kejuruteraan Mekanikal",
    "Penjagaan Muka & Penggayaan Rambut",
    "Pertanian",
    "Produksi Multimedia",
    "Produksi Reka Tanda",
    "Reka Bentuk Grafik Digital",
    "Reka Cipta",
    "Rekaan dan Jahitan Pakaian",
    "Science Computer",
    "Sains Rumah Tangga",
    "Sains Sukan",
    "Sains Tambahan",
    "Tanaman Makanan",
  ],
  ksi: [
    "AL-ADAB WA AL-BALAGHAH",
    "AL-LUGHAH AL-ARABIAH AL-MU'ASIRAH",
    "AL-SYARIAH",
    "ALAT MUZIK UTAMA",
    "APRESIASI TARI",
    "AURAL DAN TEORI MUZIK",
    "BAHASA ARAB / BAHASA ARAB TINGGI",
    "BAHASA CINA",
    "BAHASA IBAN",
    "BAHASA KADAZANDUSUN",
    "BAHASA PUNJABI",
    "BAHASA SEMAI",
    "BAHASA TAMIL",
    "BIBLE KNOWLEDGE",
    "EKONOMI",
    "GEOGRAFI",
    "HIFZ AL QURAN",
    "KESUSASTERAAN CINA",
    "KESUSASTERAAN INGGERIS",
    "KESUSASTERAAN MELAYU KOMUNIKATIF",
    "KESUSASTERAAN TAMIL",
    "KOREOGRAFI TARI",
    "LAKONAN",
    "LUKISAN",
    "MAHARAT AL QURAN",
    "MANAHIJ AL-'ULUM AL-ISLAMIAH",
    "MULTIMEDIA KREATIF",
    "MUZIK KOMPUTER",
    "PENDIDIKAN AL-QURAN DAN AL-SUNNAH",
    "PENDIDIKAN MUZIK",
    "PENDIDIKAN SENI VISUAL",
    "PENDIDIKAN SYARI'AH ISLAMIAH",
    "PENGAJIAN KEUSAHAWANAN",
    "PENULISAN SKRIP",
    "PERNIAGAAN",
    "PRINSIP PERAKAUNAN",
    "PRODUKSI SENI PERSEMBAHAN",
    "REKA BENTUK GRAFIK",
    "REKA BENTUK INDUSTRI",
    "REKA BENTUK KRAF",
    "SEJARAH DAN PENGURUSAN SENI",
    "SENI HALUS 2D",
    "SENI HALUS 3D",
    "SINOGRAFI",
    "TARIAN",
    "TASAWWUR ISLAM",
    "TURATH AL-QURAN DAN AL-SUNNAH",
    "Turath Bahasa Arab",
    "Turath Dirasat Islamiah",
    "Usul Al-Din",
  ],
};

// NEW: Create a master list of ALL subjects from ALL streams for the "Best Subject" category
const allAvailableSubjects = [
  ...new Set(Object.values(subjectsByStream).flat()),
].sort();

// 2. Grab the elements
const streamSelector = document.getElementById("streamSelector");
const allSubjectSelects = document.querySelectorAll(".package-subject-select");
// Target the rows in "Best Subject Package" to hide the second one for STEM C
const packageRows = document.querySelectorAll(
  ".right-column .subject-card:first-child .input-group-row",
);

// 3. FUNCTION: Populate dropdowns when Stream changes
streamSelector.addEventListener("change", function () {
  const selectedStream = this.value;
  const streamSpecificSubjects = subjectsByStream[selectedStream] || [];

  // Logic for STEM C: Hide the second row in the package card
  if (selectedStream === "stem_c") {
    packageRows[1].style.display = "none";
    allSubjectSelects[1].value = ""; // Reset the hidden dropdown
  } else {
    packageRows[1].style.display = "flex";
  }

  allSubjectSelects.forEach((select, index) => {
    // Determine which list to use:
    // Index 0 and 1 are "Best Subject Package" (Stream Specific)
    // Index 2 and 3 are "Best Subject" (All Subjects)
    const listToUse = index < 2 ? streamSpecificSubjects : allAvailableSubjects;

    select.innerHTML = '<option value="">CHOOSE SUBJECT</option>';
    listToUse.forEach((subject) => {
      const option = document.createElement("option");
      option.value = subject;
      option.textContent = subject;
      select.appendChild(option);
    });
  });
});

// 4. FUNCTION: The "Master Filter" for duplicates (remains the same)
allSubjectSelects.forEach((currentSelect) => {
  currentSelect.addEventListener("change", function () {
    const selectedValues = Array.from(allSubjectSelects)
      .map((s) => s.value)
      .filter((val) => val !== "");

    allSubjectSelects.forEach((dropdown) => {
      const currentChoice = dropdown.value;
      Array.from(dropdown.options).forEach((option) => {
        if (option.value === "") return;
        if (
          selectedValues.includes(option.value) &&
          option.value !== currentChoice
        ) {
          option.disabled = true;
          option.style.color = "#ccc";
        } else {
          option.disabled = false;
          option.style.color = "";
        }
      });
    });
  });
});
