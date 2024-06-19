from django_components import component


@component.register("heading")
class Heading(component.Component):
    template_name = "heading/template.html"

    def get_context_data(self, content):
        return {
            "content": content,
        }

    class Media:
        css = "heading/style.css"
        js = "heading/script.js"
