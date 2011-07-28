from django.conf import settings


#NAMESPACE (can change from "ADS_" in case already used)
ns = getattr(settings, "JOE_DJANGO_ADS_NAMESPACE", "ADS") + "_"

#SLOTS
example_slots = [   (1, 'Slot 1 - First of small boxes'),
                    (2, 'Slot 2 - Second of small boxes'),  ]
SLOTS = getattr(settings, ns + "SLOTS", example_slots)


#SLOT SETS
example_slot_sets = [   ('home_lhs' , [1,2])  ]
SLOTSETS = getattr(settings, ns + "SLOTSETS", example_slot_sets)


#PRIORITIES
standard_priorities = [     (4, 'Very high'),
                            (3, 'High'),
                            (2, 'Medium'),
                            (1, 'Low'),     ]
PRIORITIES = getattr(settings, ns + "PRIORITIES", standard_priorities)

