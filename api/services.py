from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psutil
import docker
import subprocess
from typing import Dict, List

app = FastAPI()

# Docker client
try:
    docker_client = docker.from_env()
except Exception as e:
    print(f"Warning: Could not connect to Docker: {e}")
    docker_client = None

class ServiceStatus(BaseModel):
    status: str
    details: Dict

class SystemMetrics(BaseModel):
    cpu_usage: float
    memory_usage: float
    disk_usage: float

@app.get("/api/services/status")
async def get_services_status():
    """Get status of all services"""
    services = {}
    
    # Docker status
    if docker_client:
        try:
            containers = docker_client.containers.list()
            services["docker"] = {
                "status": "running",
                "details": {
                    "containers": len(containers),
                    "images": len(docker_client.images.list())
                }
            }
        except:
            services["docker"] = {
                "status": "stopped",
                "details": {}
            }
    
    # Database status (PostgreSQL)
    try:
        result = subprocess.run(
            ["systemctl", "is-active", "postgresql"],
            capture_output=True,
            text=True
        )
        services["database"] = {
            "status": "running" if result.stdout.strip() == "active" else "stopped",
            "details": {
                "type": "PostgreSQL",
                "port": 5432
            }
        }
    except:
        services["database"] = {
            "status": "stopped",
            "details": {}
        }
    
    # Web server status (Nginx)
    try:
        result = subprocess.run(
            ["systemctl", "is-active", "nginx"],
            capture_output=True,
            text=True
        )
        services["webserver"] = {
            "status": "running" if result.stdout.strip() == "active" else "stopped",
            "details": {
                "type": "Nginx",
                "ports": [80, 443]
            }
        }
    except:
        services["webserver"] = {
            "status": "stopped",
            "details": {}
        }
    
    # Redis status
    try:
        result = subprocess.run(
            ["systemctl", "is-active", "redis"],
            capture_output=True,
            text=True
        )
        services["cache"] = {
            "status": "running" if result.stdout.strip() == "active" else "stopped",
            "details": {
                "type": "Redis"
            }
        }
    except:
        services["cache"] = {
            "status": "stopped",
            "details": {}
        }
    
    return services

@app.get("/api/system/metrics")
async def get_system_metrics():
    """Get system metrics"""
    return {
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent
    }

@app.post("/api/services/{service_name}/{action}")
async def control_service(service_name: str, action: str):
    """Control a service (start/stop/restart)"""
    if action not in ["start", "stop", "restart"]:
        raise HTTPException(status_code=400, detail="Invalid action")
    
    service_map = {
        "docker": "docker",
        "database": "postgresql",
        "webserver": "nginx",
        "cache": "redis"
    }
    
    if service_name not in service_map:
        raise HTTPException(status_code=404, detail="Service not found")
    
    try:
        subprocess.run(
            ["systemctl", action, service_map[service_name]],
            check=True
        )
        return {"message": f"Service {service_name} {action}ed successfully"}
    except subprocess.CalledProcessError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to {action} {service_name}: {str(e)}"
        )

# Update local-services.md to use these endpoints
@app.get("/api/services/update-script")
async def get_update_script():
    """Get the JavaScript code for updating the dashboard"""
    return {
        "code": """
        async function updateServiceStatus() {
            try {
                const response = await fetch('/api/services/status');
                const services = await response.json();
                
                for (const [serviceId, data] of Object.entries(services)) {
                    const card = document.getElementById(`${serviceId}-service`);
                    if (card) {
                        const badge = card.querySelector('.status-badge');
                        badge.setAttribute('data-status', data.status);
                        badge.textContent = data.status.charAt(0).toUpperCase() + data.status.slice(1);
                        
                        // Update details
                        if (data.details) {
                            for (const [key, value] of Object.entries(data.details)) {
                                const element = card.querySelector(`#${serviceId}-${key}`);
                                if (element) {
                                    element.textContent = value;
                                }
                            }
                        }
                    }
                }
            } catch (error) {
                console.error('Error updating service status:', error);
            }
        }

        async function updateSystemMetrics() {
            try {
                const response = await fetch('/api/system/metrics');
                const metrics = await response.json();
                
                document.getElementById('cpu-usage').textContent = `${metrics.cpu_usage}%`;
                document.getElementById('memory-usage').textContent = `${metrics.memory_usage}%`;
                document.getElementById('disk-usage').textContent = `${metrics.disk_usage}%`;
                
                // Update progress bars
                document.querySelectorAll('.metric-card').forEach(card => {
                    const value = parseInt(card.querySelector('.metric-value').textContent);
                    card.querySelector('.progress').style.width = `${value}%`;
                });
            } catch (error) {
                console.error('Error updating system metrics:', error);
            }
        }

        async function controlService(serviceId, action) {
            try {
                const response = await fetch(`/api/services/${serviceId}/${action}`, {
                    method: 'POST'
                });
                
                if (!response.ok) {
                    throw new Error('Failed to control service');
                }
                
                // Update status after action
                await updateServiceStatus();
            } catch (error) {
                console.error(`Error ${action}ing service:`, error);
                alert(`Failed to ${action} service. Please check the logs.`);
            }
        }

        // Add click handlers for action buttons
        document.querySelectorAll('.action-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                const action = this.classList.contains('restart') ? 'restart' : 'stop';
                const serviceCard = this.closest('.service-card');
                const serviceId = serviceCard.id.replace('-service', '');
                
                controlService(serviceId, action);
            });
        });

        // Initial update and set intervals
        updateServiceStatus();
        updateSystemMetrics();
        setInterval(updateServiceStatus, 5000);
        setInterval(updateSystemMetrics, 5000);
        """
    }
