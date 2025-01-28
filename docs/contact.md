---
title: Contact Me
description: Get in touch with Mo Maher
---

# Contact Me

I'm always interested in hearing from readers, potential collaborators, or anyone who wants to discuss technology and software development.

## Get in Touch

You can reach me through any of the following channels:

- 📧 Email: [mo.maher74@elshi5.com](mailto:mo.maher74@elshi5.com)
- 💼 LinkedIn: [Connect with me on LinkedIn](https://www.linkedin.com/in/momaher94/)
- 🐦 Twitter: [@mo_maher94](https://twitter.com/mo_maher94)
- 💻 GitHub: [slorksmo](https://github.com/slorksmo)

## Contact Form

<div class="contact-form">
    <form action="https://formspree.io/f/xanqopdk" method="POST">
        <div class="form-group">
            <label for="email">Your Email</label>
            <input type="email" id="email" name="email" placeholder="your.email@example.com" required>
        </div>
        
        <div class="form-group">
            <label for="message">Your Message</label>
            <textarea id="message" name="message" rows="5" placeholder="Type your message here..." required></textarea>
        </div>
        
        <button type="submit" class="submit-btn">
            <span class="material-icons">send</span>
            Send Message
        </button>
    </form>
</div>

<style>
.contact-form {
    max-width: 600px;
    margin: 2rem auto;
    padding: 2rem;
    background: var(--md-code-bg-color);
    border-radius: 1rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    color: var(--md-default-fg-color);
    font-weight: 500;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 0.5rem;
    background: var(--md-default-bg-color);
    color: var(--md-default-fg-color);
    font-size: 1rem;
    transition: all 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--md-primary-fg-color);
    box-shadow: 0 0 0 3px rgba(var(--md-primary-fg-color--rgb), 0.1);
}

.form-group input::placeholder,
.form-group textarea::placeholder {
    color: var(--md-default-fg-color--light);
    opacity: 0.7;
}

.submit-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.75rem 1.5rem;
    background: var(--md-primary-fg-color);
    color: var(--md-primary-bg-color);
    border: none;
    border-radius: 0.5rem;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    width: 100%;
}

.submit-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.submit-btn .material-icons {
    margin-right: 0.5rem;
    font-size: 1.2rem;
}

/* Dark mode adjustments */
[data-md-color-scheme="slate"] .contact-form {
    background: var(--md-code-bg-color);
}

[data-md-color-scheme="slate"] .form-group input,
[data-md-color-scheme="slate"] .form-group textarea {
    background: var(--md-default-bg-color);
    border-color: var(--md-default-fg-color--lightest);
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .contact-form {
        padding: 1.5rem;
        margin: 1rem;
    }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.contact-form form');
    
    form.addEventListener('submit', function(e) {
        const button = this.querySelector('button[type="submit"]');
        button.disabled = true;
        button.innerHTML = '<span class="material-icons">hourglass_empty</span> Sending...';
    });
});
</script>
