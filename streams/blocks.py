from wagtail.blocks import CharBlock, TextBlock, StructBlock, RichTextBlock, ListBlock, PageChooserBlock
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(StructBlock):
    """Title and text and nothing else"""
    title = CharBlock(required=True, help_text="Add your title")
    text = TextBlock(required=True, help_text="Add additional text")

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class RichTextBlock(RichTextBlock):
    """Rich text with all the features"""
    class Meta:  # noqa
        template = "streams/rich_text_block.html"
        icon = "doc-full"
        label = "Full RichText"

class CardBlock(StructBlock):
    title = CharBlock(required=True, help_text="Add your title")
    cards = ListBlock(
        StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", CharBlock(required=True, max_length=40)),
                ("text", TextBlock(required=True, max_length=200)),
                ("button_page", PageChooserBlock(required=False)),
                ("button_url", CharBlock(required=False, help_text="If button page above is selected, that will be used first.")),
            ]
        )
    )
    class Meta:  # noqa
        template = "streams/card_block.html"
        icon = "doc-full"
        label = "Staff Cards"