---
title: Mo Maher - Software Engineer & Tech Enthusiast
description: Personal website and blog of Mo Maher
---

<div class="hero-section">
    <div class="hero-content">
        <h1 class="animated-title">مرحباً! أنا محمد ماهر 👋</h1>
        <p class="hero-subtitle">مهندس برمجيات متخصص في تطوير حلول تقنية مبتكرة</p>
    </div>
</div>

<div class="page-layout">
    <aside class="sidebar">
        <div class="profile-card">
            <div class="profile-header">
                <div class="profile-image-wrapper">
                    <img src="assets/images/profile.jpg" alt="Mo Maher" class="profile-image">
                </div>
                <h2 class="profile-name">Mo Maher</h2>
                <p class="profile-title">Software Engineer</p>
            </div>
            
            <div class="profile-content">
                <div class="info-section">
                    <div class="info-item">
                        <span class="icon">:octicons-location-16:</span>
                        <span>Cairo, Egypt</span>
                    </div>
                    <div class="info-item">
                        <span class="icon">:octicons-briefcase-16:</span>
                        <span>5+ Years Experience</span>
                    </div>
                </div>
                
                <div class="skills-section">
                    <h3>Core Skills</h3>
                    <div class="skills-grid">
                        <div class="skill-item">
                            <span class="skill-icon">🐍</span>
                            <span class="skill-name">Python</span>
                        </div>
                        <div class="skill-item">
                            <span class="skill-icon">⚛️</span>
                            <span class="skill-name">React</span>
                        </div>
                        <div class="skill-item">
                            <span class="skill-icon">📱</span>
                            <span class="skill-name">Node.js</span>
                        </div>
                        <div class="skill-item">
                            <span class="skill-icon">☁️</span>
                            <span class="skill-name">Cloud</span>
                        </div>
                    </div>
                </div>
                
                <div class="social-section">
                    <a href="https://github.com/momaher" class="social-button github">
                        <span class="icon">:octicons-mark-github-16:</span>
                        <span>GitHub</span>
                    </a>
                    <a href="https://linkedin.com/in/momaher" class="social-button linkedin">
                        <span class="icon">:octicons-link-16:</span>
                        <span>LinkedIn</span>
                    </a>
                    <a href="/local-services" class="social-button services">
                        <span class="icon">:octicons-server-16:</span>
                        <span>Local Services</span>
                    </a>
                </div>
            </div>
        </div>
    </aside>

    <main class="main-content">
        <section class="featured-projects">
            <h2 class="section-title">مشاريع مميزة</h2>
            <div class="project-grid">
                <div class="project-card">
                    <div class="project-image">
                        <img src="assets/images/project1.jpg" alt="Cloud-Native Application">
                        <div class="project-overlay">
                            <span class="view-project">عرض المشروع</span>
                        </div>
                    </div>
                    <div class="project-content">
                        <h3>Cloud-Native Application</h3>
                        <p>تطبيق قابل للتطوير مبني على هيكلية Microservices باستخدام Kubernetes و Docker</p>
                        <div class="tech-stack">
                            <span class="tech-tag">Docker</span>
                            <span class="tech-tag">Kubernetes</span>
                            <span class="tech-tag">Go</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="latest-articles">
            <h2 class="section-title">أحدث المقالات</h2>
            <div class="articles-grid">
                <a href="blog/posts/building-scalable-systems/" class="article-card">
                    <div class="article-content">
                        <span class="article-category">System Design</span>
                        <h3>Building Scalable Systems</h3>
                        <p>تعلم المبادئ والممارسات لبناء أنظمة موزعة عالية القابلية للتطوير.</p>
                        <div class="article-meta">
                            <span class="date">January 25, 2024</span>
                            <span class="separator">•</span>
                            <span class="read-time">10 min read</span>
                        </div>
                    </div>
                </a>
            </div>
        </section>
    </main>
</div>

<style>
:root {
    --primary-color: #2196f3;
    --secondary-color: #1976d2;
    --text-color: #333;
    --bg-color: #fff;
    --card-bg: #ffffff;
    --hover-color: #e3f2fd;
}

.hero-section {
    text-align: center;
    padding: 4rem 2rem;
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    margin-bottom: 2rem;
}

.hero-content {
    max-width: 800px;
    margin: 0 auto;
}

.animated-title {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    animation: fadeInUp 0.8s ease-out;
}

.hero-subtitle {
    font-size: 1.2rem;
    opacity: 0.9;
    animation: fadeInUp 0.8s ease-out 0.2s backwards;
}

.page-layout {
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.profile-card {
    background: var(--card-bg);
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    overflow: hidden;
    transition: transform 0.3s ease;
}

.profile-card:hover {
    transform: translateY(-5px);
}

.profile-header {
    padding: 2rem;
    text-align: center;
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
}

.profile-image-wrapper {
    width: 120px;
    height: 120px;
    margin: 0 auto 1rem;
    border-radius: 50%;
    overflow: hidden;
    border: 4px solid white;
}

.profile-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.profile-content {
    padding: 1.5rem;
}

.skills-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-top: 1rem;
}

.skill-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem;
    background: var(--hover-color);
    border-radius: 8px;
    transition: transform 0.2s ease;
}

.skill-item:hover {
    transform: scale(1.05);
}

.social-button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.8rem;
    border-radius: 8px;
    color: white;
    text-decoration: none;
    margin-top: 1rem;
    transition: transform 0.2s ease;
}

.social-button.github {
    background: #24292e;
}

.social-button.linkedin {
    background: #0077b5;
}

.social-button:hover {
    transform: translateY(-2px);
}

.project-card {
    background: var(--card-bg);
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}

.project-card:hover {
    transform: translateY(-5px);
}

.project-image {
    position: relative;
    height: 200px;
    overflow: hidden;
}

.project-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.project-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0,0,0,0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.project-card:hover .project-overlay {
    opacity: 1;
}

.view-project {
    color: white;
    font-weight: bold;
    padding: 0.8rem 1.5rem;
    border: 2px solid white;
    border-radius: 25px;
}

.article-card {
    background: var(--card-bg);
    border-radius: 15px;
    padding: 1.5rem;
    text-decoration: none;
    color: var(--text-color);
    display: block;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}

.article-card:hover {
    transform: translateY(-5px);
}

.article-category {
    display: inline-block;
    padding: 0.3rem 0.8rem;
    background: var(--primary-color);
    color: white;
    border-radius: 15px;
    font-size: 0.9rem;
    margin-bottom: 1rem;
}

.section-title {
    font-size: 1.8rem;
    margin-bottom: 1.5rem;
    color: var(--text-color);
    border-bottom: 3px solid var(--primary-color);
    padding-bottom: 0.5rem;
    display: inline-block;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media (max-width: 768px) {
    .page-layout {
        grid-template-columns: 1fr;
    }
    
    .hero-section {
        padding: 2rem 1rem;
    }
    
    .animated-title {
        font-size: 2rem;
    }
}
</style>
