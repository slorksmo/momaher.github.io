---
title: Mo Maher - Software Engineer & Tech Enthusiast
description: Personal website and blog of Mo Maher
---

# Welcome to My Personal Blog

<div class="hero">
    <div class="hero-content">
        <div class="profile-container">
            <div class="profile-image-wrapper">
                <img src="assets/images/profile.jpg" alt="Mo Maher" class="profile-image">
            </div>
            <h1 class="name">Mo Maher</h1>
            <p class="subtitle">Software Engineer & Tech Enthusiast</p>
        </div>
        <div class="social-links">
            <a href="https://github.com/slorksmo" class="social-link github" target="_blank" rel="noopener" aria-label="GitHub Profile">
                <span class="material-icons">code</span>
                <span class="label">GitHub</span>
            </a>
            <a href="https://linkedin.com/in/momaher94" class="social-link linkedin" target="_blank" rel="noopener" aria-label="LinkedIn Profile">
                <span class="material-icons">integration_instructions</span>
                <span class="label">LinkedIn</span>
            </a>
            <a href="https://twitter.com/mo_maher94" class="social-link twitter" target="_blank" rel="noopener" aria-label="Twitter Profile">
                <span class="material-icons">cloud</span>
                <span class="label">Twitter</span>
            </a>
        </div>
    </div>
</div>

<style>
.hero {
    text-align: center;
    padding: 4rem 0;
    background: linear-gradient(135deg, var(--md-primary-fg-color--light) 0%, var(--md-primary-fg-color) 100%);
    color: var(--md-primary-bg-color);
    border-radius: 1rem;
    margin: 2rem 0;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.hero-content {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 1rem;
}

.profile-container {
    margin-bottom: 2rem;
}

.profile-image-wrapper {
    position: relative;
    width: 200px;
    height: 200px;
    margin: 0 auto 1.5rem;
    border-radius: 50%;
    padding: 0.5rem;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    transition: transform 0.3s ease;
}

.profile-image-wrapper:hover {
    transform: scale(1.05);
}

.profile-image {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid var(--md-primary-bg-color);
    transition: transform 0.3s ease;
}

.name {
    font-size: 2.5rem;
    margin: 1rem 0 0.5rem;
    font-weight: 700;
    letter-spacing: -0.5px;
}

.subtitle {
    font-size: 1.2rem;
    color: var(--md-primary-bg-color);
    opacity: 0.9;
    margin-bottom: 2rem;
}

.social-links {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
}

.social-link {
    display: flex;
    align-items: center;
    padding: 0.75rem 1.25rem;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 2rem;
    color: var(--md-primary-bg-color);
    text-decoration: none;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
}

.social-link:hover {
    background: var(--md-primary-bg-color);
    color: var(--md-primary-fg-color);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.social-link .material-icons {
    font-size: 1.5rem;
    margin-right: 0.75rem;
}

.social-link .label {
    font-size: 1rem;
    font-weight: 500;
}

/* Social link specific colors on hover */
.social-link.github:hover {
    background: #24292e;
    color: #fff;
}

.social-link.linkedin:hover {
    background: #0077b5;
    color: #fff;
}

.social-link.twitter:hover {
    background: #1da1f2;
    color: #fff;
}

@media (max-width: 768px) {
    .hero {
        padding: 3rem 0;
        margin: 1rem 0;
    }

    .name {
        font-size: 2rem;
    }

    .subtitle {
        font-size: 1.1rem;
    }

    .social-links {
        flex-direction: column;
        align-items: stretch;
        gap: 0.75rem;
    }

    .social-link {
        justify-content: center;
    }
}

/* Dark mode adjustments */
[data-md-color-scheme="slate"] .hero {
    background: linear-gradient(135deg, var(--md-primary-fg-color--dark) 0%, var(--md-primary-fg-color) 100%);
}

[data-md-color-scheme="slate"] .social-link {
    background: rgba(0, 0, 0, 0.2);
}

[data-md-color-scheme="slate"] .profile-image-wrapper {
    background: rgba(0, 0, 0, 0.2);
}
</style>

## Featured Articles

<div class="featured-section">
    <div class="grid cards" markdown>
        <div class="card">
            <span class="material-icons card-icon">article</span>
            [__Building Scalable Systems__](blog/posts/building-scalable-systems.md)
            ---
            Learn about best practices and patterns for building scalable software systems.
            
            <span class="material-icons card-arrow">arrow_forward</span>
        </div>

        <div class="card">
            <span class="material-icons card-icon">memory</span>
            [__Cloud Native Applications__](blog/posts/cloud-native-apps.md)
            ---
            Explore modern cloud-native application development principles.
            
            <span class="material-icons card-arrow">arrow_forward</span>
        </div>
    </div>
</div>

## Latest Projects

<div class="featured-section">
    <div class="grid cards" markdown>
        <div class="card">
            <span class="material-icons card-icon">code</span>
            [__Project 1__](portfolio/project1.md)
            ---
            Description of your first featured project.
            
            <span class="material-icons card-arrow">arrow_forward</span>
        </div>

        <div class="card">
            <span class="material-icons card-icon">storage</span>
            [__Project 2__](portfolio/project2.md)
            ---
            Description of your second featured project.
            
            <span class="material-icons card-arrow">arrow_forward</span>
        </div>
    </div>
</div>

## Technical Skills

<div class="skills-section">
    <div class="skill-category">
        <h3>Programming Languages</h3>
        <div class="skills-grid">
            <a href="#" class="skill">
                <span class="material-icons">code</span>
                Python
            </a>
            <a href="#" class="skill">
                <span class="material-icons">javascript</span>
                JavaScript
            </a>
            <a href="#" class="skill">
                <span class="material-icons">coffee</span>
                Java
            </a>
        </div>
    </div>

    <div class="skill-category">
        <h3>Technologies & Tools</h3>
        <div class="skills-grid">
            <a href="#" class="skill">
                <span class="material-icons">integration_instructions</span>
                Docker
            </a>
            <a href="#" class="skill">
                <span class="material-icons">cloud</span>
                AWS
            </a>
            <a href="#" class="skill">
                <span class="material-icons">merge</span>
                Git
            </a>
        </div>
    </div>
</div>

## Get in Touch

<div class="contact-section">
    <a href="contact.md">
        <span class="material-icons contact-icon">mail</span>
        Feel free to contact me for collaborations or questions!
    </a>
</div>

<style>
/* Add Material Icons Font */
@import url('https://fonts.googleapis.com/icon?family=Material+Icons');

/* Featured Sections Styling */
.featured-section {
    margin: 2rem 0;
}

.grid.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 1.5rem 0;
}

.card {
    position: relative;
    padding: 1.5rem;
    background: var(--md-code-bg-color);
    border-radius: 0.8rem;
    transition: all 0.3s ease;
    border: 1px solid var(--md-default-fg-color--lightest);
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    border-color: var(--md-primary-fg-color);
}

.card-icon {
    font-size: 2.5rem;
    color: var(--md-primary-fg-color);
    margin-bottom: 1rem;
    display: block;
}

.card h2 {
    margin: 1rem 0;
    color: var(--md-default-fg-color);
}

.card p {
    color: var(--md-default-fg-color--light);
}

.card-arrow {
    position: absolute;
    bottom: 1rem;
    right: 1rem;
    color: var(--md-primary-fg-color);
    opacity: 0;
    transform: translateX(-10px);
    transition: all 0.3s ease;
}

.card:hover .card-arrow {
    opacity: 1;
    transform: translateX(0);
}

/* Skills Section Styling */
.skills-section {
    margin: 2rem 0;
}

.skill-category {
    margin: 2rem 0;
}

.skill-category h3 {
    color: var(--md-default-fg-color);
    margin-bottom: 1rem;
    font-size: 1.2rem;
}

.skills-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin: 1rem 0;
}

.skill {
    display: inline-flex;
    align-items: center;
    padding: 0.75rem 1.25rem;
    background: var(--md-code-bg-color);
    border-radius: 2rem;
    color: var(--md-default-fg-color);
    text-decoration: none;
    transition: all 0.3s ease;
    border: 1px solid var(--md-default-fg-color--lightest);
}

.skill:hover {
    background: var(--md-primary-fg-color);
    color: var(--md-primary-bg-color);
    transform: translateY(-2px);
}

.skill .material-icons {
    margin-right: 0.5rem;
    font-size: 1.2rem;
}

/* Contact Section Styling */
.contact-section {
    text-align: center;
    margin: 3rem 0;
    padding: 2rem;
    background: var(--md-code-bg-color);
    border-radius: 1rem;
    transition: all 0.3s ease;
}

.contact-section:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.contact-section a {
    display: inline-flex;
    align-items: center;
    color: var(--md-primary-fg-color);
    text-decoration: none;
    font-size: 1.2rem;
    transition: color 0.3s ease;
}

.contact-section a:hover {
    color: var(--md-accent-fg-color);
}

.contact-icon {
    margin-right: 0.5rem;
    font-size: 1.5rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .grid.cards {
        grid-template-columns: 1fr;
    }

    .skills-grid {
        justify-content: center;
    }

    .skill {
        width: calc(50% - 1rem);
        justify-content: center;
    }
}

/* Dark Mode Adjustments */
[data-md-color-scheme="slate"] .card {
    background: var(--md-code-bg-color);
    border-color: var(--md-default-fg-color--lightest);
}

[data-md-color-scheme="slate"] .card:hover {
    border-color: var(--md-primary-fg-color);
}

[data-md-color-scheme="slate"] .contact-section {
    background: var(--md-code-bg-color);
}
</style>
