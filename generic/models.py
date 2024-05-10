from django.db import models
from django.utils.translation import gettext_lazy as _


class GenericAPI(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    use_cache = models.BooleanField(_("Use Cache"), default=False)
    cache_time = models.IntegerField(_("Cache Time"), default=0)
    authorization_required = models.BooleanField(_("Authorization Required"), default=False)
    permission_required = models.BooleanField(_("Permission Required"), default=False)
    add_view = models.BooleanField(_("Add View"), default=False)
    list_view = models.BooleanField(_("List View"), default=False)
    detail_view = models.BooleanField(_("Detail View"), default=False)
    update_view = models.BooleanField(_("Update View"), default=False)
    delete_view = models.BooleanField(_("Delete View"), default=False)
    pagination = models.BooleanField(_("Pagination"), default=False)
    counter = models.BooleanField(_("Counter"), default=False)
    throttle = models.BooleanField(_("Throttle"), default=False)
    throttle_time = models.IntegerField(_("Throttle time"), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Generic API")
        verbose_name_plural = _("Generic API")


class GenericAPIField(models.Model):
    class FieldChoices(models.TextChoices):
        TEXT = "char", _("Text field")
        BIG_TEXT = "text", _("Big text field")
        BIG_TEXT_WITH_CKEDITOR = "text_with_ckeditor", _("Big text field with ckeditor")
        BOOLEAN = "boolean", _("Boolean")
        INTEGER = "integer", _("Integer")
        FLOAT = "float", _("Float")
        FILE = "file", _("File")
        IMAGE = "image", _("Image")
        IMAGE_COMPRESSED = "image_compressed", _("Image compressed")
        URL = "url", _("URL")
        DATE = "date", _("Date")
        DATETIME = "datetime", _("Datetime")
        TIME = "time", _("Time")
        EMAIL = "email", _("Email")
        PHONE_NUMBER = "phone_number", _("Phone Number")
        SLUG = "slug", _("Slug")

    api = models.ForeignKey(GenericAPI, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(_("Field name"), max_length=255)
    field_type = models.CharField(_("Field type"), max_length=255, choices=FieldChoices.choices)
    is_searchable = models.BooleanField(_("Is Searchable"), default=False)
    is_filterable = models.BooleanField(_("Is Filterable"), default=False)
    is_hidden_for_admin = models.BooleanField(_("Is Hidden for Admin"), default=False)
    is_lookup = models.BooleanField(_("Is Lookup"), default=False)
