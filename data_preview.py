"""Generate a LaTeX table preview of data with optional language support."""

from datetime import datetime
from typing import Iterable, Mapping

CAPTION_TRANSLATIONS = {
    "English": "Data Preview",
    "Português (Brasil)": "Pré-visualização dos dados",
}

ROW_END = " " + "\\\\"

def save_latex_preview(data: Iterable[Mapping[str, object]], latex_language: str = "English") -> str:
    """Save a simple LaTeX table preview of ``data``.

    Parameters
    ----------
    data:
        Iterable of mapping objects representing table rows.
    latex_language:
        Language used to translate the caption. If the value is
        ``"Português (Brasil)"``, the caption is translated; otherwise the
        English caption is used.

    Returns
    -------
    str
        The name of the generated LaTeX file.
    """
    rows = list(data)
    if not rows:
        raise ValueError("data must contain at least one row")

    headers = list(rows[0].keys())
    caption = CAPTION_TRANSLATIONS.get(latex_language, CAPTION_TRANSLATIONS["English"])

    latex_lines = ["\\begin{table}[ht]", "\\centering", f"\\caption{{{caption}}}"]
    column_spec = " | ".join(["l"] * len(headers))
    latex_lines.append(f"\\begin{{tabular}}{{{column_spec}}}")
    latex_lines.append("\\hline")
    latex_lines.append(" & ".join(headers) + ROW_END)
    latex_lines.append("\\hline")
    for row in rows:
        values = [str(row.get(h, "")) for h in headers]
        latex_lines.append(" & ".join(values) + ROW_END)
    latex_lines.append("\\hline")
    latex_lines.append("\\end{tabular}")
    latex_lines.append("\\end{table}")

    filename = f"data_preview_{datetime.now().strftime('%Y%m%d')}.tex"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(latex_lines))

    return filename

if __name__ == "__main__":
    example_data = [{"Name": "Alice", "Age": 30}, {"Name": "Bob", "Age": 25}]
    print(save_latex_preview(example_data, latex_language="Português (Brasil)"))
