import qrcode
from PIL import Image
import gradio as gr

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
def add_qrcode_to_image(qrcode_img, target_img, output_img_path, x, y):
    qr_img = qrcode_img
    
    # 确定二维码的大小和位置
    qr_width, qr_height = qr_img.size
    target_width, target_height = target_img.size
    qr_x = target_width - qr_width - int(x)  # 距离右边10像素
    qr_y = target_height - qr_height - int(y)  # 距离底部10像素

    # 将二维码图片粘贴到目标图片上
    target_img.paste(qr_img, (qr_x, qr_y))

    # 保存最终图片
    target_img.save(output_img_path)

# 将二维码添加到指定图片上，并生成最终图片
def process_image(input_url, target_img, x, y):
    output_filename = "qrcode.png"
    # 生成二维码
    qr_img = create_qrcode(input_url, output_filename)
    
    output_img_path = 'certificate_with_qrcode.png'
    # 将二维码添加到目标图片上
    add_qrcode_to_image(qr_img, target_img, output_img_path, x, y)

    # 打开最终生成的图片，以便 Gradio 可以返回它
    final_img = Image.open(output_img_path)
    
    # 返回图片对象，Gradio 会自动处理图片的展示和下载
    return final_img

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 💬 QR Code Image Processo ")
    gr.Markdown("## 🚀 Enter a URL and the app will generate a QR code and add it to the certificate image.")
    gr.Markdown("### 💪 Power by [InternLM](https://github.com/InternLM), If you like, please click a little ⭐ . ")
    gr.Markdown("x is the distance from the right, y is the distance from the bottom.")
    input_image = gr.Image(type="pil")
    output_image = gr.Image(format="png")
    # 定义 Gradio 界面
    gr.Interface(
        fn=process_image, 
        inputs=["text",input_image,"number","number"], 
        outputs=output_image,
        examples=[[
            "https://openxlab.org.cn/models/InternLM/subject/certificate/InternLM-C2-S4922",
            "certificate.png",
            1384,
            870
        ]])

# 启动应用
demo.launch()