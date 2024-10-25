import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from cloudinary import CloudinaryImage

class CloudinaryAPI():
    def __init__(self, cloud_name, api_key, api_secret):
        cloudinary.config(
            cloud_name = cloud_name, 
            api_key =api_key, 
            api_secret = api_secret,
            secure=True
            )

    def upload_image_to_cloudinary(self, image_path, image_public_id):
        upload_result = cloudinary.uploader.upload(image_path, public_id=image_public_id)
        return upload_result["secure_url"]

    def get_secure_url(self, image_public_id):
        url = cloudinary.utils.cloudinary_url(image_public_id, secure=True)
        return url[0]

    def upscale_image(self, image_public_id):
        tag = CloudinaryImage(image_public_id).image(effect="upscale")
        url = tag.split('''"''')[1]
        return url

    def crop_image(self, image_public_id, crop_width, crop_height):
        auto_crop_url, _ = cloudinary_url(image_public_id, width=crop_width, height=crop_height, crop="auto", gravity="auto")
        return auto_crop_url

    def optimize_image(self, image_public_id):
        optimize_url, _ = cloudinary_url(image_public_id, fetch_format="auto", quality="auto")
        return optimize_url

    def generative_bg_change(self, image_public_id, prompt):
        tag = CloudinaryImage(image_public_id).image(effect=f"gen_background_replace:prompt_{prompt}")
        url = tag.split('''"''')[1]
        return url

    def ai_image_enhance(self, image_public_id):
        tag = CloudinaryImage(image_public_id).image(effect="enhance")
        url = tag.split('''"''')[1]
        return url

    def generative_fill(self, image_public_id):
        tag = CloudinaryImage(image_public_id).image(aspect_ratio="1:1", gravity="center", background="gen_fill", crop="pad")
        url = tag.split('''"''')[1]
        return url

    def content_extraction(self, image_public_id, prompt):
        tag = CloudinaryImage(image_public_id).image(effect=f"extract:prompt_{prompt}")
        url = tag.split('''"''')[1]
        return url

    def round_corners(self, image_public_id, width, radius):
        tag = CloudinaryImage(image_public_id).image(transformation=[
            {'aspect_ratio': "1:1", 'gravity': "auto", 'width': width, 'crop': "auto"},
            {'radius': radius}
            ])
        url = tag.split('''"''')[1]
        return url

    def sharpen_image(self, image_public_id):
        tag = CloudinaryImage(image_public_id).image(effect="sharpen:150")
        url = tag.split('''"''')[1]
        return url

    def generative_replace(self, image_public_id, from_prompt, to_prompt):
        tag = CloudinaryImage(image_public_id).image(effect=f"gen_replace:from_{from_prompt};to_{to_prompt}")
        url = tag.split('''"''')[1]
        return url

    def generative_restore(self, image_public_id):
        tag = CloudinaryImage(image_public_id).image(effect="gen_restore")
        url = tag.split('''"''')[1]
        return url

    def generative_recolor(self, image_public_id, obj, hex_color):
        tag = CloudinaryImage(image_public_id).image(effect=f"gen_recolor:prompt_{obj};to-color_{hex_color}")
        url = tag.split('''"''')[1]
        return url

    def background_removal(self, image_public_id):
        tag = CloudinaryImage(image_public_id).image(effect="background_removal")
        url = tag.split('''"''')[1]
        return url

    def generative_remove(self, image_public_id, prompt):
        tag = CloudinaryImage(image_public_id).image(effect=f"gen_remove:prompt_{prompt}")
        url = tag.split('''"''')[1]
        return url

    def delete_image(self, image_public_id):
        res = cloudinary.uploader.destroy(image_public_id)
        return res
        