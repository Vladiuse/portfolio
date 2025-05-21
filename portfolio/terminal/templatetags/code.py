from django import template
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import HtmlLexer, JavascriptLexer, PythonLexer, SqlLexer

register = template.Library()
LEXERS = {
    "python": PythonLexer,
    "sql": SqlLexer,
    "js": JavascriptLexer,
    "html": HtmlLexer,
}


def del_quotes(value: str) -> str:
    value = value.replace('"', "")
    return value.replace("'", "")


def get_colored_code(code, lexer):
    return highlight(code, lexer(encodings="utf-8"), HtmlFormatter())


@register.filter(name="span")
def span_f_letter(value: str) -> str:
    result = []
    for word in value.split():
        result.append(f"<span>{word[0]}</span>" + word[1:])
    return mark_safe(" ".join(result))


@register.tag(name="pixel_screen")
def tetris_screen_highlight(parser, token):
    node = parser.parse(("end",))
    parser.delete_first_token()
    return ScreenHighLight(node)


@register.simple_tag(name="code_style")
def colors(style="dracula"):
    return mark_safe(HtmlFormatter(style=style).get_style_defs(".highlight"))


@register.tag(name="lang")
def lang(parser, token):
    tag_name, lang = token.split_contents()
    lang = del_quotes(lang)
    lexer = LEXERS[lang]
    node = parser.parse(("end",))
    parser.delete_first_token()
    return CodeExaple(node, lexer)


class CodeExaple(template.Node):
    def __init__(self, node, lexer):
        self.node = node
        self.lexer = lexer

    def render(self, context) -> str:
        output = self.node.render(context)
        result = get_colored_code(output, self.lexer)
        return mark_safe(result)


class ScreenHighLight(template.Node):
    def __init__(self, node):
        self.node = node

    def render(self, context) -> str:
        value = self.node.render(context)
        value = value.strip()
        rows = value.split("\n")
        result = ""
        for row in rows:
            pixel_on = "[x]"
            pixel_off = "[ ]"
            pixel_on_tag = '<div class="pixel on"><div>%s</div></div>'
            pixel_off_tag = '<div class="pixel"><div>%s</div></div>'
            row = row.replace(pixel_on, pixel_on_tag)
            row = row.replace(pixel_off, pixel_off_tag)
            result += f'<div class="pixel-line">{row}</div>'
        return mark_safe(result)


@register.inclusion_tag("terminal/slider.html")
def slider(poll) -> dict:
    images = poll.image_set.all()
    return {"images": images}
