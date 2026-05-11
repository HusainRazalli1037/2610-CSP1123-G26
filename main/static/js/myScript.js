// 1. Setup the data
const subjectsByStream = {
  stem_a: ["Biology", "Physics", "Chemistry", "Additional Mathematics"],
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

// 2. Grab the elements
const streamSelector = document.getElementById("streamSelector");
// This grabs ALL 4 dropdowns because they all share this class
const allSubjectSelects = document.querySelectorAll(".package-subject-select");

// 3. FUNCTION: Populate dropdowns when Stream changes
streamSelector.addEventListener("change", function () {
  const selectedStream = this.value;
  const availableSubjects = subjectsByStream[selectedStream] || [];

  allSubjectSelects.forEach((select) => {
    select.innerHTML = '<option value="">CHOOSE SUBJECT</option>';
    availableSubjects.forEach((subject) => {
      const option = document.createElement("option");
      option.value = subject;
      option.textContent = subject;
      select.appendChild(option);
    });
  });
});

// 4. FUNCTION: The "Master Filter" for duplicates
allSubjectSelects.forEach((currentSelect) => {
  currentSelect.addEventListener("change", function () {
    // Step A: Create a list of all currently selected values across all 4 boxes
    const selectedValues = Array.from(allSubjectSelects)
      .map((s) => s.value)
      .filter((val) => val !== ""); // Ignore empty/default choices

    // Step B: Update every dropdown to disable what others have picked
    allSubjectSelects.forEach((dropdown) => {
      const currentChoice = dropdown.value; // What this specific box has picked

      Array.from(dropdown.options).forEach((option) => {
        if (option.value === "") return; // Skip the "CHOOSE SUBJECT" option

        // If this option is picked in ANOTHER box, disable it
        // BUT, don't disable it if it's the one THIS box currently has selected
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