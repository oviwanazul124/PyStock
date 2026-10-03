from pystock.models.save_search_mode import search_mode
from pystock.services.save_service import get_full_view

def filter_by(mode : search_mode, type : str, exact_filtrer=0 ,min_filtrer=0, max_filtrer=0) -> list:

    full_view = get_full_view()
    filtered_items = []

    if mode == search_mode.EXACT:
        for id in full_view.keys():
            if getattr(full_view[id], type) == int(exact_filtrer):
                filtered_items.append(full_view[id])

    elif mode == search_mode.MIN:
        for id in full_view.keys():
            if getattr(full_view[id], type) >= int(min_filtrer):
                filtered_items.append(full_view[id])

    elif mode == search_mode.MAX:
        for id in full_view.keys():
            if getattr(full_view[id], type) <= int(max_filtrer):
                filtered_items.append(full_view[id])

    return filtered_items