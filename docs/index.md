---
title: Mo Maher - Software Engineer & Tech Enthusiast
description: Personal website and blog of Mo Maher
---

# Welcome to My Blog! 👋

<div class="page-layout">
    <aside class="sidebar">
        <div class="about-card">
            <div class="about-header">
                <div class="profile-image">
                    <img src="assets/images/profile.jpg" alt="Mo Maher">
                </div>
                <h2>Mo Maher</h2>
                <p class="title">Software Engineer</p>
            </div>
            
            <div class="about-content">
                <div class="info-item">
                    <span class="icon">:octicons-location-16:</span>
                    <span>Cairo, Egypt</span>
                </div>
                <div class="info-item">
                    <span class="icon">:octicons-briefcase-16:</span>
                    <span>5+ Years Experience</span>
                </div>
                
                <div class="skills">
                    <span class="skill-tag">Python</span>
                    <span class="skill-tag">JavaScript</span>
                    <span class="skill-tag">React</span>
                    <span class="skill-tag">Node.js</span>
                </div>
                
                <div class="social-links">
                    <a href="https://github.com/momaher" class="social-link">
                        <span class="icon">:octicons-mark-github-16:</span>
                        <span>GitHub</span>
                    </a>
                    <a href="https://linkedin.com/in/momaher" class="social-link">
                        <span class="icon">:octicons-link-16:</span>
                        <span>LinkedIn</span>
                    </a>
                </div>
            </div>
        </div>
    </aside>

    <main class="main-content">
        <p class="intro">
            Welcome to my personal blog! Here, I share my experiences, insights, and knowledge about software development,
            cloud architecture, and technology trends.
        </p>

        <section class="featured-projects">
            <h2>Featured Projects</h2>
            <div class="project-grid">
                <div class="project-card">
                    <div class="project-image">
                        <img src="assets/images/project1.jpg" alt="Project 1">
                    </div>
                    <div class="project-content">
                        <h3>Cloud-Native Application</h3>
                        <p>A scalable microservices architecture built with Kubernetes and Docker.</p>
                        <div class="tech-tags">
                            <span class="tech-tag">Docker</span>
                            <span class="tech-tag">Kubernetes</span>
                            <span class="tech-tag">Go</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="latest-articles">
            <h2>Latest Articles</h2>
            <div class="article-grid">
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
    </main>
</div>

<style>
.page-layout {
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

.sidebar {
    position: sticky;
    top: 2rem;
}

.about-card {
    background: var(--md-primary-fg-color--light);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.about-header {
    text-align: center;
    padding: 2rem;
    background: linear-gradient(to bottom, var(--md-primary-fg-color--light), white);
}

.profile-image {
    width: 120px;
    height: 120px;
    margin: 0 auto 1rem;
    border-radius: 50%;
    overflow: hidden;
    border: 3px solid white;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.profile-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.about-header h2 {
    margin: 0;
    color: var(--md-primary-fg-color);
    font-size: 1.5rem;
}

.about-header .title {
    color: var(--md-primary-fg-color);
    margin: 0.5rem 0 0;
    font-size: 1.1rem;
}

.about-content {
    padding: 1.5rem;
}

.info-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.8rem;
    color: var(--md-typeset-color);
}

.skills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 1.5rem 0;
}

.skill-tag {
    background: rgba(var(--md-primary-fg-color--rgb), 0.1);
    color: var(--md-primary-fg-color);
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
    font-size: 0.9rem;
}

.social-links {
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
    margin-top: 1.5rem;
}

.social-link {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--md-typeset-color);
    text-decoration: none;
    padding: 0.5rem;
    border-radius: 8px;
    transition: all 0.3s ease;
}

.social-link:hover {
    background: rgba(var(--md-primary-fg-color--rgb), 0.1);
    color: var(--md-primary-fg-color);
}

.intro {
    font-size: 1.2rem;
    line-height: 1.6;
    color: var(--md-typeset-color);
    margin-bottom: 3rem;
}

@media (max-width: 768px) {
    .page-layout {
        grid-template-columns: 1fr;
        padding: 1rem;
    }
    
    .sidebar {
        position: static;
        margin-bottom: 2rem;
    }
}
</style>
