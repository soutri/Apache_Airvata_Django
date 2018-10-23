from tastypie.resources import ModelResource
from api.models import FileNames
from tastypie.authorization import Authorization

class FileResource(ModelResource):
    class Meta:
        queryset = FileNames.objects.all()
        resource_name = 'file'
        authorization = Authorization()

    def dehydrate(self, bundle):
        # If they're requesting their own record, add in their email address.
        if bundle.request.user.pk == bundle.obj.pk:
            # Note that there isn't an ``email`` field on the ``Resource``.
            # By this time, it doesn't matter, as the built data will no
            # longer be checked against the fields on the ``Resource``.
            bundle.data['fileName'] = bundle.obj.fileName
            print(bundle)
        return bundle
