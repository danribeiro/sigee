from django.contrib.formtools.preview import FormPreview
from fonte_emissao.models import FonteEmissao
from django.http import HttpResponseRedirect
class TesteFormPreview(FormPreview):

    def done(self, request, cleaned_data):
        # Do something with the cleaned_data, then redirect
        # to a "success" page.
        return HttpResponseRedirect('/')

