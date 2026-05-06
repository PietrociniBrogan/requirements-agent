# Usage Guide

This guide explains how to set up, run, and test the Requirements Agent project locally.

## Setup

This project uses Python 3.11+.

Create and activate a virtual environment:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Create a local `.env` file based on `.env.example`:

```env
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-5-nano-2025-08-07
LOG_LEVEL=INFO
```

The `.env` file should not be committed to GitHub.

## Running the App

Run the app with the default sample input:

```powershell
$env:PYTHONPATH="src"
python -m requirements_agent.main
```

Run the app with a specific input file:

```powershell
$env:PYTHONPATH="src"
python -m requirements_agent.main --input sample_data/inputs/meeting_notes_01.txt
```

Limit the number of clarifying questions:

```powershell
$env:PYTHONPATH="src"
python -m requirements_agent.main --input sample_data/inputs/onboarding_workflow.txt --max-questions 2
```

Set a custom output directory:

```powershell
$env:PYTHONPATH="src"
python -m requirements_agent.main --input sample_data/inputs/meeting_notes_01.txt --output-dir outputs/demo_run
```

## Outputs

Generated outputs are saved locally under the selected output directory.

Default generated files include:

```text
outputs/
├─ initial_analysis.json
├─ refined_analysis.json
└─ refined_analysis.md
```

The `outputs/` folder is intentionally ignored by Git because generated files can change on each run.

Curated examples are available in the `examples/` folder so the project can be reviewed on GitHub without requiring an API key.

## Examples

See the `examples/` folder for:

- a sample workflow input file
- a refined Markdown output generated after the clarification loop

These examples use generic, non-sensitive workflow content.

## Testing

Run the test suite:

```powershell
python -m pytest
```

The current tests cover:

- input file ingestion
- Pydantic model defaults
- Markdown and JSON export behavior
- CLI path resolution

The tests intentionally avoid live LLM/API calls so they remain fast, reliable, and free to run.

## Current Status

The project now includes a working end-to-end v1 flow:

- Input file ingestion
- Command-line input selection
- Structured AI analysis
- Model output validation with Pydantic
- Clarification question generation
- User response collection
- Refined requirements output
- JSON and Markdown exporting
- Curated GitHub examples
- Basic unit tests

This is a functional first version of the project.

## Planned Improvements

Potential next steps include:

- Improve prompt rules to reduce overlap between confirmed requirements and assumptions
- Add richer example inputs and outputs
- Add support for multiple clarification rounds
- Add cleaner terminal formatting
- Add optional non-interactive mode for automated runs
- Add evaluation examples for output quality
- Add support for longer transcript inputs
