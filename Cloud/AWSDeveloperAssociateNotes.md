# AWS Developer Associate Notes

By Fasal Kahn, hosted through Stormwind Studios
Enrolled in Summer 2024

## Running Notes

### Questions/Look Up Later

* SQS
* Difference between Data Centers and availability zone
* CCP in context of EBS
* IOPS as a unit of size
  * Input output per second
* SSD vs HDD
* Layers (Layer 3 = network, TCP = Layer 4, HTTP=Layer 7)
* Connection Draining vs Deregistration Delay
* Replication vs Sharding
* Deep Dive into DNS
* CNAME vs Alias
* NSlookup.io
* VPC: Subnets, internet gateways, NAT gateways, security groups, network ACL, vpc flow logs, VPC Peering, VPC endpoints, site to site vpn
* Routing Table

### Practice Ideas

* Label FQDN:  Protocol, domain name, sub domain, SLD, TLD, root
* Route 53 Lab
* S3 Encryption methods


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

EC2 = Elastic Compute Cloud V2

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

### EC2 Instance Storage Section [67]

EBS Volume = Elastic Block Storage Volume

* General
  * EBS = a network drive you can attach to instances while they run
  * Allows instances to persist data even after termination
  * Mounted to one instance at a time (at the CCP level)
  * Bound on specific availability zone
* Summary
  * It's a network drive
    * Can switch between EC2 instances quickly
  * It's locked to an availability Zone
  * Has a provisioned capacity (size in GBs, IOPS input output per second)
* Delete on Termination Attribute
* EBS Snapshots
  * Makes a backup of EBS volume
  * Can copy across AZ or region

AMI = Amazon Machine Image, OS-like

* AMI = Customization of EC2 instance
* AMI Process
  1. Start EC2 instance
  2. Customize it
  3. Stop the instance
  4. Build AMI, which creates EBS snapshots
  5. Launch instances from other AMIs

EC2 Instance Store

* High performance EBS = EC2 Instance Store
* They lose their instance when stopped (ephemeral)
* Backups are your responsibility

EBS Volume Types

* Six types (HDD = Hard Disk Drives)
  * gp2/gp3 SSD: balances price and performance for wide workloads
  * io1/io2 SSD: High performance for mission critical, low latency, high throughput workloads
  * st1 HDD: Low cost for frequent access workloads
    * Throughput optimized HDD
  * sc1 HDD: lowest cost, less frequent accessed workloads
    * Cold HDD
* Hard disc drives
* Only gpX and ioX are used as boot volumes
* EBS Multi Attatch
  * The ioX family only
  * Can attach one EBS to multiple EC2 instances

EFS = Elastic File System

* Details
  * Managed NFS that can be mounted on many EC2s
  * Works with many azs
  * Use Cases: Content Management, web serve, wordpress
  * USes NFSv4.1 protocol
  * Uses security group for access control
* EFS Performance and Storage Classes
  * EFS Scale
  * Performance Mode
  * Throughput mode
  * Storage Tiers (lifecycle management feature)
* EBS vs EFS
  * EBS = attached to one instance at a time, locked at one AZ level (but can migrate with a snapshot). 
    * Root EVS get terminated if EC2 instance is terminated if (can be controlled by Termination Attribute)
  * EFS = attaches to multiple EC2, mounts across AZs, Linux only

Takeaway: EFS vs EBS vs instance store

## 3. Load Balancing, Auto Scaling Groups, and EBS Volumes

### High availability and Scalability

* How an ap/system scales with higher loads
  * Vertical scale
    * Increase Size of instance
    * More expensive
  * Horizontal Scale/elasticity
    * add same size multiple instances
    * implies distributed system
* high availability
  * Run same instance across multiple azs
  * Goal = survive data center loss

### Load Balancing

Tactic with Horizontal Scaling

* FW traffic to multiple servers
* Seemlessly handles failure of single instances

ELB = Elastic load balancer

* Is a managed load balancer, guarantees working
* Health Check is crucial to load balancer
* Done on a port/route (/health)
* AWS's 4 types of LBs
  * Classic v1, 2009, (CLB)
    * Health Check = TCP or HTTP
  * Application Load Balancer v2, 2016, (ALB)
    * Only works on layer 7, HTTP based only
    * Needs a routing table
    * Different servers may specialize; site/user goes to one EC2 instance, site/setting goes to second
    * Practical Example = platform=Mobile goe to target group 1, platform=Desktop goes to On premises private IP routing
  * Network Load Balancer v2, 2017 (NLB)
    * Good for streaming, is layer 4 based (TCP UDP)
    * FW TCP and UDP to instances
    * Has one static IP per AZ
  * Gateway Load Balancer, 2020 (GLB)
    * Layer 3 (Network Layer), IP Packets
    * Use cases: firewall

Demo  

Sticky Session

* Configure so that same client is always redirected to same instance
* Works for ALB and CLB bc HTTP. Uses cookies
* Consequence: May unbalance your loads as a result
* Cookie Names
  * App based cookies
    1. Custom(generatd by target, specified per target group) or Application(generated by laod balancer, ex AWSALBAPP)
  * Duration based cookies (generated by LB, AWSALB for ALB, AWSELB for CLB)

Cross Zone Load Balancing

* With Cross Zone LB
  * Each LB instance distributes evenly across all registered instance in all LZs
  * Always on for ALB
* Without Cross Zone LB
  * Requests are disctibuted in the instances of the node of the ELB

SSL/TLS

* Certificates = allows encryption of traffic
* Public SSL certificates issued by Certificate Authority
* Client -> (HTTPS encrypted) to LB, it is resolved there before going to instances
* Server Name indications (SNI). Solve problem of loading multiple SSL certs into one web server
* ELBs support for certs
  * CLB = can only support one SSL cert
  * ALB can support multiple certs, uses SNI
  * NLB uses SNI to make it work too

Connection Draining(CLB) / Deregistration Delay(ALB and NLB)

* Fix when one server has unhealthy status

### Auto Scaling Groups

ASG = Auto Scaling Groups

* Goals
  * Scale out (add EC2 instances) to match increased load
  * Scale in (remove EC2 instances) to match decreased load
  * Ensure we have max and min number of machines running
  * Automatically register new instances to a load balancer
* Load balancer adds or removes automatically
* ASGs have following attributes
  * Launch configuration with AMI specifying EC2 user data, EBS volumes, security groups, ssh key pairs

Auto Scaling Alarm

* Scale an ASG based on CloudWatch Alarms
* Look out for a specific metric. Can set custom metrics
* Alarm trigger results in scale out or scale in
* Must give a Launch Template and Launch Configuration
* Can schedule scaling up too
* Predictive Scaling or Dynamic Scaling
* Cooldown period applied after a scaling event

## 4. RDS, Aurora, and Elasticache

### Relational Database Service

RDS = Relational Database service

* Uses SQL
* Managed, automated provisioning, monitoring dashboard
* Database Backup
  * AWS Backup automated
* Dynamic Scaling for RDS
  * Set Max
  * If 10% space left, then it can scale my default
* Read Replica
  * Read-Only Replica, up to 5 of them
  * Increases Throughput
* Multi AZ (for Disaster Recovery)
* Can switch from single AZ to multi AZ
* RDS Security
  * At Rest Encyption (Transparent Data Encryption)
  * In flight encryption (use certs)
  * Encryption operations
    * Can encrypt while making a snapshot
  * Network Security
    * Leverages security groupsm controls which ip can communicate with RDS
  * Access Management
    * IAM policies control who manages RDS
    * Plus = SSL Encryption

### Aurora

Amazon Aurora = MySql and Postgres, Amazon-built specifically

* High availability, costs more than normal RDS
* Backup and recovery
* Push button scaling, zero downtime, security
* Can backtrack

### Elasticache

AWS Elasticache

* Manages Redis and Memcached
* Replication vs sharding
* Redis = multi az with auto failover
* Memcached = multi node partition of data, sharding
* Cluster, Cluster mode enabled
* Lazy Load, cache aside, lazy population
* Write through
* Cache Eviction and TimeToLive TTL

## 5. DNS and VPCs

### Route 53

AWS has 200-250ish services, but Route 53 is advanced DNS server

* DNS = Domain Name System
  * Uses hierarchical naming structure
  * Translate hostname -> IP Address
* Key Terms
  * FQDN = Fully Qualified Domain Name
  * Domain Register = Amazon Route 53, GoDaddy, etc
  * DNS Record = A, AAAA, CNAME, NS
  * Zone File =contains DNS Records
  * Name Server = Resolves DNS Queries
  * Top Level Domain (TLD) = .com, .us, .uk
  * Second Level Domain (SLD) = amazon.com

Amazon Route 53

* Pros that set it apart from other DNS servers
  * Routing policy customization
  * Built in health checks 
  * Offers support for advanced DNS record types 
* Highly available, scalable, fully managed authoritative DNS
* Authoritative = Customer can update the DNS records
* Route 53 is a domain registrar, is a DNS server
  * DNS Server translates hostname to IP address
* 53 is a reference to the traditional dns port
* Record Types
  * A = Maps hostname to IPv4
  * AAAA = mapshostname to IPv6
  * CNAME = Maps hostname to another hostname
  * NS = Name servers for hosted zone, which controls how traffic is routed for a domain
* Hosted Zones
  * Container for records to define how to route traffic to a domain and subdomains
  * Public Hosted Zones = Contains records that specify how to route traffic on the internet(public domain names)
  * Private Hosted Zones = Records that specify how you route traffic within one or more VPCs (private domain names)
* TTL (time to live)
  * High TTL = long, 24 hr
  * Low TTL = short, 60 sec
* CNAME vs Alias
* ALias Record
  * Maps a hostname to AWS resource
  * Extends the DNS functionality
  * Can't set the TTL
* Routing Policies for Route 53
  * Define how Route 53 responds to DNS queries
  * Simple
    * Route traffic to a single resource
    * Specify multiple values in the same record
    * If multiple values returned, random one chosen by the client
  * Weighted
    * Control percentage of requests that go to the resource
    * DNS records must hae saem name and type
    * Can have health checks
  * Failover
    * Active-Passive
  * Latency Based
    * Redirect to resource that has least latency close to us
    * Helpful when latency is a priority
    * Latency based on traffic between users and AWS regions
  * Geolocation
    * Different from latency based
  * Multi Value Answer
    * Routing to multiple resources
    * up to 8 healthy records returned per multi value query
    * Not a substitute for having an ELB
  * Geoproximity
    * Route traffic to resources based on location of users and resources
    * Uses Route 53 Traffic Flow
    * Eample = East vs west US
    * Can be added in bias
* Health Checks
  * HTTP Health checks only for publix respirces
  * Automated DNS failover = health check
  * Integrated with CW (CloudWatch) metrics
  * Used to monitor an endpoint
  * Can combine health checks
  * Private Hosted Zones
* Traffic Flow
  * Simplify process of create and maintain records in complex cinfigurations
* Domain Registrar vs DNS
  * Example: GoDaddy as a Registrar, and Route53 as a DNS Service

### VPC Primer

* VPC = Virtual Private Cloud
  * Build your own local area network
  * Can include public or private subnets
  * Routing Table
  * Network ACL = Firewall that controls traffic to and from subnet. Different from Security Group. Gives internet to private subnets
  * Security groups = stateful, operate at EC2 instance
  * VCL Flow Log = like wireshark, captured data
  * VPC Endpoint
  * VPC Peering=connect 2 vpc with non overlapping ip ranges

## 6. Tier 3 Architecture

* T1 Public Subnet, T2 Private Subnet, T3 Data Subnet(RDS, Caches)
* Wordpress example

## 7. Amazon Simple Storage Service

### Amazon S3

* Storage of objects (like dropbox)
* Bucket - directory. Needs to be globally unique
* Every file has a key, is used in the path
* Max Size is 5TB
* Can enable versioning
* Encryption
  * 4 types of encryption
    * Server Side Encryption (SSE-C, SSE-S)
    * Client Side Encryption
    * Key management service (SSE-KMS)
  * Encryption in Transit for SSL and TLS
* Security: IAM is an options
* Networking, logging and auditing, presigned urls
* Can use S3 bucket to host URL

### Cross Origin Resource Sharing (CORS)

* CORS basics
  * Origin = Scheme, host, and port
  * CORS headers: access-control-allow-origin
  * Good Diagram in Notes
* Consistency Model: Strong consistency, no performance impact or additional cost

## 8. AWS Development

### Developing on AWS

AWS CLI

* Simulate the commands with a dry run flag: --dry-run
* sts decode-authorization-message = info for parsing error messages
* AWS EC2 Instance Metadata
  * Example: add latest/meta-data/placement/availability-zone to get availability zone info
* MFA with CLI
  * Must run STS GetSessionToken API Call
* AWS SDK Software developer kit
  * Example: DynamoDB
  * Be aware of API rate limits and Service Quotas
  * May need to increase limits
  * Exponential Backoff: Retry mechanism to deal with throttling exceptions
* Credentials for CLI
  * Prfile, EnvVars
  * ~/.aws/credentials

### Development with Simple Storage Service

MFA Delete
* Force user to generate a cde before deleting
* MFA = multi factor authentication
* Bucket Policies bs Default encryption
Access Logs
* Don't set your logging bucket to your monitoring bucket
S3 Replication
Pre-Signed URLs
* Allows expiring URLS
S3 Storage Class Options
* General Purpose
* S3 OneZone-Infrequent Access(IA)
* Intelligent Tiering
* Amazon Glacier: good for archiving and backup
  * Normal, and Glacier Deep Archive
Moving between storage classes
* Can transition
Lifecycle rules
* Transition actions
* Expiration actions
Baseline perfmance
* Use Multi-part solutions for uploads
* Can optimize byte range
* Select and glacier select
* Event notification
KMS Limitation
Amazon Athena
* Serverless query service
* Use SQL Language to query the files


## 9. Cloudfront, Beanstalk, and Docker Development

### Cloudfront

* General
  * Improves CDN read performance
  * Content is cached at the edge
  * Helps prevent DOS attacks
* Origins
* Gets from cache, or from the origin depending on availability
* Geo restrictions
  * Country whitelists or blacklists
  * Cloudfront = global edge network
* Caching
  * Based on headers, session cookies, query string parameters
  * Signed URL or signed cookies
* Signed urls
  * Either from Cloudfront, or S3 pre-signed URL
* Price Classes
* Field Level Encryption

### Elastic Beanstalk

* Deploy Web app 3-tier
* Management infrastrucutre to deploy app on AWS
* Handled load balancing, scaling, etc
* Components
  * Supported platforms listed
  * Web server vs worker tier
* Deployment Models
  * Deployment all at once
  * Rolling
  * Rolling with additional batch
  * Immutable
* Load Balancing
  * Traffic Splitting
* Overall
  * USeful for zero downtime updates
  * Plenty of CLI for interacting with it
  * Lifecycle policy (max number of versions = 1000)
  * Extensions: format is yaml or json
  * RDS available, with some Decoupled options too
  * Multi Docker
  * Can use HTTPS too
  * Can do custom platform if you want

### AWS EC5 Essentials

* ECS Clusters 
  * Essentially Docker
  * Run code in nearly any OS
  * Docker images are stored in docker repositories
  * Private= ECR Repos
* Docker vs VMs
* Docker Container Management
  * Three choices: ECS (Amazon's platforms), Fargate: Amazon's serverless platform, and EKS: Amazon's kubernetes/open source
* ECS Clusters
  * Groupings of EC2 Instances
  * Run on the ECS Agent (docker container)
  * Task Definitions: JSON form to tell how to run a docker container
  * ECS Service says how many tasks run
  * ECS Service with a load balancer, can support dynamic port forwarding
  * ECR = private docker image repository, access controlled through IAM
  * AWS Login command CLI 1(exam quesiton): $(aws ecr get-login --no-include-email --region eu-west-1)
  * AWS Login v2: aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stin
* Fargate
  * Serverless, don't need to provision any EC2 instances
  * Needs Instance profile, and task role
  * Taks placement: Must determine where to place it, constraints of CPU, memory
  * Strategies for Task placement
    * Binpack, random, spread, mix and match
  * Can auto-scale using cloudwatch or cloud alarm
  * Cluster Capcity Provider
  * ECS Data Volumes
* EKS
* ECS Classic 
  * NEeds EC2 instances
  * Configure security groups

## 10. CICD

### AWS CICD

Code integrations and Code Deployment

* Take your code, automatically build and test before putting in main
* Delivery = bring into the main branch
* Technology Stack
  * CodeCommit=Stores the Code. Exapmples= AWS Code Commit, Github, Bitbuckey
  * CodeBuild=Build and test the code= AWS Code Build, Jenkins
  * CodeDeploy=Deploy and provision the code: AWS Code Deploy, Elastic Beanstalk, etc
  * Can coordinate with AWS Code Pipeline
    * ARtifacts generated after every step, serve as inputs for every next step

### AWS CodeBuild

* Like Jenkins, TeamCity
* Charges by minute, uses docker under the hood
* Specify the source, make buildspec.yml for building it, typically stored with the code at root
* Lots of supported envs (java, ruby, etc)
* Can run in VPC

### AWS Code Deploy

* Deploys code to many EC2 instances
* EC2 instances are not necessarily managed by Elastic Beanstalk
* Handling deployments with open souce tools like Terraform, Ansible, Chef, Puppet
* Steps
  * Polling CodeDeploy constantly
  * appspec.yaml
  * Hooks order
  * Can be configured one at a time, or more
  * Redeploy or rollback

### Other AWS CICD Services

* CodeStar
  * Create CICD ready projects
* CodeArtifact
  * Storing and retrieving dependencies
* CodeGuru
  * Automated Code review
  * Code profiler: behavior, memory leak

## 11. Managing your Infrastructure and Code

### CloudFormation

* Infrastructure as Code
  * Build as template
  * Declarative way to outline resources and details
  * Benefits: nothing is manual, version controlled, code reviews for changes
    * Can destroy on the fly
    * Separation of concern
    * Don't reinvent the wheel
  * Cost: Can estimate the cost
* Cloudformation template
  * Resources
    * Limitation: Cannot be dynamic
  * Parameters
    * Pseudo parameters AWS:Region
  * Mappings (Access a static value)
  * Outputs
  * Cross Stack Reference
  * Conditions

### Cloudformation Functions

* Intrinsic functions
  * Fn::Ref: Reference function
  * Fn::GetAtt: Get attribute
  * Fn::FindInMap: access map values
  * Fn::ImportValue: grab from other templates
  * Fn::Join
  * Fn:Sub
* Condition Functions
* Cloud Formation Rollbacks
* Changesets
* Nested Stacks
* Cross Stacks
  * Helpful for re-using
* Stack Sets
* Cloud Formation Drift

## 12. AWS Monitoring, Troubleshooting, and Audit

### Cloudwatch

CloudWatch

* Metrics
* Detailed Monitoring
* Logs, log stream
  * Can export to S3 Bucket
* Alarm Targets
* Event Bridge builds on Cloudwatch

### AWS X-ray

* Debug in production
* Visual analysis of applications
* Compatible with lots of apps
* LEverages tracing requests
  * Needs to import SDK
  * Install Daemon or X Ray Kit
* Concepts: Segments, Subsegments
* Sampling Rules

### AWS Cloudtrail

* Monitoring
* Who made changes, kinda version control, enabled by default, used for governance, compliance and audits
* Management Events, Data Events, and Insight Events

## 13. AWS Integration and Messaging

### Amazon Simple Queue Service (SQS)

* Communicate with each other in apps
* Synchronization between apps is challenging
* Queue
  * Standard Queue
  * FIFO Queue
* Producer
* Consuming Messages
* Auto Scaling Group
* Decouple between application tiers
* Dead letter Queue - DLQ
* Delay Queue
* Long Polling
* Extended Client
* List of the must-know APIs
* FIFO
  * Deduplication
  * Message Grouping

### Amazon Simple Notification Service SNS

* Common service, used for notifications
* Send to email or other notification method
* Event Producer sends to SNS Topic
* Subscribers
  * SMS, Emails, SQS, etc
* AWS services send to SNS, or Cloudwatch, etc

### Kinesis

* Collect, process and analyze streaming data in real time
* Kinesis Data Stream
  * Takes app, then creates shards
  * Billed per shard, scales on shards
  * Partition Keys to determine which shard it goes into
  * Security
* Kinesis Producer = App, java app, etc
* Has an API to interact iwth it
* Provisioned Throughput Exceed
* Kinesis Consumers
  * Types: Enhanced fan out(push), or shared fan-out(pull)
  * AWS Lambda can be a consumer
  * Configure batch size
* KCL = Kinesis Client Library
* Can use Amazon DynamoDB as destination
* Shard Splitting
* Merging Shards
* Kinesis Data Firehose (alternative to Firehose)
* Kinesis Data Analytics (SQL Application)
* Ordering Data into Kinesis: used with partition to determie shard
* Kinesis vs SQS Ordering vs SNS


## 14. Lambda and DynamoDB

### Intro to AWS Lambda

### Even more lambda

### DynamoDB Basics

### Working with DynamoDB

## 15. API Gateway

### API Gateway Basics

### API Tuning

## 16. Working with Serverless Application Model (SAM)

### Serverless Application Model

### AWS Cloud Development Kit

### Amazon Cognito

### Other Serverless Features

## 17. Additional Security

### Advanced Integrity Management

### AWS Security and encryption

## 18. Additional AWS Services

* AWS SES = Simple Email Service
* DB Summary, lots of options (Dynamo, Neptune, Redshift)
* AWS Certificate Manager
* AWS Cloud Map (map of backend)
* AWS Fault injection Simulator
