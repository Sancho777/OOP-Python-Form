# html_elements.py

from typing import List, Dict, Optional

class HTMLElement:
    def __init__(self, tag: str, attrs: Optional[Dict[str, str]] = None, self_closing=False):
        self.tag = tag
        self.attrs = attrs or {}
        self.children: List['HTMLElement'] = []
        self.self_closing = self_closing

    def set_attr(self, key: str, value: str):
        self.attrs[key] = value

    def add_child(self, child: 'HTMLElement'):
        self.children.append(child)

    def render_attrs(self):
        return ' '.join(f'{key}="{value}"' for key, value in self.attrs.items())

    def render(self):
        attrs = self.render_attrs()
        if self.self_closing:
            return f'<{self.tag} {attrs}/>'.strip()
        inner_html = ''.join(child.render() if isinstance(child, HTMLElement) else str(child) for child in self.children)
        return f'<{self.tag} {attrs}>{inner_html}</{self.tag}>'.strip()


class Input(HTMLElement):
    def __init__(self, input_type="text", **attrs):
        super().__init__('input', attrs, self_closing=True)
        self.set_attr('type', input_type)


class Select(HTMLElement):
    def __init__(self, **attrs):
        super().__init__('select', attrs)

    def add_option(self, text: str, value: Optional[str] = None):
        option = HTMLElement('option')
        option.add_child(text)
        if value:
            option.set_attr('value', value)
        self.add_child(option)


class A(HTMLElement):
    def __init__(self, href: str, text: str, **attrs):
        super().__init__('a', attrs)
        self.set_attr('href', href)
        self.add_child(text)


class Img(HTMLElement):
    def __init__(self, src: str, alt: str = "", **attrs):
        super().__init__('img', attrs, self_closing=True)
        self.set_attr('src', src)
        self.set_attr('alt', alt)


class Div(HTMLElement):
    def __init__(self, **attrs):
        super().__init__('div', attrs)


class Form(HTMLElement):
    def __init__(self, **attrs):
        super().__init__('form', attrs)
