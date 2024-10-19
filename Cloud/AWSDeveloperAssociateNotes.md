# AWS Developer Associate Notes

By Fasal Kahn, hosted through Stormwind Studios
Enrolled in Summer 2024

## Running Questions

* SQS
* Difference between Data Centers and availability zone

## 1. Introduction to Developing in Azure

### Getting Started with AWS

* History:
  * 2002 founded. 2007 expanded massively
  * 2019: AWS had 35+million in revenue
  * Low barrier of entry for Cloud compared to its competitors
* Pros: Highly customizable, highly secure, helps save money on infrastructure for businesses
* Terms:
  * AWS Regions (North america, asia)
    * Deployed all over the world
    * Names = us-east-1, eu-west-3
    * How to Choose an AWS Region
      * Compliance: Some countries have gov regulations for spinning up servers. Some regions are cheaper than others (North Virginia is cheapest, but perhaps at cost of stability due to traffic)
      * Proximity
      * Available services in a region
      * Pricing
  * Availability Zone
    * Each region has many availability zones (min 2, max 6, usually 3)
    * Each AZ is a discrete data center (locations not advertised)
  * Data Centers
    * There will be at least 2 redundant data centers for each availability zone
  * Edge Locations
    * Amazon provides a copy of websites into a servers across regions, and users will be served through edge locations. Increases throughput for a site until changes are around
    * Points of Presence
      * 216 total in 84 cities across 42 countries
    * Global Services available (IAM, Route 53, WAF).
    * Most Services are Region Scoped
  * Caching

### Exploring IAM

IAM = Identity Access Management

* Important for security, compliance, etc
* Roles in IAM
  * Root Account = master account
  * Users = people that can be grouped by team, role, etc. User can belong to multiple groups
  * Groups = contain other users (dont contatin other groups)
* Permissions
  * Governed by JSON
  * Applies Least Privilege Principle(only applies what the user needs)
  * Create Permissions with Effect, Actions, and Resources
  * Policies can be Inherited across groups
* IAM Policies Structure
  * Statements have : sid, effect(allow, deny), principal(call out specific account), action, resource
* Password Policy
  * Stregth, allowing people to change their passwords, etc
  * Multi Factor Auth
    * Support for AWS is either USB Key, Phone app, etc
* How user can access AWS:
  * Access Keys are mandatory; they are secret like a password too
  1. AWS Management Console/Web Browser page: password + MFA
  2. Command Line CLI: protected by access key
  3. AWS Coftware Developer Kit: protected by access key
* Demo
  * Create Roles
  * Setting up MFA (Multi factor identification)
  * Add new groups
  * Apply roles to users

## 2. EC2

### EC2 Basics

EC2

* Every AWS account has at least 1 EC2 instance running before they scale out more
* Elastic Compute Cloud
* Iaas = Infrastructure as a service (dont need hw, just create a VM)
* Most popular offering from AWS
* Capabilities
  * Renting virtual machines (EC2)
  * Storing data on virtual drives (EBS)
  * Load balancing (ELB)
  * Scaling services using an auto-scaling group (ASG)
* Sizing and Configurations (all different costs)
  * Can configure CPUs(compute power and cores), Random Access memory (RAM), Storage Space (Network attached(EBS and EFS) and hardware(EC2 instance store))
  * Network card, speed of card, public IP Address
  * Firewall rules: security group (host based firewall, only allow a certain type of traffic)
  * Bootstrap script(configure at startup), EC2 user data
* EC2 User Data
  * Possible to bootstrap our instances using an EC2 User data script
  * Bootstrapping = launching commands when a machine starts
    * Only run once at instance's first start
    * Automates boot tasks like: installing updates, install sw, download common files from internet, anything else
    * Runs with Root
  * Demo
    * Can select an OS based on AMI ID
    * Can select architecture available
    * Generate Key Pair
    * VPC = Virtual private cloud, can create your own or do default
      * Specify Subnet
      * Automatic IP address
      * Set security groups
      * Add other ports
    * Add other network cards
    * Storage configuration
    * Active Directory
    * User Data Script (example sets up users)

EC2 Instance Types: https://aws.amazon.com/ec2/instance-types/ 

* Overview
  * Type of physical server you are renting from AWS
  * There are different instances optimized for different use cases
    * General purpose (m, t)
      * Balances between compute, memory, and networking
      * Example = t2.micro, part of free tier
    * Compute Optimized (c)
      * CPU utilization
      * Scientific modeling
      * Batch processing
      * Mediatranscoding
      * Gaming Servers
    * Memory Optimized (r)
      * Fast performance for workloads with large data sets in memory
    * Accelerated Computing (p)
    * Storage Optimized (l)
      * Great for storage use
    * HPC Optimized (hpc)
  * AWS naming convention
    * m5.2xlarge = m instance class, 5 generation, 2xlarge size within instance class
* Security Group
  * They control how traffic is allowed in or out of EC2 instances
  * Only contain "allow rules". No deny rules, since everything is denied
  * Security groups can reference by IP or by security group
  * Like a firewall
  * Every security group is specific to a region. It is locked down to a region/VPC combination
  * It's good to maintain one separate security group for SSH access
  * All inbound traffic is blocked by default, all outbound traffic is authorized by default
  * Security groups can be nested
* Common ports
  * 22 SSH
  * 21 FTP
  * 22 SFTP
  * 80 HTTP
  * 3389 Remote Desktop Protocol
* Linux/Mac Example
* Payments:
  * On-Demand, or reserved, or spot instances, or dedicated hosts
  * Dedicated Hosts and server
  * Physical services available
  * Some companies will ramp up resources over the holiday season
* Demo - Purchasing a reserve

### EC2 Instance Storage Section

## 3. Load Balancing, Auto Scaling Groups, and EBS Volumes

### High availability and Scalability

### Load Balancing

### Auto Scaling Groups

## 4. RDS, Aurora, and Elasticache

### Relational Database Service

### Aurora

### Elasticache

## 5. DNS and VPCs

## 6. Tier 3 Architecture

## 7. Amazon Simple Storage Service

## 8. AWS Development

## 9. Cloudfront, Beanstalk, and Docker Development

## 10. CICD

## 11. Managing your Infrastructure ad Code

## 12. AWS Monitoring, Troubleshooting, and Audit

## 13. AWS Integration and Messaging

## 14. Lambda and DynamoDB

## 15. API Gateway

## 16. Working with Serverless Application Model (SAM)

## 17. Additional Security

## 18. Additional AWS Services