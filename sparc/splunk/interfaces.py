from zope import interface
from zope.interface.common import mapping
from zope import schema
from splunklib import client

class ISplunkQuery(interface.Interface):
    """A Splunk query"""
    query = schema.Text(
            title=_(u"Splunk query string"),
            description=(u"A query to find events"),
            required = True
            )

class ISplunkResultsStream(interface.Interface):
    """A Splunk job results stream handle"""
    def read():
        """Reads stream and advances pointer"""

class ISplunkJob(interface.Interface):
    """Marker for splunklib.client.Job"""
interface.classImplements(client.Job, ISplunkJob)

class ISplunkSavedSearches(interface.Interface):
    """Marker for splunklib.client.SavedSearches"""
interface.classImplements(client.SavedSearches, ISplunkSavedSearches)

class ISplunkSavedSearch(interface.Interface):
    """Marker for splunklib.client.SavedSearch"""
interface.classImplements(client.SavedSearch, ISplunkSavedSearch)

class ISplunkConnectionInfo(mapping.IFullMapping):
    """A Python dict for Splunk connection info. see splunklib.client.connect
    
    Implementers should make sure these objects can be passed into such as
    splunklib.client.connect(**implementation)
    
    Sample implementation:
        >>> from zope import interface
        >>> @interface.implementer(ISplunkConnectionInfo)
        >>> class MySplunkConnInfo(dict):
        ...     pass
    """

class ISplunkSavedSearchQueryFilter(interface.Interface):
    """A Python str for a regex Splunk Saved Search name filer
    
    Sample implementation:
        >>> from zope import interface
        >>> @interface.implementer(ISplunkSavedSearchQueryFilter)
        >>> class MySplunkSavedSearchQueryFilter(str):
        ...     pass
        
    """

class ISplunkKVCollectionSchema(mapping.IFullMapping):
    """A Dict-based Splunk KV Collection schema definition
    
    This should be a Python dict whose keys are strings that define Splunk
    KV collection field names and values define that fields Splunk data type.
    Other non-attribute fields may be defined as well in the same manor (such
    as accelerated_fields, etc).
    
    
    Sample implementation:
        >>> from zope import interface
        >>> @interface.implementer(ISplunkKVCollectionSchema)
        >>> class MySplunkKVSchema(dict):
        ...     pass
    """

class ISPlunkKVCollectionIdentifier(interface.Interface):
    """An identifier for a Splunk KV Collection end point"""
    collection = schema.TextLine(title=u"Collection Name")
    application = schema.TextLine(title=u"Splunk Application Name")
    username = schema.TextLine(title=u"Splunk Associated User Name")