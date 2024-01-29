from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator

MAX_SIZE_7_MB = 3 * 1024 * 2024


def validate_max_size_of_image(value):
    if value.size > MAX_SIZE_7_MB:
        raise ValidationError(f"The size of the image is {value}, it can be a maximum of 7 MB!")


class MaxSizeImageValidator(BaseValidator):
    def clean(self, x):
        return x.size

    def compare(self, img_size, max_size):
        return max_size < img_size
