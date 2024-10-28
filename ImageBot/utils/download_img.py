import requests


def download_img_cloudinary(url, path):
    res = requests.get(url)
    if res.status_code == 200:
        with open(path, "wb") as f:
            f.write(res.content)
        return path
    else:
        print(res)
