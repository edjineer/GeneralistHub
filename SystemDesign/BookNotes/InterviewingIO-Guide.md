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

## Part 3: A 3 Step Framework to crush any system Design interview

## Part 4: Watch us design simple systems from scratch, adn learn how to get unstuck

## Questions for Later

* For instance, you should understand the difference between SQL and NoSQL databases, their broad performance characteristics, and the types of applications each might be useful for (which we’ll teach you later in this guide).

## Next Steps

* Address Remaining Questions
* Read Bill Brnett and Dave Evans' "Designing your Life"
