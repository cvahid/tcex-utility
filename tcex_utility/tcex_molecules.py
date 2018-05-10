#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Relatively complex functions (known as 'Molecules') performed using the underlying 'Elements'."""

from .tcex_elements import Elements


class Molecules(Elements):
    def __init__(self, owner=None):
        self.owner = owner
        super(Molecules, self).__init__()

    #
    # ADD ATTRIBUTES
    #

    def add_attributes_to_items_by_type(self, attributes, item_type):
        """Add the given attributes to all items of the given type."""
        items = self.get_items(item_type)
        self.add_attributes(attributes, items, item_type)

    def add_attributes_to_items_by_attribute(self, new_attributes, item_type, item_attribute):
        """Add the given attributes to all items of the given type."""
        items = self.get_items_by_attribute(item_attribute, item_type)
        self.add_attributes(new_attributes, items, item_type)

    def add_attributes_to_items_by_sec_label(self, attributes, item_type, item_sec_label):
        """Add the given attributes to all items with the given security label."""
        items = self.get_items_by_sec_label(item_sec_label, item_type)
        self.add_attributes(attributes, items, item_type)

    def add_attributes_to_items_by_tag(self, attributes, item_type, item_tag):
        """Add the given attributes to all items with the given tag."""
        items = self.get_items_by_tag(item_tag, item_type)
        self.add_attributes(attributes, items, item_type)

    #
    # ADD SECURITY LABELS
    #

    def add_sec_labels_to_items_by_type(self, sec_labels, item_type):
        """Add the given security labels to all items of the given type."""
        items = self.get_items(item_type)
        self.add_sec_labels(sec_labels, items, item_type)

    def add_sec_labels_to_items_by_attribute(self, new_sec_labels, item_type, item_attribute):
        """Add the given security labels to all items with the given attribute."""
        items = self.get_items_by_attribute(item_attribute, item_type)
        self.add_sec_labels(new_sec_labels, items, item_type)

    def add_sec_labels_to_items_by_sec_label(self, new_sec_labels, item_type, item_sec_label):
        """Add the given security labels to all items with the given security label."""
        items = self.get_items_by_sec_label(item_sec_label, item_type)
        self.add_sec_labels(new_sec_labels, items, item_type)

    def add_sec_labels_to_items_by_tag(self, new_sec_labels, item_type, item_tag):
        """Add the given security labels to all items with the given tag."""
        items = self.get_items_by_tag(item_tag, item_type)
        self.add_sec_labels(new_sec_labels, items, item_type)

    #
    # ADD TAGS
    #

    def add_tags_to_items_by_type(self, tags, item_type):
        """Add the given tags to all items of the given type."""
        items = self.get_items(item_type)
        self.add_tags(tags, items, item_type)

    def add_tags_to_items_by_attribute(self, new_tags, item_type, item_attribute):
        """Add the given tags to all items with the given attribute."""
        items = self.get_items_by_attribute(item_attribute, item_type)
        self.add_tags(new_tags, items, item_type)

    def add_tags_to_items_by_sec_label(self, new_tags, item_type, item_sec_label):
        """Add the given tags to all items with the given security label."""
        items = self.get_items_by_sec_label(item_sec_label, item_type)
        self.add_tags(new_tags, items, item_type)

    def add_tags_to_items_by_tag(self, new_tags, item_type, item_tag):
        """Add the given tags to all items with the given tag."""
        items = self.get_items_by_tag(item_tag, item_type)
        self.add_tags(new_tags, items, item_type)

    #
    # MISC FUNCTIONS
    #

    def update_attributes_on_items(self, old_attribute, new_attribute, items, items_type):
        """Change the old_attribute to the new_attribute for all of the given items."""
        # if no attribute type is given for the new attribute, assume it is the same type as the old attribute
        if not new_attribute.get('type'):
            new_attribute['type'] = old_attribute['type']

        for item in items:
            attributes = self.get_attributes(item, items_type)
            for attribute in attributes:
                if attribute['type'] == old_attribute['type']:
                    if attribute.get('value'):
                        if attribute['value'] == old_attribute['value']:
                            self.delete_attributes(item, items_type, attribute['id'])
                            self.add_attributes([item], items_type, [new_attribute])
                            break
                        else:
                            pass
                    else:
                        self.delete_attributes(item, items_type, attribute['id'])
                        self.add_attributes([item], items_type, [new_attribute])
                        break
