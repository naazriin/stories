from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify


from recipes.models import Reciepes

# @receiver(pre_save, sender=Reciepes)
# def create_slug(sender, instance, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.title)
#         instance.save()

@receiver(post_save, sender=Reciepes)
def create_slug(sender, instance, created, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()
