import datastore


def process_and_store(key, raw_value):
    raw_value = raw_value.strip().upper()
    datastore.store_value(key, raw_value)
    return raw_value


def retrieve_processed(key):
    value = datastore.get_value(key)
    return value.lower() if value is not None else None


def update_value(key, raw_value):
    process_and_store(key, raw_value)


def delete_value(key):
    return datastore.delete_value(key)


def list_all_keys():
    return datastore.list_keys()
