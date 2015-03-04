import copy

def strip_key_header(text_to_strip, dictionary):
    dict_copy = copy.copy(dictionary)
    for k, v in dictionary.items():
        if k.startswith(text_to_strip):
            new_key = k.replace(text_to_strip, '', 1)
            dict_copy[new_key] = v
            dict_copy.pop(k, None)
    return dict_copy


def get_settings_for(consul, service_name):
    return strip_key_header(
        service_name,
        consul.kv.find(service_name),
    )
