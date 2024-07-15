//Contact form button animation

document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contact_section');

    contactForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        document.getElementById('nameInput').value = '';
        document.getElementById('emailInput').value = '';
        document.getElementById('subjectInput').value = '';
        document.getElementById('messageInput').value = '';
    });
});
