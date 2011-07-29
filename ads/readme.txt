
Ads module
==========

Purpose:

Allows "Page ads" to be created and displayed in slots on the home page.
Allows random page ads to show on pages.


Dependencies:
  - Thumbnails
  - Styler


Install:
  - Define ADS_SLOTS and ADS_SLOTSETS in settings.py
  - Symlink site_media to use standard css
  - Include template dir to use page_ads.html


Use:
    {% load ads_tags %}
    {% prepare_ad_slots %}  - allocates ads to slots and attaches to the request object (naughty)
    {% for ad in request.ads.slot_sets.name_of_slotset %}
        {% include 'ads/includes/page_ads.html' %}
    {% endfor %}


