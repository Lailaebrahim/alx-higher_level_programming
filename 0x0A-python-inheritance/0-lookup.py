def lookup(obj):
        # Get the attributes and methods of the object
    attributes_and_methods = dir( obj )

        # Filter out the built-in methods and attributes
    filtered_attributes_and_methods = [item for item in attributes_and_methods if not item.startswith( "__" )]
    return filtered_attributes_and_methods
