from enum import Enum
from typing import Mapping
from markupsafe import Markup
from flask import Flask


class Editor(Enum):
    """Enum representing the CKEditor5 CDN options

    :param Enum: built-in enum type
    :type Enum: generic enumeration
    """
    Classic = 0
    Inline = 1
    Balloon = 2
    BalloonBlock = 3
    Document = 4


class CKEditor5(object):

    def __init__(self, app: Flask = None) -> None:
        """Initialise the flask module

        :param app: current app context, defaults to None
        :type app: Flask, optional
        """
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Factory app pattern initialiser

        :param app: the flask app context
        :type app: Flask
        """
        pass

    def load(self, url: str = None, editor: Editor = Editor.Classic) -> Markup:
        """Generates the script src

        :param url: location of the static js, defaults to None
        :type url: str, optional
        :param editor: CKEditor5 build option, defaults to Editor.Classic
        :type editor: Editor, optional
        :return: script tag
        :rtype: Markup
        """
        if url is None:
            url = self.CDN_5.format(self.resource[editor])

        return Markup(f"<script src=\"{url}\"></script>")

    def config(self, editor: Editor = Editor.Classic) -> Markup:
        """Generates the editor instantiation script

        :param id: DOM `id` attribute, defaults to 'editor'
        :type id: str, optional
        :param editor: CKEditor5 build option, defaults to Editor.Classic
        :type editor: Editor, optional
        :return: activation script
        :rtype: Markup
        """
        return Markup(
            f"""
            <script>
                {self.jsobject[editor]}
                    .create( document.querySelector( '.ckeditor' ) )
                    .catch( error => {{
                        console.error( error );
                    }} );
            </script>
            """
        )

    # cdn url
    CDN_5 = "https://cdn.ckeditor.com/ckeditor5/24.0.0/{0}/ckeditor.js"

    # url mappings
    resource: Mapping[Editor, str] = {
        Editor.Classic: 'classic',
        Editor.Inline: 'inline',
        Editor.Balloon: 'balloon',
        Editor.BalloonBlock: 'balloon-block',
        Editor.Document: 'decoupled-document',
    }
    # js mappings
    jsobject: Mapping[Editor, str] = {
        Editor.Classic: 'ClassicEditor',
        Editor.Inline: 'InlineEditor',
        Editor.Balloon: 'BalloonEditor',
        Editor.BalloonBlock: 'BalloonEditor',
        Editor.Document: 'DecoupledEditor',
    }
