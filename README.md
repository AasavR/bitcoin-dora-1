📦 Cortensor Infra

Infrastructure and service code for deploying Cortensor on Kubernetes using Terraform, FastAPI, and Prometheus/Grafana monitoring.

📂 Project Structure
cortensor_infra/
│── README.md
│── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│── app/
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│── monitoring/
│   ├── prometheus.yaml
│   ├── grafana-dashboards/
│       └── cortensor-dashboard.json

🚀 Setup Instructions
1. Provision Infrastructure (Terraform)
cd terraform
terraform init
terraform apply -auto-approve


This will set up the Kubernetes cluster (EKS/GKE/AKS depending on your provider).

2. Build & Push Docker Image
cd app
docker build -t cortensor-app:latest .
docker tag cortensor-app:latest <your-dockerhub-username>/cortensor-app:latest
docker push <your-dockerhub-username>/cortensor-app:latest

3. Deploy to Kubernetes
cd ../k8s
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml

4. Access the FastAPI App

Once deployed, check service:

kubectl get svc cortensor-service


Visit the EXTERNAL-IP at /docs to view FastAPI Swagger UI.

5. Monitoring Setup (Prometheus + Grafana)
cd ../monitoring
kubectl apply -f prometheus.yaml
kubectl apply -f grafana-dashboards/cortensor-dashboard.json


Access Prometheus and Grafana via their service IPs. Import cortensor-dashboard.json into Grafana.

🛠 Development

Local run:

cd app
uvicorn main:app --reload


Test API:

curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"data": [1,2,3]}'

📌 Notes

Replace <your-dockerhub-username> with your Docker Hub username.

Update Terraform provider configs (main.tf) for AWS/GCP/Azure as per your environment.

grafana-dashboards/cortensor-dashboard.json can be customized for metrics.
