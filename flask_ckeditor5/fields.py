from markupsafe import Markup
from wtforms.widgets import TextArea
from wtforms.fields import TextAreaField


class CKTextAreaWidget(TextArea):

    def __call__(self, field: TextAreaField, **kwargs) -> Markup:

        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')

        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()
