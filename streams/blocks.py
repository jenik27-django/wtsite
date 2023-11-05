from wagtail.blocks import CharBlock, TextBlock, StructBlock, RichTextBlock


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
