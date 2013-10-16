from tastypie.resources import ModelResource
from polls.models import Poll, Choice

# use CSVSerializer
import csv
import StringIO
from tastypie.serializers import Serializer

# test
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404,render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

class CSVSerializer(Serializer):
    formats = ['json', 'jsonp', 'xml', 'yaml', 'html', 'csv']
    content_types = {
        'json': 'application/json',
        'jsonp': 'text/javascript',
        'xml': 'application/xml',
        'yaml': 'text/yaml',
        'html': 'text/html',
        'csv': 'text/csv',
    }

    def to_csv(self, data, options=None):
        options = options or {}
        #data = self.to_simple(data, options)
        data = self.to_simple(data, options)
        d = data
        print data
        print data.keys()
        try:
          d = data['objects']
          keys = d[0].keys()
        except KeyError:
          d = data
          keys = data.keys()

        raw_data = StringIO.StringIO()        
        writer = csv.DictWriter(raw_data, keys, extrasaction='ignore')
        writer.writerows(d)
        
        return raw_data.getvalue()

    def from_csv(self, content):
        raw_data = StringIO.StringIO(content)
        data = []
        # Untested, so this might not work exactly right.
        for item in csv.DictReader(raw_data):
            data.append(item)
        return data
        

class PollResource(ModelResource):
    class Meta:
        queryset = Poll.objects.all()
        allowed_methods = ['get']
        resource_name = 'polls'
        serializer = CSVSerializer(formats=['json', 'csv'])
      
      
        
class ChoiceResource(ModelResource):
    class Meta:
        queryset = Choice.objects.all()
        allowed_methods = ['get']
        resource_name = 'choices'
        serializer = CSVSerializer(formats=['json', 'csv'])
        

        
