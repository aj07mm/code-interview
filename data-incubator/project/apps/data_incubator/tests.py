from django.test import TestCase
from PIL import Image
import tempfile
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from django.utils.six import BytesIO


class UploadImageTests(TestCase):

    def test_uploading_image_correctly(self):
        client = Client()

        image = Image.new('RGB', (100, 100))

        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)

        response = client.post(
            reverse('data_incubator:upload_image'), 
            {'my_file': tmp_file}, 
            format='multipart',
        )
        
        # redirecting to uploaded file
        assert response.status_code == 302 
