from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

import datetime


class Category(models.Model):
    """Category model"""
    title = models.CharField(_('title'), max_length=100, unique=True)
    slug = models.SlugField(_('slug'), unique=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('title',)

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('blog_category_detail', kwargs={'slug': self.slug})


class Post(models.Model):
    """Post model"""
    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public'))
    )

    title = models.CharField(_('title'), max_length=200, unique=True)
    slug = models.SlugField(_('slug'), unique_for_date='published')
    body = models.TextField(_('body'))
    status = models.IntegerField(_('status'),
                                 choices=STATUS_CHOICES, default=1)
    published = models.DateTimeField(_('published'),
                                     default=datetime.datetime.now)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    categories = models.ManyToManyField('Category', blank=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ('-published',)
        get_latest_by = 'published'

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('blog_post_detail',
                       kwargs={
                       'slug': self.slug,
                       'year': self.published.year,
                       'month': self.published.strftime('%b').lower(),
                       'day': self.published.day
                       }
        )
