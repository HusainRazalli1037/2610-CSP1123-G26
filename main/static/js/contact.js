document
  .getElementById("contact-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Change button text to show it's sending
    const btn = document.querySelector(".btn-send");
    btn.innerHTML = "SENDING...";
    btn.disabled = true;

    const serviceID = "default_service";
    const templateID = "template_3nzqgxs"; // From EmailJS dashboard

    emailjs.sendForm(serviceID, templateID, this).then(
      () => {
        btn.innerHTML = "SEND MESSAGE";
        btn.disabled = false;
        alert("Message Sent Successfully!");
        document.getElementById("contact-form").reset(); // Clear form
      },
      (err) => {
        btn.innerHTML = "SEND MESSAGE";
        btn.disabled = false;
        alert("Failed to send message. Error: " + JSON.stringify(err));
      },
    );
  });