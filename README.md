# Enterprise Data Engineering LLM: Fine-tuning for Traceability & Analytics with Consumer GPU
### Revolutionizing Enterprise AI with Accessible Hardware

## Project Overview
##### Enterprise Data Engineering LLM is a cutting-edge project that demonstrates how to fine-tune large language models (specifically Google's Gemma 2B) for enterprise data engineering tasks using consumer-grade hardware (RTX 4070). The project focuses on creating a specialized LLM capable of handling complex data engineering workflows including:

- Structured Data Extraction - Converting natural language descriptions into structured JSON

- Schema Inference - Automatically designing database schemas from data descriptions

- Data Quality Rules - Generating validation rules for enterprise data

- ETL Pipeline Design - Creating data pipeline architectures

- SQL Optimization - Improving database query performance

### Key Innovation: Consumer GPU for Enterprise AI
##### <ins>Hardware</ins>: NVIDIA RTX 4070 (Consumer GPU)
##### This project also demonstrates a significant cost breakthrough - using a consumer-grade RTX 4070 GPU (8GB VRAM) instead of expensive enterprise-grade hardware to fine-tune LLMs for enterprise applications.

---


### Project Highlights: Traditional vs Low-Cost LLM Fine-Tuning 

| Development Aspect | Traditional Enterprise Approach | Our Efficient Solution | Competitive Advantage |
|-------------------|---------------------------------|------------------------|----------------------|
| **Hardware Investment** | • A100/H100 GPUs<br>• $10,000+ per unit<br>• Enterprise licensing | • RTX 4070/4080<br>• $600-$1500 per unit<br>• Consumer hardware | **94% lower cost**<br>Accessible to small teams & startups |
| **Deployment Timeline** | • Days waiting for cloud resources<br>• Security/compliance reviews<br>• Infrastructure provisioning | • Hours to deploy locally<br>• Immediate resource access<br>• Simplified security model | **10x faster deployment**<br>Quick response to business needs |
| **Data Privacy & Security** | • Data stored with cloud providers<br>• Shared infrastructure<br>• Compliance challenges | • Full on-premises control<br>• No third-party data access<br>• Simplified compliance | **Zero data sovereignty risk**<br>Ideal for sensitive applications |
| **Training Efficiency** | • 8+ hours per training run<br>• Limited parallel experiments<br>• High cloud compute costs | • <2 hours with optimizations<br>• Multiple parallel runs<br>• Minimal electricity cost | **4x faster iterations**<br>More experiments, better models |
| **Development Velocity** | • Budget-limited cloud credits<br>• Queue-based resource access<br>• Slow feedback cycles | • Unlimited local experimentation<br>• Immediate result feedback<br>• Continuous optimization | **Rapid prototyping capability**<br>Faster time-to-market |

#### Key Technology Innovations
1. **Parameter-Efficient Fine-Tuning (PEFT)** - Reduces training requirements
2. **4-bit/8-bit Quantization** - Enables consumer GPU usage
3. **Local AI Toolchains** - Eliminates cloud dependency
4. **Open-Source Optimization** - Removes licensing costs
5. **Simplified MLOps** - Reduces operational complexity

#### Business Impact Summary
- **Cost Efficiency:** 94% reduction in hardware costs
- **Speed to Market:** 10x faster deployment cycles
- **Data Sovereignty:** Complete privacy and control
- **Development Agility:** 4x more experimental iterations
- **Accessibility:** Democratizes AI for all organization sizes

## Project's Enterprise Benefits
#### 1. Automated Data Engineering Workflows
- 10x faster data pipeline design from requirements to implementation

- Automated schema generation reducing manual design time by 80%

- Intelligent data quality rules that adapt to your data patterns

#### 2. Traceability & Compliance
- End-to-end data lineage tracking for regulatory compliance (GDPR, HIPAA, SOX)

- Automated audit trail generation from natural language descriptions

- Real-time data quality monitoring with AI-generated validation rules

#### 3. Scalable Data Operations
- One model, multiple use cases: Single LLM handles extraction, quality, pipelines, optimization

- Adaptable to any industry: Subscription data used as example; easily transferable

- Reduced SME dependency: Less reliance on specialized data engineers for routine tasks

#### 4. Cost-Effective AI Integration
- No expensive AI specialists required: Standard data engineers can maintain

- Minimal infrastructure overhead: Runs on existing consumer hardware

- Predictable costs: No surprise cloud GPU bills, one-time hardware investment
---

## Getting Started

#### Prerequisites
- NVIDIA GPU with 8GB+ VRAM (RTX 4070 recommended)

- Python 3.10+

- 16GB System RAM

- 20GB Free Disk Space

```python
# 1. Clone the repository
git clone https://github.com/manuelbomi/Enterprise-Data-Engineering-LLM-Fine-tuning-LLMs-for-Traceability-Analytics-with-Consumer-GPU.git
cd enterprise-data-engineering-llm

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Generate training data (optional)
python generate_dataset.py  #you can also decid eto leave the code as it is since it will use the enhanced_data_engineering_dataset.json (2000 records) by default

# 5. Run LLM fine-tuning and testing code
python fine_tune_LLM_Data_Engineering.ipynb

```

## Results

The project is desinged to use the GPU  that is on the Dev's project environment to fine-tune the LLM. The GPU is RTX 4070 on Omen HP computer in our case. You may first need to install the relevant CUDA toolkit if the code (in cell 1 of fine_tune_LLM_Data_Engineering.ipynb) deos not naturally detect your GPU. The project uses the *unsloth* library (*from unsloth import FastLanguageModel*) to import an LLM (*gemma-2b-bnb-4bit* in our case), and then fine-tune the LLM using tokenized data and *LoRA* (*Low Rank Adaptation*) to enable the LLM to accomplish some specific enterprise task(s). 

The tasks in our case are data engineering specific, and they include: 

- schema inference
- data quality assessment
- etl pipeline design
- sql optimization
- data extration.

Some snippets of the tasks and the results generated by the LLM after fine-tunning are shown below:





#### Training Data Categories Generated:

<img width="1769" height="627" alt="Image" src="https://github.com/user-attachments/assets/3450855e-59e7-4ecc-be11-ab108ee7aaea" />

#### 1. Data Extraction 
##### <ins>Data Structure </ins>

```python
  {
    "task_type": "extraction",
    "input": "Extract subscription usage details:\nCustomer 10000 used Apple Music on Mobile under the Family plan costing $6.39 in region AU.",
    "output": {
      "customer_id": "CUST-10000",
      "service_name": "Apple Music",
      "subscription_plan": "Family",
      "monthly_price_usd": 6.39,
      "device_type": "Mobile",
      "region": "AU",
      "usage_hours": 4.57,
      "event_timestamp": "2024-06-15T00:00:00"
    }
  },
```
#### <ins> Test Result </ins>
```python
Test 1: Data Extraction
 Input: Extract subscription usage details:
Customer 10001 used Apple Music on Game Cons...

 Response:
----------------------------------------
user
Extract structured JSON data from the given text.

Extract subscription usage details:
Customer 10001 used Apple Music on Game Console under the Basic plan costing $16.23 in region AU.
model
{
  "customer_id": "CUST-10001",
  "service_name": "Apple Music",
  "subscription_plan": "Basic",
  "monthly_price_usd": 16.23,
  "device_type": "Game Console",
  "region": "AU",
  "usage_hours": 5.98,
  "event_timestamp": "2024-07-16T10:08:33"
...
    "A
... (truncated)

```


<img width="1267" height="783" alt="Image" src="https://github.com/user-attachments/assets/d916dabb-46bf-4065-bdea-dce9421a4c7b" />

---


##### Focuses on subscription data with consistent JSON schema

#### 2. Schema Inference
##### <ins>Data Structure </ins>

- Database schema design for subscription tracking systems

- Normalized schemas (customers, subscriptions, services, usage)

- Data type recommendations and indexing strategies

```python
  {
    "task_type": "schema_inference",
    "input": "Design a database schema for tracking Disney+ subscription usage. Include customer details, subscription info, and usage metrics.",
    "output": {
      "tables": [
        {
          "table_name": "customers",
          "columns": [
            {"name": "customer_id", "type": "VARCHAR(20)", "primary_key": true, "nullable": false},
            {"name": "email", "type": "VARCHAR(255)", "nullable": false},
            {"name": "signup_date", "type": "DATE", "nullable": false},
            {"name": "country", "type": "VARCHAR(2)", "nullable": false}
          ],
          "indexes": ["customer_id", "email"]
        }
      ]
    }
  }

```

#### <ins> Test Result </ins>

<img width="1790" height="677" alt="Image" src="https://github.com/user-attachments/assets/51c93bcc-3a1c-46ae-9eeb-3c8a2dd3675c" />

---

#### 3. Data Quality Rules 
- Validation rules for subscription data

- Business logic constraints (price ranges, plan types)

- Cross-field validation and temporal consistency

##### <ins>Data Structure </ins>
```python
  {
    "task_type": "data_quality",
    "input": "Generate data quality rules for subscription data with fields: customer_id, service_name, subscription_plan, monthly_price_usd, device_type, region, usage_hours, event_timestamp",
    "output": {
      "table_name": "subscriptions",
      "quality_rules": [
        {
          "rule_id": "DQ001",
          "rule_name": "customer_id_not_null",
          "rule": "customer_id IS NOT NULL",
          "severity": "critical",
          "description": "Customer ID must be present"
        }
      ]
    }
  }
```

#### <ins> Test Result </ins>

<img width="1663" height="659" alt="Image" src="https://github.com/user-attachments/assets/d6e0aaeb-4b9c-4da6-915f-0a65fee51100" />

---

#### 4. ETL Pipeline Design
- Daily/weekly batch processing pipelines

- Real-time streaming ingestion

- Error handling and monitoring

##### <ins>Data Structure </ins>

```python
  {
    "task_type": "etl_pipeline",
    "input": "Design an ETL pipeline to process daily Netflix subscription data from CSV files to a data warehouse for analytics.",
    "output": {
      "pipeline_name": "daily_netflix_etl",
      "source": {
        "type": "s3_csv",
        "location": "s3://subscription-data/netflix/daily/",
        "pattern": "netflix_*.csv"
      },
      "transformations": [
        "Validate required columns",
        "Convert event_timestamp to ISO 8601"
      ],
      "destination": {
        "type": "snowflake",
        "table": "subscription_fact"
      }
    }
  }

```

#### <ins> Test Result </ins>

<img width="1442" height="666" alt="Image" src="https://github.com/user-attachments/assets/5c90a8cc-8418-4d57-94f4-15a717a04154" />


---

#### 5. SQL Optimization 
- Query optimization for subscription analytics

- Indexing recommendations

- Performance tuning for common patterns

##### <ins>Data Structure </ins>

```python
  {
    "task_type": "sql_optimization",
    "input": "Optimize this SQL query: SELECT * FROM subscriptions WHERE DATE(event_timestamp) = '2024-06-15' AND region = 'AU'",
    "output": {
      "original_query": "SELECT * FROM subscriptions WHERE DATE(event_timestamp) = '2024-06-15' AND region = 'AU'",
      "optimized_query": "SELECT * FROM subscriptions WHERE event_timestamp >= '2024-06-15' AND event_timestamp < '2024-06-16' AND region = 'AU'",
      "optimizations": [
        "Replace DATE() function with range comparison",
        "Add index on (region, event_timestamp)",
        "Use partitioned table by event_date column"
      ]
    }
  }

```

#### <ins> Test Result </ins>

<img width="1657" height="557" alt="Image" src="https://github.com/user-attachments/assets/98750b53-47d7-4588-bd47-4135c806feac" />

---

## Customizing the Project for Your Enterprise

#### 1. Adapting to Your Data

```python
# Modify the data generation script for your industry
def generate_your_industry_data():
    return [
        {
            "task_type": "extraction",
            "input": "Your specific data description...",
            "output": {"your_field": "your_value"}  # Your schema
        }
    ]
```

#### 2. Adding New Task Types

```python
# Extend the system prompts for your use cases
system_prompts = {
    "your_task": "Your custom instruction...",
    # ... existing tasks
}

# Add to training data generation
if task_type == "your_task":
    assistant_response = generate_your_task_output()
```

#### 3. Industry-Specific Tuning
- Financial: Add transaction types, regulatory fields

- Healthcare: Include medical codes, patient identifiers

- Retail: Add product SKUs, customer segments

- Manufacturing: Include part numbers, quality metrics


## Contributing
##### We welcome contributions! Areas of particular interest:

- Additional enterprise use cases

- Performance optimizations for other GPUs

- Integration with data platforms (Snowflake, Databricks, etc.)

- Multi-language support for global enterprises

##  License
MIT License 

## Summary 
#### Why This Project Matters
This project democratizes enterprise AI by proving that sophisticated data engineering automation doesn't require massive infrastructure investments. Organizations can now implement AI-powered data pipelines, quality controls, and analytics automation using hardware they already own or can affordably acquire, significantly lowering the barrier to AI adoption while maintaining enterprise-grade capabilities.

#### The Future It Enables
A world where every data engineering team has access to AI assistance, where cost is no longer the primary barrier to intelligent automation, and where organizations can iterate rapidly on AI solutions without budget approvals for expensive cloud resources or specialized hardware.

#### Core Innovation
The project demonstrates how to fine-tune Large Language Models (Gemma 2B) for enterprise data engineering tasks using consumer-grade NVIDIA RTX 4070 GPUs, achieving enterprise-grade AI capabilities at 94% lower cost than traditional enterprise hardware solutions.

#### Problem Solved
Enterprise AI traditionally requires expensive infrastructure ($10,000+ GPUs, cloud subscriptions) that creates barriers to adoption. This project breaks those barriers by showing how consumer hardware (RTX 4070, ~$600) can deliver comparable results for specialized data engineering applications.

#### Key Capabilities
The fine-tuned LLM handles five critical data engineering tasks:

- Structured Data Extraction - Convert natural language to JSON

- Schema Inference - Design database schemas from descriptions

- Data Quality Rules - Generate validation rules automatically

- ETL Pipeline Design - Create optimized data pipelines

- SQL Optimization - Improve query performance

#### Technical Achievement
- Training Time: 2 hours for 2000 examples (vs. 6+ hours on cloud)

- Model Size: Gemma 2B with 4-bit quantization

- Memory Usage: <8GB VRAM throughout training

- Fine-tuning: LoRA adapters (only 2.5% parameters trained)

- Cost/Model: ~$0.50 in electricity vs. $500+ on cloud

---

### Thank you for reading
---

### **AUTHOR'S BACKGROUND**
### Author's Name:  Emmanuel Oyekanlu
```
Skillset:   I have experience spanning several years in data science, developing scalable enterprise data pipelines,
enterprise solution architecture, architecting enterprise systems data and AI applications,
software and AI solution design and deployments, data engineering, high performance computing (GPU, CUDA), machine learning,
NLP, Agentic-AI and LLM applications as well as deploying scalable solutions (apps) on-prem and in the cloud.

I can be reached through: manuelbomi@yahoo.com

Website:  http://emmanueloyekanlu.com/
Publications:  https://scholar.google.com/citations?user=S-jTMfkAAAAJ&hl=en
LinkedIn:  https://www.linkedin.com/in/emmanuel-oyekanlu-6ba98616
Github:  https://github.com/manuelbomi

```
[![Icons](https://skillicons.dev/icons?i=aws,azure,gcp,scala,mongodb,redis,cassandra,kafka,anaconda,matlab,nodejs,django,py,c,anaconda,git,github,mysql,docker,kubernetes&theme=dark)](https://skillicons.dev)

