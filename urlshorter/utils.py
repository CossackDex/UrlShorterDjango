from django.conf import settings

import os
from pyblake2 import blake2b, BLAKE2B_SALT_SIZE

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)


def create_random_url(model_instance):
    model_class = model_instance.__class__
    random_part = blake2b(digest_size=SIZE, salt=os.urandom(BLAKE2B_SALT_SIZE)).hexdigest()

    if model_class.objects.filter(short_url=random_part).exists():
        return create_random_url(model_instance)
    return random_part
