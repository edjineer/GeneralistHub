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

### 1.2 Tokenization

### 1.3 Basic Prompting

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