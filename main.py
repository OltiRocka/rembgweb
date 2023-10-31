import io
from rembg import remove
import gradio as gr


def remove_bg(input_image):
    input_bytes = io.BytesIO(input_image)
    output_bytes = remove(input_bytes)
    return output_bytes


def gradio_interface():
    interface = gr.Interface(
        fn=remove_bg,
        inputs=gr.inputs.Image(type="file", label="Upload Image"),
        outputs=gr.outputs.Image(type="file", label="Image without Background"),
        live=True,
        title="Bulk Background Remover",
        description="Upload images to remove their backgrounds.",
    )
    interface.launch()


if __name__ == "__main__":
    gradio_interface()
