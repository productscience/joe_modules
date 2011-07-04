from django.conf import settings


#NAMESPACE (can change from "BLOG_" in case already used)
ns = getattr(settings, "JOE_DJANGO_BLOG_NAMESPACE", "BLOG") + "_"


# Used for assigning an author to blog entries
# Must have "first_name" and "last_name" attributes
USER_MODEL = getattr(settings, ns + "USER_MODEL", "auth.User")

# The number of posts to show on the home page
N_HOME_POSTS = getattr(settings, ns + "N_HOME_POSTS", 10)

