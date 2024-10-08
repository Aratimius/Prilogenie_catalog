from django.core.cache import cache

from config.settings import CASHE_ENABLED


def get_objects_from_cache(model):
    """Получить данные по модели из кеша, если кеш пуст, то из БД"""
    if not CASHE_ENABLED:
        return model.objects.all()
    key = f"{model}_list"
    objects = cache.get(key)
    if objects is not None:
        return objects
    objects = model.objects.all()
    cache.set(key, objects)
    return objects

