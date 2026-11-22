
def analyze_task(
    problem,
    object_name,
    useful_action,
    undesired_effect,
    goal,
    constraints,
    resources
):
    # 1. Анализ исходной проблемы
    if problem.strip():
        problem_analysis = (
            f"Необходимо решить следующую проблему: {problem}"
        )
    else:
        problem_analysis = "Описание проблемы не заполнено."

    # 2. Формирование технического противоречия
    if useful_action.strip() and undesired_effect.strip():
        contradiction = (
            f"При попытке обеспечить функцию «{useful_action}» "
            f"возникает нежелательный эффект: "
            f"«{undesired_effect}»."
        )
    else:
        contradiction = (
            "Недостаточно данных. Укажите полезную функцию "
            "и нежелательный эффект."
        )

    # 3. Формулирование идеального конечного результата
    if goal.strip():
        ideal_result = (
            f"Объект «{object_name}» должен самостоятельно "
            f"обеспечивать следующий результат: {goal}. "
            "При этом нежелательный эффект должен быть устранён."
        )
    else:
        ideal_result = (
            "Необходимо уточнить желаемый результат, "
            "чтобы сформулировать ИКР."
        )

    # 4. Учет ограничений и ресурсов
    available_resources = resources.strip() or "Не указаны."
    task_constraints = constraints.strip() or "Не указаны."

    return {
        "problem_analysis": problem_analysis,
        "contradiction": contradiction,
        "ideal_result": ideal_result,
        "resources": available_resources,
        "constraints": task_constraints
    }
