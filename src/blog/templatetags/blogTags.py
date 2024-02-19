from django import template
import os

register = template.Library()
COMPONENTS_DIR = "blog/components/"


@register.inclusion_tag(os.path.join(COMPONENTS_DIR, "toggleThemeComponent.html"))
def toggleTheme():
  return


@register.inclusion_tag(os.path.join(COMPONENTS_DIR, "asideLayoutComponent.html"))
def asideLayout(popularPosts, *args, **kwargs):
  data = {
    'popularPosts': popularPosts,
  }
  return data


@register.inclusion_tag(os.path.join(COMPONENTS_DIR, "postComponent.html"))
def post(post, tags, *args, **kwargs):
  
  data = {
    'post': post,
    'tags': tags,
  }
  
  return data
