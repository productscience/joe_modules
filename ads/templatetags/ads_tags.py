from django import template
from ads.models import PageAd
register = template.Library()
#import random
from ads.settings import SLOTS, SLOTSETS
from ads.choose import choose
import datetime



@register.tag()
def prepare_ad_slots(parser, token):
    return GetSlotsNode()
class GetSlotsNode(template.Node):
    def render(self, context):
        """
        prepare an 'ads' object and attach to request.
        ads['slot'] = {'slot_name' : ad, 'slot_name' : ad ... }                #implement later??
        ads['slot_sets'] = {'slot_set_name' : [ad, ad, ad ... ], ... }
        """

        today = datetime.date.today()
        
        #get all possible page ads out of the database now (quicker?)
        pageads = PageAd.objects.filter(active_from__lte=today).exclude(active_until__lt=today)
        pinned = list(pageads.filter(pin_to_slot__isnull=False))
        unpinned = list(pageads.filter(pin_to_slot__isnull=True))
        
        class SlotInfo : pass
        slots = {}
        for slot_id, name, fill_random in SLOTS :
            slots[slot_id] = SlotInfo()
            slots[slot_id].name = name
            slots[slot_id].fill_random = fill_random

        #fill slots with ads that want to be pinned
        for slot_id, slot in slots.iteritems() :
            #choose (weighted by priority) from the contenders
            chosen, dummy = choose([(ad,ad.priority) for ad in pinned if ad.pin_to_slot==slot_id], 1)
            slot.ad = chosen[0]
        
        #fill other slots
        for slot_id, slot in slots.iteritems() :
            if not slot.ad :           #not already filled
                if slot.fill_random :        #slot can be filled with random ad
                    chosen, unpinned = choose([(ad,ad.priority) for ad in unpinned], 1)
                    slot.ad = chosen[0]
     
        raise RuntimeError, str( [s.ad for s in slots.values() ] )
      
        #prepare slot lists
        slotset = {}
        for name, slot_ids in SLOTSETS :
            slotset[name] = [ slots[slot_id].ad for slot_id in slot_ids ]

        #attach data to request object -- BAD BEHAVIOUR !! Can't find another way around block scope in templates at the moment
        context['request'].ads = { 'slot_sets' : slotset }

        raise RuntimeError, str(context['request'].ads)

        return ""


@register.inclusion_tag('homepage/ad_list.html')
def ad_list(ads=3, current_page=None):
    
    if type(ads) == type(1) :
        
        ret = []
        
        #get all possible actions and page ads out of the database now (quicker?)
        today = datetime.date.today()
        actions = Action.objects.filter(active_from__lte=today).exclude(active_until__lt=today)
        pageads = PageAd.objects.filter(active_from__lte=today).exclude(active_until__lt=today)
        if type(current_page).__name__ == "Page" :      #CMS fills "current_page" with guff when parsing template prior to editing
            pageads = pageads.exclude(page=current_page)
        avail = list(actions) + list(pageads)
        
        for i in range(ads) :
            #choose (weighted by priority) from the contenders
            chosen, avail = choose([(ad,ad.priority) for ad in avail], 1)
            ret.append(chosen[0])
        
        return {'ads' : ret }
    else :
        return {'ads' : ads }


"""
@register.inclusion_tag('elements/includes/see_also.html')
def see_also(page, n=3):
    return {'page_ads' : get_random_ads(n, exclude=page, news_wins=False) }
"""
