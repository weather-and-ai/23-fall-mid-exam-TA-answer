# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/06
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import os
import subprocess
import gradio as gr
from typing import Any
from EEJudge.GUI import Information as information

def get_code(txt):
    with open("tmp.py", "w") as file:
        file.write(txt)

    try:
        output = subprocess.check_output(
            ["python", "tmp.py"], 
            stderr=subprocess.STDOUT, 
            universal_newlines=True,
        )
        print("Script output:")
        print(output)
        return output
    except subprocess.CalledProcessError as e:
        print("Error:", e.output)
        return e.output
    finally:
        os.remove("tmp.py")

def build_eejudge(
        *args: Any, 
        **kwargs: Any,
    ) -> None:

    demo = gr.Blocks(
        title='EE-Judge',
    )

    with demo:
        heading = gr.Markdown(
            information.ee_judge_header
        )

        with gr.Tab("Submit Your Code"):
            heading = gr.Markdown(
                "EE-Judge Test"
            )

            txt = gr.Textbox(
                label="Paste Your code here", 
            )

            txt_3 = gr.Textbox(
                label="Your code results"
            )

            btn = gr.Button(value="Submit")
            btn.click(get_code, inputs=[txt], outputs=[txt_3])

    demo.launch(
        # enable_queue=True,
        # share=True, 
        server_name="127.0.0.1", 
        server_port=6006,
        debug=True,
    )
