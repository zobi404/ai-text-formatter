import markdown
import re

def markdown_to_html(text):
    text = re.sub(r'\s+\n', '\n', text).strip()

    return markdown.markdown(
        text,
        extensions=[
            "extra",
            "sane_lists",
            "nl2br",
            "tables",
            "fenced_code"
        ]
    )
