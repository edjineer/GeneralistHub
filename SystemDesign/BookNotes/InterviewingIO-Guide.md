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
      * **Basics:**
      * **Strengths:**
      * **Weaknesses:**
    * NoSQL
      * **Basics:**
      * **Strengths:**
      * **Weaknesses:**

3. Scaling

4. CAP Theorem

5. Web Authentication and basic security

6. Load Balancers

7. Caching

8. Message Queues

9. Indexing

10. Failovers

11. Replication

12. Consistent Hashing

## Part 3: A 3 Step Framework to crush any system Design interview

Time: *40 minute read*

## Part 4: Watch us design simple systems from scratch, adn learn how to get unstuck

Time: *80 minute read*

## Questions for Later

* For instance, you should understand the difference between SQL and NoSQL databases, their broad performance characteristics, and the types of applications each might be useful for (which we’ll teach you later in this guide).
* URL vs URI
* Review and Reinforce each of the 12 tech fundamentals

## Next Steps

* Address Remaining Questions
* Read Bill Brnett and Dave Evans' "Designing your Life"
