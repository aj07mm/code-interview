from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from project import settings
from project.apps.data_incubator.forms import UploadImageForm


class UploadImageView(TemplateView):
    template_name = "upload_image.html"

    def post(self, request):
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            my_file = request.FILES['my_file']
            fs = FileSystemStorage()
            filename = fs.save(my_file.name, my_file)
            uploaded_file_url = fs.url(filename)
            return redirect(settings.MEDIA_URL + my_file.name)

        return render(request, self.template_name, {"form": form})
