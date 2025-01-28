---
title: Blog
description: Technical articles, tutorials, and insights
---

# Technical Blog

Welcome to my technical blog where I share insights, tutorials, and experiences in software development, cloud computing, and technology.

## Latest Posts

{%- for post in blog.posts %}
<div class="post-card">
    <div class="post-meta">
        <span class="post-date">{{ post.date }}</span>
        {% for tag in post.tags %}
        <span class="post-tag">{{ tag }}</span>
        {% endfor %}
    </div>
    <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
    <p>{{ post.description }}</p>
    <a href="{{ post.url }}" class="read-more">Read More →</a>
</div>
{%- endfor %}

## Categories

<div class="categories-grid">
    <a href="categories/cloud-computing/" class="category-card">
        <h3>Cloud Computing</h3>
        <p>Articles about AWS, GCP, Azure, and cloud architecture</p>
    </a>
    <a href="categories/web-development/" class="category-card">
        <h3>Web Development</h3>
        <p>Frontend and backend development tutorials</p>
    </a>
    <a href="categories/devops/" class="category-card">
        <h3>DevOps</h3>
        <p>CI/CD, containers, and infrastructure as code</p>
    </a>
    <a href="categories/programming/" class="category-card">
        <h3>Programming</h3>
        <p>Programming languages, algorithms, and best practices</p>
    </a>
</div>

<style>
.post-card {
    background: var(--md-code-bg-color);
    padding: 1.5rem;
    border-radius: 8px;
    margin-bottom: 2rem;
}

.post-meta {
    margin-bottom: 1rem;
}

.post-date {
    color: var(--md-default-fg-color--light);
    font-size: 0.9rem;
}

.post-tag {
    background: var(--md-primary-fg-color);
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 15px;
    font-size: 0.8rem;
    margin-left: 0.5rem;
}

.read-more {
    display: inline-block;
    margin-top: 1rem;
    color: var(--md-primary-fg-color);
    font-weight: bold;
    text-decoration: none;
}

.categories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.category-card {
    background: var(--md-code-bg-color);
    padding: 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    color: inherit;
    transition: transform 0.2s;
}

.category-card:hover {
    transform: translateY(-5px);
}

.category-card h3 {
    color: var(--md-primary-fg-color);
    margin-top: 0;
}

.category-card p {
    margin-bottom: 0;
    opacity: 0.8;
}
</style>
