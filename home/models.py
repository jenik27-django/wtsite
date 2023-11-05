from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import RichTextField




class HomePage(Page):
    """Home page model."""

    templates = "home/home_page.html"
    # makes sure there is only one instance of the homepage
    max_count = 1
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"], blank=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    ) 
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel("banner_image")
    ]