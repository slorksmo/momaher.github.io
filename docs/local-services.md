---
title: Local Services Dashboard
description: Dashboard for monitoring and managing local services
---

<div class="services-dashboard">
    <div class="dashboard-header">
        <h1>لوحة التحكم بالخدمات المحلية</h1>
        <p class="dashboard-subtitle">مراقبة وإدارة الخدمات المحلية على السيرفر</p>
    </div>

    <div class="services-grid">
        <!-- Docker Service -->
        <div class="service-card" id="docker-service">
            <div class="service-header">
                <span class="service-icon">🐳</span>
                <h3>Docker</h3>
                <span class="status-badge" data-status="running">Running</span>
            </div>
            <div class="service-details">
                <div class="detail-item">
                    <span class="label">Containers:</span>
                    <span class="value" id="docker-containers">-</span>
                </div>
                <div class="detail-item">
                    <span class="label">Images:</span>
                    <span class="value" id="docker-images">-</span>
                </div>
            </div>
            <div class="service-actions">
                <button class="action-btn restart">Restart</button>
                <button class="action-btn stop">Stop</button>
            </div>
        </div>

        <!-- Database Service -->
        <div class="service-card" id="database-service">
            <div class="service-header">
                <span class="service-icon">🗄️</span>
                <h3>Database</h3>
                <span class="status-badge" data-status="running">Running</span>
            </div>
            <div class="service-details">
                <div class="detail-item">
                    <span class="label">Type:</span>
                    <span class="value">PostgreSQL</span>
                </div>
                <div class="detail-item">
                    <span class="label">Port:</span>
                    <span class="value">5432</span>
                </div>
            </div>
            <div class="service-actions">
                <button class="action-btn restart">Restart</button>
                <button class="action-btn stop">Stop</button>
            </div>
        </div>

        <!-- Web Server -->
        <div class="service-card" id="webserver-service">
            <div class="service-header">
                <span class="service-icon">🌐</span>
                <h3>Web Server</h3>
                <span class="status-badge" data-status="running">Running</span>
            </div>
            <div class="service-details">
                <div class="detail-item">
                    <span class="label">Type:</span>
                    <span class="value">Nginx</span>
                </div>
                <div class="detail-item">
                    <span class="label">Port:</span>
                    <span class="value">80, 443</span>
                </div>
            </div>
            <div class="service-actions">
                <button class="action-btn restart">Restart</button>
                <button class="action-btn stop">Stop</button>
            </div>
        </div>

        <!-- Cache Service -->
        <div class="service-card" id="cache-service">
            <div class="service-header">
                <span class="service-icon">⚡</span>
                <h3>Cache</h3>
                <span class="status-badge" data-status="running">Running</span>
            </div>
            <div class="service-details">
                <div class="detail-item">
                    <span class="label">Type:</span>
                    <span class="value">Redis</span>
                </div>
                <div class="detail-item">
                    <span class="label">Memory:</span>
                    <span class="value" id="redis-memory">-</span>
                </div>
            </div>
            <div class="service-actions">
                <button class="action-btn restart">Restart</button>
                <button class="action-btn stop">Stop</button>
            </div>
        </div>
    </div>

    <div class="system-metrics">
        <h2>معلومات النظام</h2>
        <div class="metrics-grid">
            <div class="metric-card">
                <h4>CPU Usage</h4>
                <div class="metric-value" id="cpu-usage">-%</div>
                <div class="progress-bar">
                    <div class="progress" style="width: 0%"></div>
                </div>
            </div>
            <div class="metric-card">
                <h4>Memory Usage</h4>
                <div class="metric-value" id="memory-usage">-%</div>
                <div class="progress-bar">
                    <div class="progress" style="width: 0%"></div>
                </div>
            </div>
            <div class="metric-card">
                <h4>Disk Usage</h4>
                <div class="metric-value" id="disk-usage">-%</div>
                <div class="progress-bar">
                    <div class="progress" style="width: 0%"></div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
:root {
    --primary-color: #2196f3;
    --secondary-color: #1976d2;
    --success-color: #4caf50;
    --warning-color: #ff9800;
    --danger-color: #f44336;
    --text-color: #333;
    --bg-color: #f5f5f5;
    --card-bg: #ffffff;
}

.services-dashboard {
    padding: 2rem;
    background: var(--bg-color);
    min-height: 100vh;
}

.dashboard-header {
    text-align: center;
    margin-bottom: 3rem;
}

.dashboard-header h1 {
    font-size: 2.5rem;
    color: var(--text-color);
    margin-bottom: 0.5rem;
}

.dashboard-subtitle {
    color: #666;
    font-size: 1.2rem;
}

.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
}

.service-card {
    background: var(--card-bg);
    border-radius: 15px;
    padding: 1.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
}

.service-card:hover {
    transform: translateY(-5px);
}

.service-header {
    display: flex;
    align-items: center;
    margin-bottom: 1.5rem;
}

.service-icon {
    font-size: 2rem;
    margin-right: 1rem;
}

.service-header h3 {
    margin: 0;
    flex-grow: 1;
}

.status-badge {
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
    font-size: 0.9rem;
    font-weight: 500;
}

.status-badge[data-status="running"] {
    background: rgba(76, 175, 80, 0.1);
    color: var(--success-color);
}

.status-badge[data-status="stopped"] {
    background: rgba(244, 67, 54, 0.1);
    color: var(--danger-color);
}

.service-details {
    margin-bottom: 1.5rem;
}

.detail-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.5rem;
}

.label {
    color: #666;
}

.service-actions {
    display: flex;
    gap: 1rem;
}

.action-btn {
    flex: 1;
    padding: 0.8rem;
    border: none;
    border-radius: 8px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
}

.action-btn.restart {
    background: rgba(33, 150, 243, 0.1);
    color: var(--primary-color);
}

.action-btn.stop {
    background: rgba(244, 67, 54, 0.1);
    color: var(--danger-color);
}

.action-btn:hover {
    filter: brightness(0.9);
}

.system-metrics {
    background: var(--card-bg);
    border-radius: 15px;
    padding: 2rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.system-metrics h2 {
    margin-bottom: 2rem;
    text-align: center;
}

.metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}

.metric-card {
    text-align: center;
}

.metric-value {
    font-size: 2rem;
    font-weight: 600;
    margin: 1rem 0;
}

.progress-bar {
    background: #eee;
    height: 8px;
    border-radius: 4px;
    overflow: hidden;
}

.progress {
    height: 100%;
    background: var(--primary-color);
    transition: width 0.3s ease;
}

@media (max-width: 768px) {
    .services-dashboard {
        padding: 1rem;
    }
    
    .dashboard-header h1 {
        font-size: 2rem;
    }
    
    .services-grid {
        grid-template-columns: 1fr;
    }
}
</style>

<script>
// Fetch and inject the dashboard update script
async function loadDashboardScript() {
    try {
        const response = await fetch('/api/services/update-script');
        const data = await response.json();
        const script = document.createElement('script');
        script.textContent = data.code;
        document.body.appendChild(script);
    } catch (error) {
        console.error('Error loading dashboard script:', error);
    }
}

document.addEventListener('DOMContentLoaded', loadDashboardScript);
</script>
