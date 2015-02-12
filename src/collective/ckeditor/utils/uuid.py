

from Products.CMFCore.utils import getToolByName

try:
    from zope.component.hooks import getSite
except ImportError:
    from zope.app.component.hooks import getSite


def  uuidToURL(uuid):
    portal = getSite()
    reference_catalog = getToolByName(portal, 'reference_catalog')
    obj =  reference_catalog.lookupObject(uuid)
    return obj.absolute_url()
