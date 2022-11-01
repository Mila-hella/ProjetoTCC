from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_year(value):
    if value < 0:
        raise ValidationError(
            _("Valores negativos não são permitidos.")
        )