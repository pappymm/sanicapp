function showMessage() {
    alert("Hello! Thanks for visiting.");
}
document.querySelector("form").addEventListener("submit", async function(event) {

     alert("Thank you for reaching out! We will get back to you soon.");
    const formData = new FormData(event.target);

    const response = await fetch("/submit_form", {
        method: "POST",
        body: formData
    });

    const result = await response.json();
    if (result.status === "success") {
        // Replace form with a thank-you message
        document.querySelector("#contact").innerHTML = `
            <h2>Thank You!</h2>
            <p>We’ve received your message, and we’ll get back to you as soon as possible.</p>
            <a href="/">Return to Home</a>
        `;
    } else {
        alert("There was an error submitting the form. Please try again.");
    }

});
