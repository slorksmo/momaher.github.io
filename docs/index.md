---
title: Mo Maher - Software Engineer & Tech Enthusiast
description: Personal website and blog of Mo Maher
---

<div class="hero">
    <div class="hero-content">
        <img src="assets/images/profile.jpg" alt="Mo Maher" class="profile-image">
        <h1>Mo Maher</h1>
        <p class="subtitle">Software Engineer & Tech Enthusiast</p>
        <div class="social-links">
            <a href="https://github.com/slorksmo" target="_blank" title="GitHub"><span class="twemoji">{% include ".icons/fontawesome/brands/github.svg" %}</span></a>
            <a href="https://linkedin.com/in/slorksmo" target="_blank" title="LinkedIn"><span class="twemoji">{% include ".icons/fontawesome/brands/linkedin.svg" %}</span></a>
            <a href="https://twitter.com/slorksmo" target="_blank" title="Twitter"><span class="twemoji">{% include ".icons/fontawesome/brands/twitter.svg" %}</span></a>
        </div>
    </div>
</div>

## Featured Articles

<div class="grid-container">
    <div class="grid-item">
        <a href="blog/post1">
            <div class="article-card">
                <img src="assets/images/article1.jpg" alt="Article 1">
                <h3>Building Scalable Systems</h3>
                <p>Learn about building highly scalable distributed systems...</p>
                <span class="read-more">Read More →</span>
            </div>
        </a>
    </div>
    <div class="grid-item">
        <a href="blog/post2">
            <div class="article-card">
                <img src="assets/images/article2.jpg" alt="Article 2">
                <h3>Cloud Native Applications</h3>
                <p>Best practices for developing cloud native applications...</p>
                <span class="read-more">Read More →</span>
            </div>
        </a>
    </div>
</div>

## Latest Projects

<div class="project-showcase">
    <div class="project-card">
        <img src="assets/images/project1.jpg" alt="Project 1">
        <div class="project-info">
            <h3>Project Name</h3>
            <p>Brief description of the project and its impact...</p>
            <div class="tech-stack">
                <span class="tech-tag">React</span>
                <span class="tech-tag">Node.js</span>
                <span class="tech-tag">MongoDB</span>
            </div>
            <a href="portfolio#project-1" class="project-link">View Details →</a>
        </div>
    </div>
</div>

## Newsletter
<div class="newsletter-section">
    <h3>Stay Updated</h3>
    <p>Subscribe to my newsletter for the latest articles, tutorials, and tech insights.</p>
    <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST" class="newsletter-form">
        <input type="email" name="email" placeholder="Your email address" required>
        <button type="submit">Subscribe</button>
    </form>
</div>

<style>
.hero {
    text-align: center;
    padding: 4rem 0;
    background: linear-gradient(to right, var(--md-primary-fg-color--light), var(--md-primary-fg-color));
    color: white;
    border-radius: 8px;
    margin-bottom: 3rem;
}

.profile-image {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    border: 4px solid white;
    margin-bottom: 1rem;
}

.subtitle {
    font-size: 1.2rem;
    opacity: 0.9;
}

.social-links {
    margin-top: 1rem;
}

.social-links a {
    margin: 0 0.5rem;
    color: white;
    font-size: 1.5rem;
}

.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.article-card {
    background: var(--md-code-bg-color);
    border-radius: 8px;
    overflow: hidden;
    transition: transform 0.2s;
}

.article-card:hover {
    transform: translateY(-5px);
}

.article-card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.article-card h3 {
    padding: 1rem;
    margin: 0;
}

.article-card p {
    padding: 0 1rem;
}

.read-more {
    display: block;
    padding: 1rem;
    color: var(--md-primary-fg-color);
    font-weight: bold;
}

.project-card {
    display: flex;
    background: var(--md-code-bg-color);
    border-radius: 8px;
    overflow: hidden;
    margin: 2rem 0;
}

.project-card img {
    width: 300px;
    height: 200px;
    object-fit: cover;
}

.project-info {
    padding: 1.5rem;
}

.tech-stack {
    margin: 1rem 0;
}

.tech-tag {
    background: var(--md-primary-fg-color);
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 15px;
    font-size: 0.9rem;
    margin-right: 0.5rem;
}

.project-link {
    color: var(--md-primary-fg-color);
    font-weight: bold;
    text-decoration: none;
}

.newsletter-section {
    background: var(--md-code-bg-color);
    padding: 2rem;
    border-radius: 8px;
    text-align: center;
    margin: 3rem 0;
}

.newsletter-form {
    display: flex;
    gap: 1rem;
    max-width: 500px;
    margin: 1rem auto;
}

.newsletter-form input {
    flex: 1;
    padding: 0.75rem;
    border: 1px solid #ddd;
    border-radius: 4px;
}

.newsletter-form button {
    background: var(--md-primary-fg-color);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
}

.newsletter-form button:hover {
    opacity: 0.9;
}

@media (max-width: 768px) {
    .project-card {
        flex-direction: column;
    }
    
    .project-card img {
        width: 100%;
    }
    
    .newsletter-form {
        flex-direction: column;
    }
}
</style>
