# LLM Essentials Course by Nebius

Notes for Nebius AI LLM Essentials course, enrollment from May->July 2025.

## Topics To Revisit Later

* What is best practice nowadays for safely storing API keys?
* What exactly is a token?
* Does order of messages matter in the creation of a client.completions?
* Normal amount of time to wait for LLM responses?

## Topic 1: LLM API Basics

### 1.1 Intro to LLM APIs

* [Link to Colab](https://colab.research.google.com/github/Nebius-Academy/LLM-Engineering-Essentials/blob/main/topic1/1.1_intro_to_llm_apis.ipynb)
* [Get started with jupyter](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
* Text passed to an LLM is a prompt, and LLM output is a completion or a response
* Prompt and completion length are indicated in tokens
* Returned object is chat_completion class out of open_ai
* Dialog Roles
  * user, assistant, system
  * Can include LLM's previous message as an "assistant" message in the messages list
  * There is a max content length
  * Each dialog under the hood has 4 sections, which end up being sent as a structured prompt
* Max Content Length
  * Dependent on LLM, llama is 128k tokens
  * max_tokens parameter
  * client.chat.completions.create(model, messages, max_tokens)
  * Pro-tip; view the whole completion with completion.to_json
  * finish_reason: usually set to "stop", but when max_token is specified then it is "length"
* OpenAI API
  * Shares similar API with Nebius's
* Multimodal Input
  * VLMs= visual language models or MLLMs, multimodal LLMs
  * OpenAI requires an image to be encoded with base64 before sending through an LLM
  * Nebius can also access VLMs
* Generating images
  * Text to image models out there
  * client.images.generate(mode, response_format="b64_json, extra_body=specificatiions, prompt="")
  * Example loading it in and displaying the image

Practice Exercises:

* Task 1
  * Challenges: Names as first and last
  * Handling new lines
* Task 2
  * Come back

### 1.2 Tokenization

* [Link to Colab](https://github.com/Nebius-Academy/LLM-Engineering-Essentials/blob/main/topic1/1.2_tokenization.ipynb) 
* Prompts are tokenized before going into the LLM, completions are also generated token by token
* Words are cut into subword units, not words. Having character level tokens
* Tokens with " " are different than tokens without " "
* Open source LLMs are available at Hugging Face
* Different LLMs may have different tokenizers: example with gpt-4o-mini vs Qwen. Qwen uses G' as space instead of space
* Qwen does not require logging in
* LLMs don't usually see text on character level
  * LLMs are not good at arithmetic, reversing strings, etc
* Don't trust LLM Calculations

Practice Exercises

### 1.3 Basic Prompting

* Instruction and Context
  * Three parts
    * System: set style, tone, knowledge domain where LLM is supposed to answer. Role assignment
    * Instruction: Tells LLM exactly what to do
    * Context: Background info and specifics relevant to task
* Advice
  * Clarity, instructions, requirements, and restrictions
  * Give a clear understanding for: style, length, level of details
  * Example: "Do NOT use words: x, y, z; Only use words a, b, c"
* Formatting
  * LLMs are natural markdown users
  * **Bold**, *italics*, Sections(#) CAPS
* Negative prompting
  * Example: It's more effecitve to say "Answer in 2-3 sentances" than "Don't be too wordy"
* Role Assignment
  * Assign it who or what it should impersonate
* Levels of Details
  * There may be improvization at any stage
  * Example: Fantasy world. Asking "how's the weather" without telling the weather may lead to creative results inconsistent with the greater world
  * **Hallucinations**: Unbased asssumptions from an LLM
  * Recommendations to combat this:
    * Assess which details are crucial, include them in the prompt. May bloat the prompt
    * In system prompt, forbid LLM to discuss anything not related to the primary goal
    * Add context and using RAG
  * LLM Can only handle a certain level of detail
    * Too many details lead to distortion
    * 10 is too large for a number of requirements
    * Contradictory requirements lead to inconsistent results
  * Reasoning
    * Detailed solution = Chain of Thought
    * LLMs produce more accurate solutions when CoT instead of plopping out answers
    * Most LLMs do CoT by default
  * Extracting Answers
    * "In the end, output only the net surplus after #ANSWER:", `answer = float(result.split("#ANSWER:")[1].strip())`
    * Good to let it give some words, but be able to parse out the answer
  * Non-Linear Reasoning
    * Evolution to the CoT (CoT = LLM gets correct answer from first try). now NLR = May need to experiment, try other things
    * Orchestration techniques: Tree of Thoughts, Graph of Thoughts
    * Current Top NLR Models = Phi-4, Llama, DeepSeek R1
  * Psychological Tricks
    * LLMs are trained on human data, so human tricks can work
    * "This is important for my career", "Take a deep breath and work this through step by step", "I'm going to pay you better if you answer this better"

### 1.4 What goes wrong

### 1.5 Choosing an LLM

### 1.6 LLM Inference Parameters

### 1.7 Creating an LLM-powered Character

## Topic 2: LLM Workflows

## Topic 3: Context

## Topic 4: Self-Served LLMs

## Topic 5: Optimiation and Monitoring

## Topic 6: Fine-Tuning

## Project