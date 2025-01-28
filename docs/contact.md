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
    <form action="https://formspree.io/f/xanqopdk" method="POST" enctype="multipart/form-data">
        <div class="form-group">
            <label for="name">Name</label>
            <input type="text" id="name" name="name" placeholder="Your name" required>
        </div>
        
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" placeholder="your.email@example.com" required>
        </div>
        
        <div class="form-group">
            <label for="subject">Subject</label>
            <input type="text" id="subject" name="subject" placeholder="Message subject" required>
        </div>
        
        <div class="form-group">
            <label for="message">Message</label>
            <textarea id="message" name="message" rows="5" placeholder="Your message here..." required></textarea>
        </div>

        <div class="form-group file-upload">
            <label for="upload">
                <span class="material-icons">attach_file</span>
                Attachment
            </label>
            <input type="file" id="upload" name="upload" class="file-input">
            <div class="file-name">No file chosen</div>
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

/* File Upload Styling */
.file-upload {
    position: relative;
}

.file-upload label {
    display: inline-flex;
    align-items: center;
    padding: 0.75rem 1.5rem;
    background: var(--md-code-bg-color);
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 0.5rem;
    cursor: pointer;
    transition: all 0.3s ease;
}

.file-upload label:hover {
    border-color: var(--md-primary-fg-color);
}

.file-upload .material-icons {
    margin-right: 0.5rem;
}

.file-upload .file-input {
    position: absolute;
    width: 0.1px;
    height: 0.1px;
    opacity: 0;
    overflow: hidden;
    z-index: -1;
}

.file-upload .file-name {
    margin-top: 0.5rem;
    font-size: 0.9rem;
    color: var(--md-default-fg-color--light);
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
    
    .submit-btn {
        width: 100%;
    }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.contact-form form');
    const fileInput = document.querySelector('.file-input');
    const fileName = document.querySelector('.file-name');

    // Update file name when file is selected
    fileInput.addEventListener('change', function() {
        if (this.files.length > 0) {
            fileName.textContent = this.files[0].name;
        } else {
            fileName.textContent = 'No file chosen';
        }
    });

    // Form submission handling
    form.addEventListener('submit', function(e) {
        const button = this.querySelector('button[type="submit"]');
        button.disabled = true;
        button.innerHTML = '<span class="material-icons">hourglass_empty</span> Sending...';
    });
});
</script>
