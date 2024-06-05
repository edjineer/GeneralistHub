# Interviewing IO System Design Guide

[Link](https://interviewing.io/guides/system-design-interview)
Estimated Completion Time = 6 hours

## Part 1: How to Approach a System Design Interview

* Engineering is great when you know there is one great solution out there
* Design problems are where there is no fixed or predetermined outcome
  * You're creating a map for someone else to find the solution
  * Think like a Tech Lead: explain to junior engineers
* Pro Tip/Strategy: Answer enough details for the interviewer to dive into your strengths on their own.
* Looking for: Broad understanding of fundamentals, back and forth on constraints and parameters, qualified decisions based on trade-offs, Unique direction based on experience, holistic view of system and its users.
* Not Looking for: deep expertise, assumptions, predefined path, specific answers, technical considerations.
* Ask details around what type of sercice the interviewer wants you to build: who are the users, what type of traffic, what limits?
* Example: Data model with an ID introduced:
  * Are IDs exposed to users? How long do they need to be t oavoid collisions? Visibility from auto incrementing and guessing ids? Confusing characters like 1,0?
* Anchor Decisions in the **user experiences** they create
  * Example: Log in before uploading a picture: pros and cons to each approach
* Red Flags and Green Flags
  * G: Communicate honestly about what you do and don't know
  * Embrace Feedback, make it collaborative
  * Direct more of the interview
  * Don't leave long stretches of silence
  * Weight pros and cons, but **make a decision** before moving on to other components. "Based on all these tradeoffs, I'll use this type"
* Say the generic name of a component, not a brannd name. Don't say "Kafka", say "a queue"

## Part 2: 15 Fundamental System Design Concepts

Time: *70 minute read, 2.5 hours of videos*

Three Core Concepts

1. There's no right way to design a system
    * [] Interviw comparison across two candidates (Left off at 25:00-Bruno High Level Design)
      * Example of Bruno from Google
      * Example of Dima from Microsoft
      * Scale by introducing hosting providers
      * Conflicts resolved by git branch strategy
    * [x] Second Video
2. General Rules of Thumb
    * If interviewer inturrupts you, its because you're going off track
    * Prior Experience affects both sides
    * Time Management: Better to get through everything broadly than any one thing in detail
    * Approach the Problem with WHY, not what
      * If you can avoid distributed systems, do it. Aim for simple
3. Exactly what words to say in specific situations
    * Strong Candidates say "I don't know" and strengthen it with a buffer
      * Example: Load balancer.
        * "I don't know, and Im going to look it up after this interview, but if I had to give it my best guess, I'd say X and here is why". Or "I don't have hands on experience, but I've read this about it"
    * If you push back against your interviewer, then do so affirmatively "Ok, yes, sure". Use "We" plenty
    * Handwave to save time: "Here's a rabbit hole we could go down, but let's skip for now"
    * Be proactive about tricky parts: iron them out first.
    * Cold Interviewers and Warm Interviewers
      * Cold: Ask questions like "stop me if I'm going off track"
      * Warm: Check in with them
    * The more questions you ask, the more junior you seem. Check in at major milestones only. Ex: Done talking requirements or high-level design.

12 Technical System Design Concepts

1. APIs
    * Basic Def: A structured, mutually agreed upon way to exchange critical information. A set of rule or contracts through which two or more sw entities communicate
    * REST: Representational State Transfer
      * **Basics:** Make a GET Request, and a POST request based on the info. Uses a single URI to access a resource with various actions to perform based on the resources.
      * **Strengths:** Creates structured ways of getting+changing info from a DB. Has tooling that supports generating documentation that is easier for devs to understand.
      * **Weaknesses:** Requires you to write the requests for each type of entity in your DB. GraphQL has no separate inqueries to grab all the data the caller needs. Worse on space efficiency than RPC.
    * RPC: Remote Procedure Call
      * **Basics:** Processes are efficient by making close and frequent communication. Allows executing a command or procedure on a remote machine. API is mor of an action or command.

      ``` txt
      RPC: /placeAnOrder (OrderDetails order)
      REST - POST /order/orderNumber={} [Order body]
      ```

      * **Strengths:** More space efficient than REST. Development is easier since code you write does not require much special syntax.
      * **Weaknesses:** Only used for internal communication, and there can be complications as you communicate between machines.
    * GraphQL
      * Analogy: Amazon Go, walk in, grab what you need, walk out.
      * **Basics:** Data is structured in a graph relationship, and left for others using it to define what they need from it. A request is made to fetch all the data with one call. Relies on having the right schema built to encompass all the queries you can make. Used in mobile apps a lot.
      * **Strengths:** Good for customer facing web and mobile apps. Front end can craft requests to get and modify info without building more backend routes.
      * **Weaknesses:** Some upfront development work needed for front and backend. Less friendly for external users than REST.  Not suitable for use cases where data needs to be aggregated on the back end.

2. Databases (SQL vs NoSQL)
    * SQL
      * **Basics:** Comprised of tables, where each row is a data entity, and each col is info about the field. Each table has bits that connect.
      * **Strengths:**
        * More powerful querying out of the box
        * Stronger ACID guarantees out of the box. Preferred if you want customers to always see up to date info, even if there is a delay.
          * Atomic: transaction completes in its entirety without failures, or else it is reverted. Half-writes aren't possible.
          * Consistent: SQL has strong consistency: Certain parts of the DB are locked when written.
          * Isolation: Read and write requests are not impacted by other transactions.
          * Durable: Failure in a given transaction can be recovered.
      * **Weaknesses:**
        * Slower to write into because SQL uses B-Trees, but quicker to read. SQL uses 4KB pages
        * Strong Consistency means that it is expensive, and thus higher latency
        * Mixed Schema Data is not a good fit
    * NoSQL
      * Four Types:
        1. **Key Value.** Most popular. Stores data with unique keys, system is opague to contents of the data. Scales by using sharding across nodes.
        2. **Document Databases:** Like Key-value, but can aggregate searches and store in JSON, XML, YAML.
        3. **Columnar Databases:** Store info in tables, but allow denormalized data. Indexing by columns, not rows.
        4. **Graph Databsaes:** Store complicated node and edge relationship, allow for easy traversal and modification.
      * **Basics:** All 4 types do not need rigid schemas like SQL does. Uses LogStructuredMergeTree instead of B Tree.
      * **Strengths:**
        * Faster to write, but slower to query.
        * Managed DBs like DynamoDB or Azure MongoDB include sharding and scaling right out of the box.
      * **Weaknesses:**
        * Eventual Consistency: your data you query might be stale for a couple of seconds before it is consistent.
        * More limited in efficient queries.

3. Scaling
    * There are different factors to scale and different approaches
    * Vertical Scaling: Upgrade existing resources
      * There is a limit: you can only improve so far
      * Risk of having a single point of failure
      * Benefits = Reduce latency since you only have one machine to communicate with, and don't need to rework your architecture
    * Horizontal Scaling: Get more resources
      * Communication across multiple computers to store and process information
      * Database Scaling:
        * Database sharding: split across into smaller pieces. Would need a hash function to determine a consistent manner to assign a partition to an item
      * Compute Scaling: Divide content across many parallel jobs to deliver
    * If asked about scaling in an interview, Ask about the number of users and amount of data that is requred, inform the decision making

4. CAP Theorem
    * Fundamental Theorem for distributed Design. All about Trade-Offs
      * System needs to make a choice between the three. It cannot achieve all three, but can have 2 of three
      * Most Systems do Fault Tolerance, and sacrifice either C or A
    * Consistency: Every node in a network will have access to the same data. Eventual Consistency = down the line, eventually all users will have same data even after a delay
    * Availability: The system is always available to the users
    * Partition tolerance: In case of a fault in the network or communication, the system still works

5. Web Authentication and basic security
    * Trade off between safety and convenience: Goal of security is to minimize risks while providing functionality.
    * Authentication: verify identity of users
      * Hashing, Salting
      * Session Tokens have expiration dates
      * Encrypt traffic with https
    * Authorization: Determine who has permission to view what.
    * JSON Web Tokens
      * Validated by signing the payload, or encrypting the payload

6. Load Balancers
    * LBs distribute traffic across machines, and account for failures
    * Round Robin: Rotate through assignments
    * Least Connections
      * Hashing. Based on an arbitraty key, returns a numeric result for each key.

7. Caching


8. Message Queues

9. Indexing

10. Failovers

11. Replication

12. Consistent Hashing

## Part 3: A 3 Step Framework to crush any system Design interview

Time: *40 minute read*

## Part 4: Watch us design simple systems from scratch, and learn how to get unstuck

Time: *80 minute read*

## Questions for Later

* For instance, you should understand the difference between SQL and NoSQL databases, their broad performance characteristics, and the types of applications each might be useful for (which we’ll teach you later in this guide).
* URL vs URI
* Review and Reinforce each of the 12 tech fundamentals
* DBs
  * ACID in DBs: dive into more reinforcing details and examples
  * [B-Trees] (link: https://en.wikipedia.org/wiki/B-tree) vs LSMT
  * Mixed Schema Data
  * Sharding with noSQL
  * Denormalized Data
* Why is Fault Tolerance more important than consistency and availabiltiy
* How would I answer a scaling question

## Next Steps

* Address Remaining Questions
* Read Bill Brnett and Dave Evans' "Designing your Life"
