import json
import random
from datetime import datetime, timedelta
import os

def generate_enhanced_data_engineering_dataset():
    """Generate a 2000-record dataset with 400 records per category"""
    
    # Configuration
    total_records = 2000
    records_per_category = 400
    
    # Services, regions, devices for variety
    services = [
        "Netflix", "Amazon Prime Video", "Disney+", "Apple Music", "Spotify",
        "Hulu", "HBO Max", "YouTube Premium", "Paramount+", "Peacock",
        "Crunchyroll", "Twitch", "ESPN+", "Apple TV+", "Discovery+"
    ]
    
    regions = ["US", "CA", "UK", "AU", "IN", "DE", "FR", "JP", "BR", "MX", "SG", "KR", "CN", "IT", "ES"]
    devices = ["Mobile", "Laptop", "Smart TV", "Game Console", "Tablet", "Desktop"]
    plans = ["Basic", "Family", "Premium", "Student", "Annual"]
    
    dataset = []
    
    # 1. Generate EXTRACTION records (400)
    print("Generating extraction records...")
    for i in range(records_per_category):
        customer_id = f"CUST-{10000 + i}"
        service = random.choice(services)
        plan = random.choice(plans)
        price = round(random.uniform(4.99, 29.99), 2)
        device = random.choice(devices)
        region = random.choice(regions)
        usage_hours = round(random.uniform(0.5, 12.0), 2)
        
        # Generate random date in 2024
        year = 2024
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        
        event_timestamp = f"{year:04d}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}"
        
        record = {
            "task_type": "extraction",
            "input": f"Extract subscription usage details:\nCustomer {10000 + i} used {service} on {device} under the {plan} plan costing ${price:.2f} in region {region}.",
            "output": {
                "customer_id": customer_id,
                "service_name": service,
                "subscription_plan": plan,
                "monthly_price_usd": price,
                "device_type": device,
                "region": region,
                "usage_hours": usage_hours,
                "event_timestamp": event_timestamp
            }
        }
        dataset.append(record)
    
    # 2. Generate SCHEMA_INFERENCE records (400)
    print("Generating schema inference records...")
    for i in range(records_per_category):
        service = random.choice(services)
        
        # Random schema complexity
        table_count = random.choice([2, 3, 4])
        tables = []
        
        # Always include customers table
        tables.append({
            "table_name": "customers",
            "columns": [
                {"name": "customer_id", "type": "VARCHAR(20)", "primary_key": True, "nullable": False},
                {"name": "email", "type": "VARCHAR(255)", "nullable": False},
                {"name": "signup_date", "type": "DATE", "nullable": False},
                {"name": "country", "type": "VARCHAR(2)", "nullable": False},
                {"name": "preferred_device", "type": "VARCHAR(50)", "nullable": True}
            ],
            "indexes": ["customer_id", "email", "signup_date", "country"]
        })
        
        # Subscriptions table
        tables.append({
            "table_name": "subscriptions",
            "columns": [
                {"name": "subscription_id", "type": "VARCHAR(30)", "primary_key": True, "nullable": False},
                {"name": "customer_id", "type": "VARCHAR(20)", "nullable": False, "foreign_key": "customers.customer_id"},
                {"name": "service_name", "type": "VARCHAR(100)", "nullable": False},
                {"name": "subscription_plan", "type": "VARCHAR(50)", "nullable": False},
                {"name": "monthly_price_usd", "type": "DECIMAL(10,2)", "nullable": False},
                {"name": "start_date", "type": "DATE", "nullable": False},
                {"name": "end_date", "type": "DATE", "nullable": True},
                {"name": "is_active", "type": "BOOLEAN", "nullable": False, "default": "true"}
            ],
            "indexes": ["subscription_id", "customer_id", "service_name", "is_active", "start_date"]
        })
        
        # Optional tables based on complexity
        if table_count >= 3:
            tables.append({
                "table_name": "usage_metrics",
                "columns": [
                    {"name": "usage_id", "type": "BIGINT", "primary_key": True, "nullable": False, "auto_increment": True},
                    {"name": "subscription_id", "type": "VARCHAR(30)", "nullable": False, "foreign_key": "subscriptions.subscription_id"},
                    {"name": "event_timestamp", "type": "TIMESTAMP", "nullable": False},
                    {"name": "usage_hours", "type": "DECIMAL(5,2)", "nullable": False},
                    {"name": "device_type", "type": "VARCHAR(50)", "nullable": False}
                ],
                "indexes": ["usage_id", "subscription_id", "event_timestamp"]
            })
        
        if table_count >= 4:
            tables.append({
                "table_name": "service_catalog",
                "columns": [
                    {"name": "service_id", "type": "INT", "primary_key": True, "nullable": False},
                    {"name": "service_name", "type": "VARCHAR(100)", "nullable": False},
                    {"name": "category", "type": "VARCHAR(50)", "nullable": False},
                    {"name": "supported_regions", "type": "JSON", "nullable": True},
                    {"name": "device_support", "type": "JSON", "nullable": True}
                ],
                "indexes": ["service_id", "service_name"]
            })
        
        record = {
            "task_type": "schema_inference",
            "input": f"Design a database schema for tracking {service} subscription usage. Include customer details, subscription info, and usage metrics.",
            "output": {
                "tables": tables,
                "relationships": [
                    "customers.customer_id → subscriptions.customer_id",
                    "subscriptions.subscription_id → usage_metrics.subscription_id"
                ] if table_count >= 3 else ["customers.customer_id → subscriptions.customer_id"]
            }
        }
        dataset.append(record)
    
    # 3. Generate DATA_QUALITY records (400)
    print("Generating data quality records...")
    for i in range(records_per_category):
        # Different quality rule sets
        rule_sets = [
            "basic_validations",
            "business_rules",
            "cross_field_validation",
            "temporal_consistency"
        ]
        
        rule_set = rule_sets[i % len(rule_sets)]
        
        # Create service list string for SQL
        service_list = ", ".join([f"'{s}'" for s in services[:5]])
        
        if rule_set == "basic_validations":
            quality_rules = [
                {
                    "rule_id": "DQ001",
                    "rule_name": "customer_id_not_null",
                    "rule": "customer_id IS NOT NULL",
                    "severity": "critical",
                    "description": "Customer ID must be present"
                },
                {
                    "rule_id": "DQ002",
                    "rule_name": "service_name_valid",
                    "rule": f"service_name IN ({service_list})",
                    "severity": "critical",
                    "description": "Service name must be from approved list"
                }
            ]
        elif rule_set == "business_rules":
            quality_rules = [
                {
                    "rule_id": "DQ101",
                    "rule_name": "price_plan_consistency",
                    "rule": "CASE WHEN subscription_plan = 'Basic' THEN monthly_price_usd <= 9.99 WHEN subscription_plan = 'Family' THEN monthly_price_usd <= 19.99 WHEN subscription_plan = 'Premium' THEN monthly_price_usd <= 29.99 ELSE true END",
                    "severity": "critical",
                    "description": "Price must be consistent with plan type"
                },
                {
                    "rule_id": "DQ102",
                    "rule_name": "usage_hours_range",
                    "rule": "usage_hours >= 0 AND usage_hours <= 24",
                    "severity": "warning",
                    "description": "Usage hours must be reasonable"
                }
            ]
        elif rule_set == "cross_field_validation":
            quality_rules = [
                {
                    "rule_id": "DQ201",
                    "rule_name": "device_region_compatibility",
                    "rule": "NOT (device_type = 'Game Console' AND region IN ('IN', 'BR')) OR service_name = 'Game Pass'",
                    "severity": "warning",
                    "description": "Device-region compatibility check"
                },
                {
                    "rule_id": "DQ202",
                    "rule_name": "subscription_duration",
                    "rule": "DATEDIFF(day, start_date, COALESCE(end_date, CURRENT_DATE)) >= 0",
                    "severity": "critical",
                    "description": "End date must be after start date"
                }
            ]
        else:  # temporal_consistency
            quality_rules = [
                {
                    "rule_id": "DQ301",
                    "rule_name": "event_timestamp_not_future",
                    "rule": "event_timestamp <= CURRENT_TIMESTAMP",
                    "severity": "critical",
                    "description": "Event timestamp cannot be in the future"
                },
                {
                    "rule_id": "DQ302",
                    "rule_name": "signup_before_usage",
                    "rule": "event_timestamp >= (SELECT signup_date FROM customers c WHERE c.customer_id = subscriptions.customer_id)",
                    "severity": "critical",
                    "description": "Usage must occur after signup"
                }
            ]
        
        record = {
            "task_type": "data_quality",
            "input": "Generate data quality rules for subscription data with fields: customer_id, service_name, subscription_plan, monthly_price_usd, device_type, region, usage_hours, event_timestamp",
            "output": {
                "table_name": "subscriptions",
                "quality_rules": quality_rules
            }
        }
        dataset.append(record)
    
    # 4. Generate ETL_PIPELINE records (400)
    print("Generating ETL pipeline records...")
    for i in range(records_per_category):
        service = random.choice(services)
        
        # Different pipeline types
        pipeline_types = ["daily_batch", "real_time_streaming", "weekly_aggregation", "data_migration"]
        pipeline_type = pipeline_types[i % len(pipeline_types)]
        
        if pipeline_type == "daily_batch":
            pipeline = {
                "pipeline_name": f"daily_{service.lower().replace(' ', '_')}_etl",
                "description": f"Daily ETL pipeline for {service} subscription data",
                "frequency": "daily",
                "schedule": "00:30 UTC",
                "source": "CSV files in S3",
                "destination": "Snowflake data warehouse",
                "transformations": ["data validation", "type conversion", "enrichment"]
            }
        elif pipeline_type == "real_time_streaming":
            pipeline = {
                "pipeline_name": f"realtime_{service.lower().replace(' ', '_')}_stream",
                "description": f"Real-time streaming pipeline for {service} events",
                "frequency": "continuous",
                "schedule": "24/7 streaming",
                "source": "Kafka topics",
                "destination": "AWS Redshift",
                "transformations": ["stream processing", "windowing", "aggregation"]
            }
        elif pipeline_type == "weekly_aggregation":
            pipeline = {
                "pipeline_name": f"weekly_{service.lower().replace(' ', '_')}_agg",
                "description": f"Weekly aggregation pipeline for {service} metrics",
                "frequency": "weekly",
                "schedule": "Sunday 02:00 UTC",
                "source": "data warehouse",
                "destination": "aggregation tables",
                "transformations": ["rollup aggregation", "metric calculation", "trend analysis"]
            }
        else:  # data_migration
            pipeline = {
                "pipeline_name": f"migrate_{service.lower().replace(' ', '_')}_legacy",
                "description": f"Migration pipeline for legacy {service} data",
                "frequency": "one_time",
                "schedule": "adhoc",
                "source": "legacy database",
                "destination": "modern data platform",
                "transformations": ["schema mapping", "data cleansing", "consistency checks"]
            }
        
        record = {
            "task_type": "etl_pipeline",
            "input": f"Design an ETL pipeline to process {service} subscription data for analytics.",
            "output": pipeline
        }
        dataset.append(record)
    
    # 5. Generate SQL_OPTIMIZATION records (400)
    print("Generating SQL optimization records...")
    for i in range(records_per_category):
        # Different query patterns to optimize
        query_patterns = [
            "date_filter",
            "aggregation",
            "join_optimization",
            "subquery_optimization"
        ]
        
        pattern = query_patterns[i % len(query_patterns)]
        
        if pattern == "date_filter":
            original = "SELECT * FROM subscriptions WHERE DATE(event_timestamp) = '2024-06-15' AND region = 'AU'"
            optimized = "SELECT * FROM subscriptions WHERE event_timestamp >= '2024-06-15' AND event_timestamp < '2024-06-16' AND region = 'AU'"
            optimizations = ["Replace DATE() function with range comparison", "Add index on (region, event_timestamp)"]
        
        elif pattern == "aggregation":
            original = "SELECT service_name, COUNT(*) as total_subscriptions FROM subscriptions GROUP BY service_name ORDER BY total_subscriptions DESC"
            optimized = "SELECT service_name, COUNT(*) as total_subscriptions FROM subscriptions WHERE event_timestamp >= '2024-01-01' GROUP BY service_name ORDER BY total_subscriptions DESC"
            optimizations = ["Add WHERE clause to reduce data", "Use materialized view for frequent aggregations"]
        
        elif pattern == "join_optimization":
            original = "SELECT c.*, s.service_name FROM customers c JOIN subscriptions s ON c.customer_id = s.customer_id WHERE s.region = 'US'"
            optimized = "SELECT c.*, s.service_name FROM subscriptions s JOIN customers c ON s.customer_id = c.customer_id WHERE s.region = 'US'"
            optimizations = ["Reorder join to start with smaller table", "Add index on subscriptions.customer_id"]
        
        else:  # subquery_optimization
            original = "SELECT * FROM customers WHERE customer_id IN (SELECT customer_id FROM subscriptions WHERE monthly_price_usd > 20)"
            optimized = "SELECT c.* FROM customers c JOIN subscriptions s ON c.customer_id = s.customer_id WHERE s.monthly_price_usd > 20"
            optimizations = ["Replace IN subquery with JOIN", "Add index on subscriptions.monthly_price_usd"]
        
        record = {
            "task_type": "sql_optimization",
            "input": f"Optimize this SQL query: {original}",
            "output": {
                "original_query": original,
                "optimized_query": optimized,
                "optimizations": optimizations,
                "expected_improvement": f"{random.randint(3, 15)}x faster execution"
            }
        }
        dataset.append(record)
    
    # Shuffle the dataset to mix categories
    random.shuffle(dataset)
    
    return dataset

def save_dataset(dataset, filename="enhanced_data_engineering_dataset.json"):
    """Save dataset to JSON file"""
    
    # Get current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, filename)
    
    # Save to JSON
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
    
    # Calculate statistics
    category_counts = {}
    for record in dataset:
        task_type = record["task_type"]
        category_counts[task_type] = category_counts.get(task_type, 0) + 1
    
    return filepath, category_counts

def main():
    """Main function to generate and save the dataset"""
    
    print("=" * 60)
    print("Generating Enhanced Data Engineering Dataset")
    print("=" * 60)
    
    # Generate dataset
    dataset = generate_enhanced_data_engineering_dataset()
    
    # Save dataset
    filename = "enhanced_data_engineering_dataset.json"
    filepath, category_counts = save_dataset(dataset, filename)
    
    # Print summary
    print("\n" + "=" * 60)
    print("Dataset Generation Complete!")
    print("=" * 60)
    print(f"\nFile saved to: {filepath}")
    print(f"Total records: {len(dataset)}")
    print(f"File size: {os.path.getsize(filepath) / 1024 / 1024:.2f} MB")
    
    print("\nCategory Distribution:")
    for category, count in sorted(category_counts.items()):
        percentage = (count / len(dataset)) * 100
        print(f"  {category:20} {count:4} records ({percentage:.1f}%)")
    
    # Display first record of each category
    print("\nSample Records (first of each category):")
    seen_categories = set()
    for record in dataset:
        if record["task_type"] not in seen_categories:
            seen_categories.add(record["task_type"])
            print(f"\n{record['task_type'].upper()}:")
            print(f"  Input: {record['input'][:80]}...")
            print(f"  Output keys: {list(record['output'].keys())}")
        
        if len(seen_categories) == 5:
            break
    
    print("\n" + "=" * 60)
    print("Dataset is ready for use with your training code!")
    print("=" * 60)

if __name__ == "__main__":
    main()