
import streamlit as st
from triz_solver import analyze_task

st.set_page_config(
    page_title="TRIZ AI Assistant",
    page_icon="💡",
    layout="wide"
)

st.title("💡 TRIZ AI Assistant")

st.subheader(
    "Интеллектуальный помощник по решению изобретательских задач"
)

st.write(
    "Опишите свою задачу. Приложение поможет структурировать "
    "проблему и подготовить её к анализу с помощью ТРИЗ."
)

st.markdown("---")

st.header("1. Постановка задачи")

problem = st.text_area(
    "Описание проблемы",
    placeholder="Подробно опишите ситуацию и возникшую проблему...",
    height=120
)

object_name = st.text_input(
    "Объект",
    placeholder="Например: металлическая конструкция"
)

useful_action = st.text_input(
    "Какую полезную функцию должен выполнять объект?",
    placeholder="Например: выдерживать большую нагрузку"
)

undesired_effect = st.text_area(
    "Что мешает получить нужный результат?",
    placeholder="Например: увеличение прочности приводит к увеличению веса",
    height=90
)

goal = st.text_area(
    "Желаемый результат",
    placeholder="Например: уменьшить вес, сохранив прочность",
    height=90
)

st.markdown("---")

st.header("2. Дополнительные условия")

constraints = st.text_area(
    "Ограничения",
    placeholder="Что нельзя менять? Какие есть условия и запреты?",
    height=90
)

resources = st.text_area(
    "Доступные ресурсы",
    placeholder="Какие материалы, детали, энергия или пространство доступны?",
    height=90
)

st.markdown("---")

st.header("3. Анализ задачи")

if st.button("Проанализировать задачу"):

    if not problem.strip() or not object_name.strip():
        st.warning("Заполните описание проблемы и укажите объект.")

    else:
        result = analyze_task(
            problem,
            object_name,
            useful_action,
            undesired_effect,
            goal,
            constraints,
            resources
        )

        st.success("Анализ задачи выполнен!")

        st.subheader("Результаты анализа")

        st.markdown("### 1. Исходная проблема")
        st.write(result["problem_analysis"])

        st.markdown("### 2. Техническое противоречие")
        st.write(result["contradiction"])

        st.markdown("### 3. Идеальный конечный результат (ИКР)")
        st.write(result["ideal_result"])

        st.markdown("### 4. Доступные ресурсы")
        st.write(result["resources"])

        st.markdown("### 5. Ограничения")
        st.write(result["constraints"])

        st.info(
            "Это предварительный анализ. В дальнейшем мы подключим "
            "искусственный интеллект и инструменты ТРИЗ."
        )

st.markdown("---")

st.header("4. Инструменты ТРИЗ")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        "**Противоречия**\n\n"
        "Выявление технических и физических противоречий."
    )

with col2:
    st.info(
        "**ИКР**\n\n"
        "Формулирование идеального конечного результата."
    )

with col3:
    st.info(
        "**40 принципов**\n\n"
        "Использование изобретательских принципов."
    )

st.markdown("---")

st.caption("TRIZ AI Assistant | Первая версия проекта")
