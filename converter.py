from PIL import Image
import os


def convert_to_pdf(img_ids):
    images = [
        Image.open("temp/" + img_id + ".png")
        for img_id in img_ids
    ]

    print("Converting to pdf")
    pdf_path: str = "temp/result.pdf"

    images[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )

    for img_id in img_ids:
        os.remove("temp/" + img_id + ".png")

    return pdf_path


def convert_to_jpg(img_ids):
    print("Converting to jpg")
