import qrcode
from PIL import Image

# 生成二维码
def create_qrcode(url, output_filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=3,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # 保存二维码图片
    img.save(output_filename)
    return img

# 将二维码添加到指定图片上
def add_qrcode_to_image(qrcode_img, target_img_path, output_img_path):
    qr_img = qrcode_img
    target_img = Image.open(target_img_path)

    # 确定二维码的大小和位置
    qr_width, qr_height = qr_img.size
    target_width, target_height = target_img.size
    qr_x = target_width - qr_width - 1384  # 距离右边10像素
    qr_y = target_height - qr_height - 870  # 距离底部10像素

    # 将二维码图片粘贴到目标图片上
    target_img.paste(qr_img, (qr_x, qr_y))

    # 保存最终图片
    target_img.save(output_img_path)

# 使用函数
url = "https://openxlab.org.cn/models/InternLM/subject/certificate/InternLM-C2-S4922"
qrcode_img = create_qrcode(url, 'qrcode.png')
add_qrcode_to_image(qrcode_img, 'certificate.png', 'certificate_with_qrcode.png')