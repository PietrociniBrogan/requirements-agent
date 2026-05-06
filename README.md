# Requirements Agent

A Python-based AI requirements analysis project that turns meeting notes, workflow descriptions, and process documents into structured implementation plans.

The project is designed as a lightweight human-in-the-loop requirements analysis agent. It identifies missing information, generates targeted clarifying questions, accepts user responses, separates confirmed requirements from assumptions, and refines next steps for workflow or application design.

This project was inspired by a recurring need in workflow and requirements meetings, where important implementation details often remain buried in transcripts or unstructured notes. The goal is to take raw discussion notes and produce clearer, more actionable outputs for solution design and implementation planning.

## Current Capabilities

The project currently supports:

- Reading business/process notes from a local `.txt` or `.md` input file
- Selecting input files through a command-line interface
- Loading local configuration through environment variables
- Sending workflow notes to an LLM for first-pass analysis
- Returning structured JSON output using Pydantic schemas
- Validating model output before using it in the application
- Generating targeted clarifying questions based on missing or ambiguous information
- Accepting user clarification answers through a terminal-based loop
- Producing a refined requirements analysis based on the original notes, initial analysis, and user-provided answers
- Separating confirmed requirements, assumptions, unresolved questions, and implementation next steps
- Exporting results to JSON and Markdown files
- Providing curated example inputs and outputs for GitHub review
- Running basic unit tests for deterministic components

## Current Workflow

The current application flow is:

1. Read a workflow/process note file from the provided input path
2. Generate an initial structured requirements analysis
3. Save the initial analysis as JSON
4. Identify missing information and clarifying questions
5. Ask the user a limited set of clarification questions
6. Use the answers to refine the analysis
7. Save the refined output as JSON
8. Save a stakeholder-readable Markdown summary

At this stage, the project is best described as a lightweight human-in-the-loop LLM workflow with emerging agentic behavior. The clarification loop allows the system to reason over uncertainty, ask for missing information, and refine its output based on user feedback.

## Project Structure

```text
requirements-agent/
├─ .env.example
├─ .gitignore
├─ README.md
├─ requirements.txt
├─ pytest.ini
├─ docs/
│  ├─ architecture-reference.md
│  └─ usage.md
├─ examples/
│  ├─ README.md
│  ├─ request_workflow_input.txt
│  └─ request_workflow_refined_output.md
├─ sample_data/
│  └─ inputs/
│     ├─ meeting_notes_01.txt
│     └─ onboarding_workflow.txt
├─ src/
│  └─ requirements_agent/
│     ├─ __init__.py
│     ├─ cli.py
│     ├─ config.py
│     ├─ main.py
│     ├─ llm/
│     │  ├─ __init__.py
│     │  ├─ client.py
│     │  └─ prompts.py
│     ├─ models/
│     │  ├─ __init__.py
│     │  ├─ requirements.py
│     │  └─ refinement.py
│     └─ services/
│        ├─ __init__.py
│        ├─ analyzer.py
│        ├─ clarifier.py
│        ├─ exporter.py
│        ├─ ingest.py
│        └─ refiner.py
└─ tests/
   ├─ test_cli.py
   ├─ test_exporter.py
   ├─ test_ingest.py
   └─ test_models.py
```

## Key Design Concepts

This project is intentionally structured as a real Python application rather than a single prompt script.

Important design choices include:

- `config.py` centralizes environment variable loading and validation
- `cli.py` handles command-line arguments and path resolution
- `ingest.py` handles input file reading and validation
- `analyzer.py` performs the first-pass requirements analysis
- `clarifier.py` collects user answers to clarification questions
- `refiner.py` produces the refined analysis after user feedback
- `exporter.py` writes validated outputs to JSON and Markdown files
- `prompts.py` keeps LLM instructions separate from application logic
- `models/` defines structured Pydantic schemas for validated outputs
- `tests/` covers deterministic parts of the application without relying on live API calls

The goal is to keep the system modular, explainable, and easy to expand.

## Documentation

Additional project documentation:

- [Usage Guide](docs/usage.md) — setup, running the app, outputs, and tests
- [Architecture Reference](docs/architecture-reference.md) — deeper explanation of the project structure and design decisions
- [Examples](examples/) — curated sample input and refined output

## Project Framing

This project is not intended to be an autonomous software architect or a multi-agent platform.

It is currently a lightweight human-in-the-loop requirements analysis system that uses an LLM as one component in a structured Python workflow. The clarification loop is the first step toward more agentic behavior because the system identifies uncertainty, asks for missing information, and refines its output based on the user’s answers.
