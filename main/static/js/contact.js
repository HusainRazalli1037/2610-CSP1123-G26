document.getElementById("contact-form").addEventListener("submit", async function (event) {
    event.preventDefault();

    const btn = document.querySelector(".btn-send");
    const originalText = "SEND MESSAGE";
    
    btn.innerHTML = "SENDING...";
    btn.disabled = true;

    // Prepare data from the form
    const formData = new FormData(this);
    
    // This object MUST match your Django Model fields
    const dataForDb = {
        name: formData.get("from_name"),  // Matches name="from_name" in HTML
        email: formData.get("user_email"), // Matches name="user_email" in HTML
        subject: formData.get("subject"),
        message: formData.get("message")
    };

    try {
        // --- 1. SAVE TO DATABASE ---
        // We use a separate try/catch so if the DB fails, the email still tries to send
        try {
            await fetch("/save-inquiry/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": formData.get("csrfmiddlewaretoken")
                },
                body: JSON.stringify(dataForDb),
            });
        } catch (dbErr) {
            console.error("Database save failed:", dbErr);
        }

        // --- 2. SEND EMAIL VIA EMAILJS ---
        // Double check these IDs in your EmailJS Dashboard!
        const serviceID = "default_service";
        const templateID = "template_3nzqgxs";

        await emailjs.sendForm(serviceID, templateID, this);

        alert("Message Sent Successfully!");
        this.reset(); 

    } catch (err) {
        console.error("EmailJS Error:", err);
        alert("Failed to send email. Please check your internet connection or EmailJS settings.");
    } finally {
        // --- 3. THE RESET (Crucial) ---
        // This ensures the button is NEVER stuck on "SENDING..."
        btn.innerHTML = originalText;
        btn.disabled = false;
    }
});