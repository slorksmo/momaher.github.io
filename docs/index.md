---
title: Mo Maher - Software Engineer & Tech Enthusiast
description: Personal website and blog of Mo Maher
---

# Welcome to My Blog! 👋

<div class="page-layout">
    <!-- Sidebar with About Me -->
    <div class="sidebar">
        <div class="profile-sidebar animate-fade-in">
            <div class="profile-image-container">
                <img src="assets/images/profile.jpg" alt="Mo Maher" class="profile-image">
            </div>
            <div class="profile-info">
                <h2>Mo Maher</h2>
                <p>Software Engineer</p>
                
                <h3>:octicons-location-16: Location</h3>
                <p>Cairo, Egypt</p>
                
                <h3>:octicons-tools-16: Tech Stack</h3>
                <div class="tech-stack">
                    <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
                    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black" alt="JavaScript">
                    <img src="https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black" alt="React">
                    <img src="https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white" alt="Node.js">
                    <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white" alt="Docker">
                </div>
                
                <div class="profile-links">
                    <a href="https://github.com/momaher" class="profile-link">
                        :octicons-mark-github-16: GitHub
                    </a>
                    <a href="https://linkedin.com/in/momaher" class="profile-link">
                        :octicons-link-16: LinkedIn
                    </a>
                    <a href="mailto:contact@momaher.com" class="profile-link">
                        :octicons-mail-16: Email
                    </a>
                </div>
            </div>
        </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
        <div class="hero-section animate-fade-in">
            <p>
                Welcome to my personal blog! Here, I share my experiences, insights, and knowledge about software development,
                cloud architecture, and technology trends.
            </p>
        </div>

        <section class="featured-projects animate-fade-in">
            <h2>Featured Projects</h2>
            <div class="project-grid">
                <div class="project-card">
                    <div class="project-image">
                        <img src="assets/images/project1.jpg" alt="Project 1">
                    </div>
                    <div class="project-content">
                        <h3>Cloud-Native Application</h3>
                        <p>A scalable microservices architecture built with Kubernetes and Docker.</p>
                        <div class="project-tech">
                            <span class="tech-tag">Docker</span>
                            <span class="tech-tag">Kubernetes</span>
                            <span class="tech-tag">Go</span>
                        </div>
                    </div>
                </div>
                <div class="project-card">
                    <div class="project-image">
                        <img src="assets/images/project2.jpg" alt="Project 2">
                    </div>
                    <div class="project-content">
                        <h3>AI-Powered Analytics</h3>
                        <p>Real-time data analytics platform using machine learning algorithms.</p>
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">TensorFlow</span>
                            <span class="tech-tag">AWS</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="latest-articles animate-fade-in">
            <h2>Latest Articles</h2>
            <div class="articles-preview">
                <a href="blog/posts/building-scalable-systems/" class="article-card">
                    <h3>Building Scalable Systems</h3>
                    <p>Learn about the principles and practices for building highly scalable distributed systems.</p>
                    <div class="article-meta">
                        <span class="date">January 25, 2024</span>
                        <span class="read-time">10 min read</span>
                    </div>
                </a>
            </div>
        </section>
    </div>
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

.about-section {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: 2rem 0;
}

.profile-sidebar {
    width: 30%;
    margin-right: 2rem;
}

.profile-image-container {
    width: 100%;
    height: 200px;
    border-radius: 1rem;
    overflow: hidden;
    margin-bottom: 1rem;
}

.profile-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.profile-info {
    padding: 1rem;
    background: var(--md-code-bg-color);
    border-radius: 1rem;
    border: 1px solid var(--md-default-fg-color--lightest);
}

.profile-info h2 {
    margin-top: 0;
}

.profile-links {
    margin-top: 1rem;
}

.profile-link {
    display: inline-block;
    margin-right: 1rem;
    color: var(--md-primary-fg-color);
    text-decoration: none;
    transition: color 0.3s ease;
}

.profile-link:hover {
    color: var(--md-accent-fg-color);
}

.main-content {
    width: 70%;
}

@media (max-width: 768px) {
    .about-section {
        flex-direction: column;
    }

    .profile-sidebar {
        width: 100%;
        margin-right: 0;
        margin-bottom: 2rem;
    }

    .main-content {
        width: 100%;
    }
}

.project-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 1.5rem 0;
}

.project-card {
    padding: 1.5rem;
    background: var(--md-code-bg-color);
    border-radius: 0.8rem;
    transition: all 0.3s ease;
    border: 1px solid var(--md-default-fg-color--lightest);
}

.project-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    border-color: var(--md-primary-fg-color);
}

.project-image {
    width: 100%;
    height: 150px;
    border-radius: 0.8rem;
    overflow: hidden;
    margin-bottom: 1rem;
}

.project-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.project-tech {
    margin-top: 1rem;
}

.tech-tag {
    display: inline-block;
    padding: 0.25rem 0.5rem;
    background: var(--md-code-bg-color);
    border-radius: 2rem;
    color: var(--md-default-fg-color);
    margin-right: 0.5rem;
}

.articles-preview {
    margin-top: 2rem;
}

.article-card {
    padding: 1.5rem;
    background: var(--md-code-bg-color);
    border-radius: 0.8rem;
    transition: all 0.3s ease;
    border: 1px solid var(--md-default-fg-color--lightest);
}

.article-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    border-color: var(--md-primary-fg-color);
}

.read-more {
    font-size: 0.8rem;
    color: var(--md-primary-fg-color);
    margin-top: 0.5rem;
    display: block;
}

.page-layout {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: 2rem 0;
}

.sidebar {
    width: 30%;
    margin-right: 2rem;
}

.main-content {
    width: 70%;
}

@media (max-width: 768px) {
    .page-layout {
        flex-direction: column;
    }

    .sidebar {
        width: 100%;
        margin-right: 0;
        margin-bottom: 2rem;
    }

    .main-content {
        width: 100%;
    }
}
</style>
