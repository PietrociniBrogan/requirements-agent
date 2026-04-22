# Requirements Agent — Architecture Reference

## Purpose

Requirements Agent is a Python-based AI requirements analysis project that takes generic business/process notes and turns them into an implementation-oriented analysis.

The long-term goal is to support a human-in-the-loop clarification loop that:

- identifies ambiguity
- asks targeted clarifying questions
- separates confirmed requirements from assumptions
- refines the implementation plan

## Current State

The project currently supports:

1. reading a sample input file
2. sending that input to an LLM
3. returning a first-pass analysis

Current output is still free-form text. The next planned step is to move to structured, validated output.

---

## High-Level Architecture

```text
Input file
  -> ingest.py
  -> analyzer.py
     -> prompts.py
     -> client.py
  -> main.py prints result
Flow summary
main.py starts the app and coordinates the workflow
config.py loads environment settings
ingest.py reads the source notes from disk
analyzer.py owns the “analyze these notes” use case
prompts.py defines the model instructions
client.py creates the OpenAI client
the model returns analysis text
main.py prints the result
Repository Structure
requirements-agent/
├─ .env
├─ .env.example
├─ .gitignore
├─ README.md
├─ requirements.txt
├─ sample_data/
│  └─ inputs/
│     └─ meeting_notes_01.txt
├─ src/
│  └─ requirements_agent/
│     ├─ __init__.py
│     ├─ config.py
│     ├─ main.py
│     ├─ llm/
│     │  ├─ __init__.py
│     │  ├─ client.py
│     │  └─ prompts.py
│     └─ services/
│        ├─ __init__.py
│        ├─ ingest.py
│        └─ analyzer.py
└─ tests/
File Responsibilities
Root-level files
.env

Local environment variables and secrets.

Examples:

OPENAI_API_KEY
MODEL_NAME
LOG_LEVEL

This file is local-only and should never be committed.

.env.example

Safe template showing which environment variables are required.

This file is committed so others can recreate the local setup.

.gitignore

Defines what Git should not track.

Important examples:

.env
.venv/
__pycache__/
requirements.txt

Dependency snapshot used to recreate the environment.

README.md

Human-facing overview of the project.

sample_data/inputs/meeting_notes_01.txt

Sample non-sensitive input file used for development and demo purposes.

Application package
src/requirements_agent/config.py

Centralized configuration.

Responsibilities:

load .env
expose settings through Config
validate required configuration

Reason:
Configuration should be managed in one place instead of scattered across the codebase.

src/requirements_agent/main.py

Application entry point.

Responsibilities:

validate configuration
locate the input file
call the ingestion service
call the analysis service
print results

Reason:
main.py should orchestrate the workflow, not contain all implementation details.

src/requirements_agent/services/ingest.py

Input-reading service.

Responsibilities:

verify file exists
verify file type is allowed
read and return text content

Reason:
File ingestion is its own concern and should not be mixed into main.py.

src/requirements_agent/services/analyzer.py

AI analysis service.

Responsibilities:

receive note text
build the analysis request
call the LLM
handle known API failure cases
return analysis output

Reason:
This file owns the “analyze notes” use case and keeps business logic separated from startup logic.

src/requirements_agent/llm/client.py

LLM client factory.

Responsibilities:

create and return the OpenAI client

Reason:
Provider-specific setup should be centralized and reusable.

src/requirements_agent/llm/prompts.py

Prompt definitions.

Responsibilities:

define the system prompt
define prompt-building logic for note analysis

Reason:
Prompts are part of application behavior and should be version-controlled and easy to refine.

Design Principles
1. Separation of concerns

Each file has one main responsibility.

Examples:

config handling in config.py
file reading in ingest.py
model call logic in analyzer.py
2. Thin entry point

main.py should coordinate the app, not do everything directly.

3. External dependency isolation

OpenAI-specific setup is kept under llm/ instead of being mixed throughout the app.

4. Incremental vertical slices

The project is being built in small end-to-end milestones:

project scaffold
input ingestion
first AI analysis
next: structured schema
next: clarification loop
5. Safe configuration management

Secrets are stored in .env, while .env.example provides a GitHub-safe template.

Current Runtime Flow

When running:

$env:PYTHONPATH="src"
python -m requirements_agent.main

the application flow is:

start main.py
validate config using config.py
read the sample input using ingest.py
pass note text into analyzer.py
build prompts using prompts.py
create the OpenAI client using client.py
send the request to the model
return and print the analysis
Error Handling Approach

The project currently treats the LLM call as an external dependency that can fail.

Current handling includes:

validating required config before runtime
validating input file presence and type
catching known API failure cases such as quota/rate-limit errors
failing clearly if the model returns no usable output

Reason:
LLM calls should be treated like any other external service dependency, not as guaranteed-success code.

Current Limitations

Current limitations are intentional to keep v1 manageable:

output is still free-form text
no structured schema validation yet
no clarification loop yet
no export to JSON/Markdown files yet
no tests yet
no CLI input selection yet
Planned Near-Term Improvements
Next
add a structured Pydantic schema
require JSON output from the model
validate model output before trusting it
After that
introduce a clarification-question loop
accept user answers
refine the analysis based on confirmed information
Later
export results to files
add tests
improve logging
add a CLI interface for selecting input files
Developer Workflow

Typical local workflow:

git status
git add .
git commit -m "Meaningful milestone message"
git push

Typical run command:

$env:PYTHONPATH="src"
python -m requirements_agent.main
Quick Reference
One-line purpose of each major file
main.py → starts and coordinates the application
config.py → loads and validates settings
ingest.py → reads input files
client.py → creates the OpenAI client
prompts.py → defines what the model is asked to do
analyzer.py → performs the AI note-analysis workflow
Key project idea

This project is not just “a prompt.”
It is an application that uses an LLM as one component inside a structured workflow.
```
