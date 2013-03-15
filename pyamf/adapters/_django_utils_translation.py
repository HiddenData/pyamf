# Copyright (c) The PyAMF Project.
# See LICENSE.txt for details.

"""
C{django.utils.translation} adapter module.

@see: U{Django Project<http://www.djangoproject.com>}
@since: 0.4.2
"""

import django
from django.utils.translation import ugettext_lazy

import pyamf


if django.VERSION[0:2] > (1, 4):
    _delegate_bytes = '_delegate_bytes'
    _delegate_text = '_delegate_text'
else:
    _delegate_bytes = '_delegate_str'
    _delegate_text = '_delegate_unicode'


def convert_lazy(l, encoder=None):
    if getattr(l.__class__, _delegate_text):
        return unicode(l)

    if getattr(l.__class__, _delegate_bytes):
        return str(l)

    raise ValueError('Don\'t know how to convert lazy value %s' % (repr(l),))


pyamf.add_type(type(ugettext_lazy('foo')), convert_lazy)
