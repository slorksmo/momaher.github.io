---
title: Mo Maher - Software Engineer & Tech Enthusiast
description: Personal website and blog of Mo Maher
---

# Welcome to My Digital Space

<div class="animate-fade-in">
    <div class="grid-container">
        <div class="card animate-scale">
            <h3>:fontawesome-solid-code: Full Stack Developer</h3>
            <p>Specializing in Python, JavaScript, and cloud technologies with 5+ years of experience.</p>
        </div>
        <div class="card animate-scale" style="animation-delay: 0.2s">
            <h3>:fontawesome-solid-cloud: Cloud Architect</h3>
            <p>Designing and implementing scalable solutions on AWS and Google Cloud Platform.</p>
        </div>
        <div class="card animate-scale" style="animation-delay: 0.4s">
            <h3>:fontawesome-solid-graduation-cap: Tech Educator</h3>
            <p>Contributing to the developer community through articles, tutorials, and open source.</p>
        </div>
    </div>
</div>

<div class="about-section animate-fade-in">
    <div class="profile-sidebar">
        <div class="profile-image-container">
            <img src="assets/images/profile.jpg" alt="Profile Picture" class="profile-image">
        </div>
        <div class="profile-info">
            <h2>About Me</h2>
            <p>Senior Software Engineer with expertise in building scalable web applications and distributed systems. Currently focused on cloud-native solutions and DevOps practices.</p>
            
            <h3>:octicons-info-16: Quick Facts</h3>
            <ul class="profile-facts">
                <li>:octicons-briefcase-16: Senior Software Engineer at Tech Solutions Inc.</li>
                <li>:octicons-location-16: Cairo, Egypt</li>
                <li>:octicons-mortar-board-16: B.Sc. in Computer Science</li>
                <li>:octicons-code-16: Python, JavaScript, Go</li>
                <li>:octicons-cloud-16: AWS Certified Solutions Architect</li>
            </ul>
            
            <h3>:simple-github: GitHub Activity</h3>
            <img src="https://github-readme-stats.vercel.app/api?username=momaher&show_icons=true&theme=transparent" alt="GitHub Stats" class="github-stats">
            
            <h3>:octicons-tools-16: Tech Stack</h3>
            <div class="tech-stack">
                <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
                <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
                <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
                <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS">
                <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
            </div>
            
            <div class="profile-links">
                <a href="https://github.com/momaher" class="profile-link">
                    :simple-github: GitHub
                </a>
                <a href="https://linkedin.com/in/momaher94" class="profile-link">
                    :simple-linkedin: LinkedIn
                </a>
                <a href="https://twitter.com/mo_maher94" class="profile-link">
                    :simple-twitter: Twitter
                </a>
            </div>
        </div>
    </div>
    
    <div class="main-content">
        <h2>Featured Projects</h2>
        
        <div class="project-grid">
            <div class="project-card">
                <div class="project-image">
                    <img src="assets/images/projects/cloudops-dashboard.png" alt="CloudOps Dashboard">
                </div>
                <h3>:fontawesome-solid-cloud: CloudOps Dashboard</h3>
                <p>A modern dashboard for monitoring and managing cloud infrastructure. Built with React and integrates with multiple cloud providers.</p>
                <div class="project-tech">
                    <span class="tech-tag">React</span>
                    <span class="tech-tag">TypeScript</span>
                    <span class="tech-tag">AWS</span>
                </div>
                <a href="#" class="md-button">View Project</a>
            </div>
            
            <div class="project-card">
                <div class="project-image">
                    <img src="assets/images/projects/data-pipeline.png" alt="Data Pipeline Framework">
                </div>
                <h3>:fontawesome-solid-database: Data Pipeline Framework</h3>
                <p>An efficient ETL framework for processing large-scale data. Supports real-time processing and multiple data sources.</p>
                <div class="project-tech">
                    <span class="tech-tag">Python</span>
                    <span class="tech-tag">Apache Kafka</span>
                    <span class="tech-tag">PostgreSQL</span>
                </div>
                <a href="#" class="md-button">Explore</a>
            </div>
            
            <div class="project-card">
                <div class="project-image">
                    <img src="assets/images/projects/api-gateway.png" alt="API Gateway Service">
                </div>
                <h3>:fontawesome-solid-network-wired: API Gateway Service</h3>
                <p>A high-performance API Gateway with built-in authentication, rate limiting, and monitoring capabilities.</p>
                <div class="project-tech">
                    <span class="tech-tag">Go</span>
                    <span class="tech-tag">Redis</span>
                    <span class="tech-tag">Docker</span>
                </div>
                <a href="#" class="md-button">Learn More</a>
            </div>
        </div>
        
        <h2>Latest Articles</h2>
        <div class="articles-preview">
            <a href="blog/posts/building-scalable-systems/" class="article-card">
                <h3>Building Scalable Systems: A Comprehensive Guide</h3>
                <p>Learn the key principles and best practices for building highly scalable distributed systems.</p>
                <span class="read-more">Read More →</span>
            </a>
        </div>
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
</style>
