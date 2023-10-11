import os
import gradio as gr
from EEJudge.GUI.Launch import build_eejudge

def build_and_mount_playground(app, playground_name, favicon_file, path):

    if playground_name == "judge":
        playground = build_eejudge()
    else:
        raise ValueError("Invalid playground name")
    
    favicon_path = "." + os.sep + "static" + os.sep + favicon_file
    playground.favicon_path = favicon_path
    app = gr.mount_gradio_app(app, playground, path=path)

    return app
