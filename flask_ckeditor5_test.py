import unittest

from markupsafe import Markup

from flask_ckeditor5 import CKEditor5, Editor


class CKEditor5TestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.ckeditor = CKEditor5()

    def test_load(self) -> None:
        script = "<script src=\"{0}\"></script>"

        # Test custom url
        test_custom: Markup = self.ckeditor.load(url='test')
        expect_custom: Markup = Markup(script.format('test'))
        self.assertEqual(test_custom, expect_custom)

        # Test editor url
        cdn = "https://cdn.ckeditor.com/ckeditor5/24.0.0/{0}/ckeditor.js"
        for editor in Editor:
            expected: Markup = Markup(
                script.format(cdn.format(CKEditor5.resource[editor]))
            )
            test: Markup = self.ckeditor.load(editor=editor)
            self.assertEqual(test, expected)

    def test_config(self) -> None:
        expect: Markup = Markup("""
            <script>
                ClassicEditor
                    .create( document.querySelector( '.ckeditor' ) )
                    .catch( error => {
                        console.error( error );
                    } );
            </script>
            """)
        test: Markup = self.ckeditor.config()
        self.assertEqual(test, expect)
