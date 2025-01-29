---
title: Mo Maher - Software Engineer & Tech Enthusiast
description: Personal website and blog of Mo Maher
---

# Welcome to My Digital Space

<div class="animate-fade-in">
    <div class="grid-container">
        <div class="card animate-scale">
            <h3>:fontawesome-solid-wand-magic-sparkles: Creative Developer</h3>
            <p>Turning complex ideas into elegant solutions through creative coding and innovative thinking.</p>
        </div>
        <div class="card animate-scale" style="animation-delay: 0.2s">
            <h3>:fontawesome-solid-pen-fancy: Tech Writer</h3>
            <p>Sharing knowledge and experiences through engaging technical content and tutorials.</p>
        </div>
        <div class="card animate-scale" style="animation-delay: 0.4s">
            <h3>:fontawesome-solid-rocket: Innovation</h3>
            <p>Always exploring new technologies and pushing the boundaries of what's possible.</p>
        </div>
    </div>
</div>

## About Me { .animate-slide-up }

<div class="animate-fade-in" style="animation-delay: 0.6s">
<img src="assets/images/profile.jpg" alt="Profile Picture" class="profile-image" width="250">

I'm a passionate Software Engineer who loves creating amazing digital experiences. My expertise includes:

- :simple-python: **Python Development** - Building scalable applications and automation tools
- :simple-javascript: **Modern Web Development** - Creating responsive and interactive web applications
- :simple-docker: **DevOps & Cloud** - Implementing efficient deployment pipelines
- :simple-linux: **Open Source** - Contributing to and maintaining open source projects
</div>

## Latest Articles { .animate-slide-up }

<div class="grid-container">
    <div class="card animate-scale" style="animation-delay: 0.8s">
        <h3>:fontawesome-solid-book: Modern Web Development</h3>
        <p>Exploring the latest trends and best practices in web development.</p>
        <a href="/blog/modern-web-dev" class="md-button">Read More</a>
    </div>
    <div class="card animate-scale" style="animation-delay: 1s">
        <h3>:fontawesome-solid-microchip: AI & Machine Learning</h3>
        <p>Diving into the world of artificial intelligence and its applications.</p>
        <a href="/blog/ai-ml-guide" class="md-button">Read More</a>
    </div>
</div>

## Featured Projects { .animate-slide-up }

<div class="timeline">
    <div class="timeline-item animate-scale" style="animation-delay: 1.2s">
        <h3>:fontawesome-solid-star: Project Nova</h3>
        <p>A revolutionary project that pushes the boundaries of modern web development.</p>
        <a href="/portfolio/project-nova" class="md-button">Learn More</a>
    </div>
    <div class="timeline-item animate-scale" style="animation-delay: 1.4s">
        <h3>:fontawesome-solid-bolt: Project Lightning</h3>
        <p>High-performance computing solution for complex data processing.</p>
        <a href="/portfolio/project-lightning" class="md-button">Explore</a>
    </div>
</div>

[View All Projects](portfolio.md){ .md-button .animate-scale }

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

/* New Styles */

.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 1.5rem 0;
}

.animate-fade-in {
    animation: fade-in 1s;
}

.animate-slide-up {
    animation: slide-up 1s;
}

@keyframes fade-in {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

@keyframes slide-up {
    from {
        transform: translateY(20px);
    }
    to {
        transform: translateY(0);
    }
}

.timeline {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
    background: var(--md-code-bg-color);
    border-radius: 1rem;
    transition: all 0.3s ease;
}

.timeline-item {
    margin-bottom: 1.5rem;
    padding: 1.5rem;
    background: var(--md-code-bg-color);
    border-radius: 0.8rem;
    transition: all 0.3s ease;
    border: 1px solid var(--md-default-fg-color--lightest);
}

.timeline-item:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    border-color: var(--md-primary-fg-color);
}

.md-button {
    display: inline-block;
    padding: 0.75rem 1.25rem;
    background: var(--md-primary-fg-color);
    color: var(--md-primary-bg-color);
    text-decoration: none;
    transition: all 0.3s ease;
    border-radius: 2rem;
}

.md-button:hover {
    background: var(--md-accent-fg-color);
    color: var(--md-accent-bg-color);
    transform: translateY(-2px);
}
</style>
