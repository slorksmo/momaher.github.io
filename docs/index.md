---
title: Mo Maher - Software Engineer & Tech Enthusiast
description: Personal website and blog of Mo Maher
---

# Welcome to My Personal Blog

<div class="hero">
    <div class="hero-content">
        <img src="assets/images/profile.jpg" alt="Mo Maher" class="profile-image">
        <h1>Mo Maher</h1>
        <p class="subtitle">Software Engineer & Tech Enthusiast</p>
        <div class="social-links">
            [:fontawesome-brands-github:{ .icon } GitHub](https://github.com/slorksmo){ .social-link }
            [:fontawesome-brands-linkedin:{ .icon } LinkedIn](https://linkedin.com/in/momaher94){ .social-link }
            [:fontawesome-brands-twitter:{ .icon } Twitter](https://twitter.com/mo_maher94){ .social-link }
        </div>
    </div>
</div>

## Featured Articles

<div class="grid cards" markdown>

- [:fontawesome-solid-cloud:{ .lg .middle } __Building Scalable Systems__](blog/posts/building-scalable-systems.md)

    ---
    Learn about best practices and patterns for building scalable software systems.

- [:fontawesome-solid-microchip:{ .lg .middle } __Cloud Native Applications__](blog/posts/cloud-native-apps.md)

    ---
    Explore modern cloud-native application development principles.

</div>

## Latest Projects

<div class="grid cards" markdown>

- [:fontawesome-solid-code:{ .lg .middle } __Project 1__](portfolio/project1.md)

    ---
    Description of your first featured project.

- [:fontawesome-solid-database:{ .lg .middle } __Project 2__](portfolio/project2.md)

    ---
    Description of your second featured project.

</div>

## Technical Skills

- [:fontawesome-brands-python:{ .lg } Python](){ .skill }
- [:fontawesome-brands-js:{ .lg } JavaScript](){ .skill }
- [:fontawesome-brands-docker:{ .lg } Docker](){ .skill }
- [:fontawesome-brands-aws:{ .lg } AWS](){ .skill }
- [:fontawesome-brands-git:{ .lg } Git](){ .skill }

## Get in Touch

[:fontawesome-regular-envelope:{ .lg } Feel free to contact me](contact.md) for collaborations or questions!

<style>
.hero {
    text-align: center;
    padding: 2rem 0;
}

.hero-content {
    max-width: 800px;
    margin: 0 auto;
}

.profile-image {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    margin-bottom: 1rem;
}

.subtitle {
    font-size: 1.2rem;
    color: var(--md-default-fg-color--light);
    margin-bottom: 1.5rem;
}

.social-links {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin-top: 1rem;
}

.social-link {
    color: var(--md-default-fg-color--light);
    text-decoration: none;
    transition: color 0.2s;
}

.social-link:hover {
    color: var(--md-primary-fg-color);
}

.icon {
    margin-right: 0.5rem;
}

.lg {
    font-size: 1.5rem;
}

.middle {
    vertical-align: middle;
}

.skill {
    display: inline-block;
    margin: 0.5rem;
    padding: 0.5rem 1rem;
    background: var(--md-code-bg-color);
    border-radius: 4px;
    text-decoration: none;
    color: var(--md-default-fg-color);
}

.skill:hover {
    background: var(--md-code-fg-color);
    color: var(--md-code-bg-color);
}

.grid.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
}

.grid.cards > * {
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 0.5rem;
    padding: 1rem;
}
</style>
