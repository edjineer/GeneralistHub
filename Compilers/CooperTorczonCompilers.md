# Engineering a Compiler, Second Edition

Authors: Keith Cooper, Linda Torczon, Rice University 2012

## Impressions

## Questions to Revisit

* JVM, or Just in Time

## 1. Overview of Compilation

Introduction

* Compiler = Translates other programs for execution
* Needs a scheme for mapping content from source to target languages
* Often a middle, intermediate language to improve translation that is optimized
* **Instruction Set** = Output of a compiler, to be executed
* Interpreters are not compilers.
  * Some languages include both interpretation and compilation
  * JVM/Just in Time
* Common between Interpreters and Compilers
  * Assess Validity of a program
  * Build internale model of structure, meaning. Semantics
  * Where to store values
* Fundamental Principles
    1. Compilers must preserve the meaning of the original program (Correctness)
    2. The compiler mus improbe the input program in some way (Practical)

Compiler Structure

* Timeline
  * 1955 is first year compilers were made
  * 1980s - Compilers were monoliths
* Three Phase Compiler
* Front End
  * Understand the source languge program
  * Translate OG code to an intermediate representation (IR)
* Back End
  * Focuses on mapping the programs to target machine
  * Back end assumes no semantic or syntactic errors
* Optimizer
  * Compiler can take multiple passes of intermediate representations (IR) to optimize it
  * Retargeting = Changing the compiler to generate code for a new processor
  * Can help reduce page faults or use less energy
* TODO Insert image of typical compiler from pg 34

Overview of Translation (35)

## 2. Scanners

## 3. Parsers

## 4. Context Sensitive Analysis

## 5. Intermediate Representations

## 6. The Procedure Abstraciton

## 7. Code Shape

## 8. Introduction to Optimization

## 9. Data Flow Analysis

## 10. Scalar Optimizations

## 11. Instruction Selection

## 12. Instruction Scheduling

## 13.Register Allocation

