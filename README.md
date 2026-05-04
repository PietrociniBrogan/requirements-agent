# Requirements Agent

A Python-based AI requirements analysis project that turns meeting notes, workflow descriptions, and process documents into structured implementation plans.

The goal of the project is to build a lightweight human-in-the-loop requirements analysis agent that can identify missing information, generate targeted clarifying questions, separate confirmed requirements from assumptions, and refine next steps for workflow or application design.

This project was inspired by a recurring need in workflow and requirements meetings, where important implementation details often remain buried in transcripts or unstructured notes. The aim is to create a tool that can take raw discussion notes and produce clearer, more actionable outputs for solution design and implementation planning.

## Current Capabilities

The project currently supports:

- Reading sample business/process notes from a local input file
- Loading local configuration through environment variables
- Sending workflow notes to an LLM for first-pass analysis
- Returning structured JSON output using Pydantic schemas
- Validating model output before using it in the application
- Generating targeted clarifying questions based on missing or ambiguous information
- Accepting user clarification answers through a terminal-based loop
- Producing a refined requirements analysis based on the original notes, initial analysis, and user-provided answers
- Separating confirmed requirements, assumptions, unresolved questions, and implementation next steps

## Current Workflow

The current application flow is:

1. Read a workflow/process note file from `sample_data/inputs`
2. Generate an initial structured requirements analysis
3. Identify missing information and clarifying questions
4. Ask the user a limited set of clarification questions
5. Use the answers to refine the analysis
6. Return a refined structured output

At this stage, the project is best described as a lightweight human-in-the-loop LLM workflow with emerging agentic behavior. The clarification loop allows the system to reason over uncertainty, ask for missing information, and refine its output based on user feedback.

## Project Structure

```text
requirements-agent/
├─ .env
├─ .env.example
├─ .gitignore
├─ README.md
├─ requirements.txt
├─ docs/
│  └─ architecture-reference.md
├─ sample_data/
│  └─ inputs/
│     └─ meeting_notes_01.txt
├─ src/
│  └─ requirements_agent/
│     ├─ config.py
│     ├─ main.py
│     ├─ llm/
│     │  ├─ client.py
│     │  └─ prompts.py
│     ├─ models/
│     │  ├─ requirements.py
│     │  └─ refinement.py
│     └─ services/
│        ├─ ingest.py
│        ├─ analyzer.py
│        ├─ clarifier.py
│        └─ refiner.py
└─ tests/
```
