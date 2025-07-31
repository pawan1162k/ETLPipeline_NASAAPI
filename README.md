# README.md

# NASA APOD ETL Pipeline

A robust ETL (Extract, Transform, Load) pipeline built with Apache Airflow that fetches NASA's Astronomy Picture of the Day (APOD) data, processes it, and loads it into various data destinations.

## 🚀 Overview

This project demonstrates a production-ready ETL pipeline that:
- **Extracts** data from NASA's APOD API using HTTP requests
- **Transforms** the data for analytics and storage optimization
- **Loads** processed data into multiple destinations (PostgreSQL, AWS S3, Redshift, RDS)
- **Orchestrates** the entire workflow using Apache Airflow with Astro CLI

## 🏗️ Architecture

```
NASA APOD API → Airflow (Astro) → Data Transformation → Multiple Destinations
                    ↓
               PostgreSQL (Local)
               AWS S3 (Cloud)
               AWS Redshift (Cloud)
               AWS RDS (Cloud)
```

## 🛠️ Tech Stack

- **Orchestration**: Apache Airflow with Astro CLI
- **Data Source**: NASA APOD API
- **Local Database**: PostgreSQL (Docker)
- **Cloud Services**: AWS S3, Redshift, RDS
- **Containerization**: Docker & Docker Compose
- **Language**: Python 3.12

## 📋 Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Astro CLI
- AWS Account (for cloud destinations)
- NASA API Key ([Get one here](https://api.nasa.gov/))

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd nasa-apod-etl-pipeline
```

### 2. Install Astro CLI
```bash
# macOS
brew install astro

# Linux/Windows
curl -sSL install.astronomer.io | sudo bash -s
```

### 3. Initialize Astro Project
```bash
astro dev init
```

### 4. Set Up Environment Variables
Create a `.env` file:
```bash
NASA_API_KEY=your_nasa_api_key_here
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_DEFAULT_REGION=us-east-1
```

### 5. Start the Pipeline
```bash
# Start Airflow with Astro
astro dev start

# Access Airflow UI at http://localhost:8080
# Default credentials: admin/admin
```

### 6. Configure Connections
In Airflow UI, add these connections:

**NASA API Connection (`nasa_api`):**
- Connection Type: HTTP
- Host: `https://api.nasa.gov`
- Extra: `{"api_key": "your_nasa_api_key"}`

**PostgreSQL Connection (`postgres_default`):**
- Connection Type: Postgres
- Host: `postgres_db`
- Database: `postgres`
- Username: `postgres`
- Password: `postgres`

## 📊 Pipeline Features

### Current Implementation (Local)
- ✅ Extract data from NASA APOD API
- ✅ Transform and clean data
- ✅ Load into PostgreSQL database
- ✅ Error handling and retries
- ✅ Data validation

### Cloud Migration (In Progress)
- 🔄 AWS S3 integration for data lake storage
- 🔄 AWS Redshift for data warehousing
- 🔄 AWS RDS for managed database
- 🔄 Multi-destination data loading
- 🔄 Cloud-native error handling

## 🗃️ Data Schema

### APOD Data Table
```sql
CREATE TABLE apod_data (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    explanation TEXT,
    url TEXT,
    date DATE,
    media_type VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);
```

## 🔧 Project Structure

```
├── dags/                   # Airflow DAGs
│   ├── etl_pipeline.py    # Main ETL pipeline
│   └── utils/             # Helper functions
├── docker-compose.yml     # Local PostgreSQL setup
├── requirements.txt       # Python dependencies
├── Dockerfile            # Astro runtime image
├── .env.example          # Environment variables template
└── README.md             # This file
```

## 🚀 Deployment Options

### Local Development
```bash
astro dev start
```

### Astronomer Cloud
```bash
astro deploy
```

### AWS MWAA (Managed Airflow)
- Upload DAGs to S3 bucket
- Configure MWAA environment
- Set up IAM roles and permissions

## 📈 Monitoring & Observability

- **Airflow UI**: Task monitoring and logs
- **Database Metrics**: Connection monitoring
- **Error Alerting**: Email/Slack notifications
- **Data Quality**: Validation checks

## 🔒 Security Best Practices

- API keys stored in Airflow connections
- AWS credentials via IAM roles
- Database passwords encrypted
- Network isolation with Docker networks

## 🚧 Roadmap

### Phase 1: Local Implementation ✅
- [x] Basic ETL pipeline
- [x] PostgreSQL integration
- [x] Error handling

### Phase 2: Cloud Migration 🔄
- [ ] AWS S3 data lake integration
- [ ] Redshift data warehouse setup
- [ ] RDS managed database
- [ ] Multi-destination loading

### Phase 3: Advanced Features 📋
- [ ] Real-time streaming with Kinesis
- [ ] Data quality monitoring
- [ ] ML pipeline integration
- [ ] Advanced scheduling strategies

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📚 Resources

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Astro CLI Documentation](https://docs.astronomer.io/astro/cli/overview)
- [NASA APOD API](https://api.nasa.gov/)
- [AWS Data Pipeline Best Practices](https://aws.amazon.com/big-data/datalakes-and-analytics/)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Your Name** - your.email@example.com  
**Project Link**: https://github.com/yourusername/nasa-apod-etl-pipeline

---

⭐ **Star this repository if you found it helpful!**