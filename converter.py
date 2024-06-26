from PIL import Image


def convert_to_pdf(img_ids):
    images = [
        Image.open("temp/" + img_id + ".png")
        for img_id in img_ids
    ]

    pdf_path: str = "temp/result.pdf"

    images[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )

    return pdf_path


def convert_to_jpg(img_ids):
    images = [
        Image.open(f"temp/{img_id}.png").convert('RGB').save(f"temp/{img_id}.jpg")
        for img_id in img_ids
    ]
