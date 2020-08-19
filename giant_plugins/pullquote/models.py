from django.db import models
from django.utils.translation import ugettext as _
from filer.fields.image import FilerImageField

from cms.models import CMSPlugin


class PullQuoteBlock(CMSPlugin):
    """
    Block for the quotes to sit in
    """

    pass


class PullQuote(CMSPlugin):
    """
    Model for a pull quote plugin
    """

    quote = models.TextField()
    caption = models.CharField(max_length=255, blank=True)
    image = FilerImageField(
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        help_text=_(
            "Here you can set an optional image to be displayed with the quote"
        ),
    )

    def __str__(self):
        """
        String representation of the object
        """
        return f"Pull quote {self.pk}"
