"""Собирает doc/catalog.md из файла шаблонов GanievPRO.st.

Запуск из корня репозитория:

    python tools/make_catalog.py

Нужен Python 3.8 или новее, сторонних пакетов нет.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "GanievPRO.st"
TARGET = ROOT / "doc" / "catalog.md"

# Группы верхнего уровня в файле шаблонов и их заголовки в каталоге.
LANGUAGES = {
    "RU": "Русский синтаксис",
    "EN": "Английский синтаксис",
}


def tokenize(text):
    """Режет текст файла .st на скобки, числа и строки."""
    pos = 0
    size = len(text)
    while pos < size:
        char = text[pos]
        if char in "{}":
            yield char
            pos += 1
        elif char == '"':
            pos += 1
            chunks = []
            while True:
                end = text.index('"', pos)
                chunks.append(text[pos:end])
                # Удвоенная кавычка внутри строки означает одну кавычку.
                if text[end + 1 : end + 2] == '"':
                    chunks.append('"')
                    pos = end + 2
                else:
                    pos = end + 1
                    break
            yield ("str", "".join(chunks))
        elif char.isdigit() or char == "-":
            end = pos + 1
            while end < size and text[end].isdigit():
                end += 1
            yield ("num", int(text[pos:end]))
            pos = end
        else:
            pos += 1


def parse(tokens):
    """Собирает вложенные списки из потока лексем."""
    stack = [[]]
    for token in tokens:
        if token == "{":
            stack.append([])
        elif token == "}":
            done = stack.pop()
            stack[-1].append(done)
        else:
            stack[-1].append(token[1])
    return stack[0][0]


def walk(node, path=()):
    """Обходит дерево и отдаёт шаблоны: (путь групп, название, сочетание)."""
    header = node[1]
    name, is_group, _flags, snippet, _body = header
    children = [item for item in node[2:] if isinstance(item, list)]
    if is_group:
        for child in children:
            yield from walk(child, path + (name,))
    else:
        yield path, name, snippet


def cell(text):
    """Готовит текст к ячейке таблицы Markdown."""
    return " ".join(text.split()).replace("|", "\\|")


def code(text):
    """Оформляет сочетание кодом. Пустое сочетание даёт пустую ячейку."""
    text = " ".join(text.split())
    if not text:
        return ""
    return f"`{text}`".replace("|", "\\|")


def build():
    text = SOURCE.read_text(encoding="utf-8-sig")
    # Файл устроен так: {1, {число, {заголовок}, вложенные узлы...}}.
    tree = parse(tokenize(text))[1]
    title = tree[1][0]

    lines = [
        "[Главная](./../README.md)",
        "",
        "# Каталог шаблонов",
        "",
        f"Собран из файла `{SOURCE.name}`: {title}.",
        "",
        "Сочетание это то, что набирается в модуле. Часть в квадратных скобках",
        "набирать не обязательно: для `Проц[едура]` хватит `Проц`. Если на одно",
        "сочетание приходится несколько шаблонов, конфигуратор покажет список на выбор.",
        "Шаблоны без сочетания перетаскиваются в модуль из окна «Шаблоны текста».",
        "",
        "Файл собирает скрипт `tools/make_catalog.py`. Руками его не правят.",
        "",
    ]

    total = 0
    for top in tree[2:]:
        if not isinstance(top, list):
            continue
        top_name = top[1][0]
        if top_name not in LANGUAGES:
            continue

        lines += [f"## {LANGUAGES[top_name]}", ""]
        for group in top[2:]:
            if not isinstance(group, list):
                continue
            rows = list(walk(group))
            if not rows:
                continue
            lines += [
                f"### {group[1][0]}",
                "",
                "| Сочетание | Шаблон | Подгруппа |",
                "| --- | --- | --- |",
            ]
            for path, name, snippet in rows:
                subgroup = " / ".join(path[1:])
                lines.append(f"| {code(snippet)} | {cell(name)} | {cell(subgroup)} |")
                total += 1
            lines.append("")

    lines += ["---", "", "[Назад](./../README.md)", ""]
    TARGET.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"{TARGET.relative_to(ROOT)}: {total} шаблонов")


if __name__ == "__main__":
    build()
