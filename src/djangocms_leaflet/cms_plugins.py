from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _

from djangocms_leaflet.models import Map, Marker
from djangocms_leaflet.models import ListOfMarkers


@plugin_pool.register_plugin
class MapPublisher(CMSPluginBase):
    """Leaflet Map"""
    model = Map
    module = 'Leaflet Map'
    name = _('Map')
    render_template = 'djangocms_leaflet/map.html'
    allow_children = True
    child_classes = ['MarkerPublisher', 'ListOfMarkersPublisher']

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin
class MarkerPublisher(CMSPluginBase):
    """Marker for Leaflet Map"""
    model = Marker
    module = 'Leaflet Map'
    name = _('Marker')
    render_template = 'djangocms_leaflet/marker.html'
    require_parent = True
    parent_classes = ['MapPublisher']
    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin
class ListOfMarkersPublisher(CMSPluginBase):
    """Marker for Leaflet Map"""
    model = ListOfMarkers
    module = 'Leaflet Map'
    name = 'List of Markers'
    render_template = 'djangocms_leaflet/markerList.html'
    require_parent = True
    parent_classes = ['MapPublisher']
    allow_children = False

    def render(self, context, instance, placeholder):
        marks = instance.markers_json
        context.update({'marks': marks})
        return context

