from requirements_agent.models.refinement import ClarificationAnswer
from requirements_agent.models.requirements import RequirementAnalysis


def collect_clarification_answers(
    analysis: RequirementAnalysis,
    max_questions: int = 3,
) -> list[ClarificationAnswer]:
    """
    Ask the user up to max_questions clarifying questions in the terminal
    and return any non-empty answers.
    """
    questions = analysis.clarifying_questions[:max_questions]

    if not questions:
        return []

    print("\n--- CLARIFYING QUESTIONS ---\n")

    answers: list[ClarificationAnswer] = []

    for index, question in enumerate(questions, start=1):
        print(f"{index}. {question}")
        answer = input("Your answer (press Enter to skip): ").strip()

        if answer:
            answers.append(
                ClarificationAnswer(
                    question=question,
                    answer=answer,
                )
            )

    return answers