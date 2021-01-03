from enum import Enum
from typing import Mapping
from markupsafe import Markup


class Editor(Enum):
    Classic = 0
    Inline = 1
    Balloon = 2
    BalloonBlock = 3
    Document = 4


class CKEditor5(object):

    def __init__(self, app=None) -> None:
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app) -> None:
        pass

    def load(self, url: str = None, editor: Editor = Editor.Classic) -> Markup:
        if url is None:
            url = f"https://cdn.ckeditor.com/ckeditor5/24.0.0/{self.resource[editor]}/ckeditor.js"

        return Markup(f"<script src=\"{url}\"></script>")

    def config(self, id: str = 'editor', editor: Editor = Editor.Classic) -> Markup:
        return Markup(
            f"""
            <script>
                {self.jsobject[editor]}
                    .create( document.querySelector( '#{id}' ) )
                    .catch( error => {{
                        console.error( error );
                    }} );
            </script>
            """
        )

    resource: Mapping[Editor, str] = {
        Editor.Classic: 'classic',
        Editor.Inline: 'inline',
        Editor.Balloon: 'balloon',
        Editor.BalloonBlock: 'balloon-block',
        Editor.Document: 'decoupled-document',
    }
    jsobject: Mapping[Editor, str] = {
        Editor.Classic: 'ClassicEditor',
        Editor.Inline: 'InlineEditor',
        Editor.Balloon: 'BalloonEditor',
        Editor.BalloonBlock: 'BalloonEditor',
        Editor.Document: 'DecoupledEditor',
    }
