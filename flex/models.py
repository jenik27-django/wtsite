from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from streams import blocks
# Create your models here.

class FlexPage(Page):
    """Flexible Page Class"""
    template = "flex/flex_page.html"
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock(classname="text_and_title")),
            ("full_richtext", blocks.RichTextBlock()),
            ("cards", blocks.CardBlock())
        ], 
        use_json_field=True,
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("content"),
    ]