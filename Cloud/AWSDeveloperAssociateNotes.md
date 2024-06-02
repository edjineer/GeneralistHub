# AWS Developer Associate Notes

By Fasal Kahn, hosted through Stormwind Studios
Enrolled in Summer 2024

## Running Questions

* SQS
* Difference between Data Centers and availability zone

## 1. Introduction ot Developing in Azure

### Getting Started with AWS

* History:
  * 2002 founded. 2007 expanded massively
  * 2019: AWS had 35+million in revenue
  * Low barrier of entry for Cloud
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
  * Applies Least Privilege Principle
  * Create Permissions with Effect, Actions, and Resources
  * Policies can be Inherited across groups
* IAM Policies Structure
  * Statements have : sid, effect, principal, action, resource
* Password Policy
  * Stregth, allowing people to change their passwords, etc
  * Multi Factor Auth
    * Support for AWS is either USB Key, Phone app, etc
* How user can access AWS:
  1. AWS Management Console/Web Browser page: password + MFA
  2. Command Line CLI: protected by access key
  3. AWS Coftware Developer Kit: protected by access key

## 2. EC2

### EC2 Basics

### EC2 Instance Storage Section

## 3. Load Balancing, Auto Scaling Groups, and EBS Volumes

## 4. RDS, Aurora, and Elasticache

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