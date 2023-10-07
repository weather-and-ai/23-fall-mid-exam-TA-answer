# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/06
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import gradio as gr
from typing import Any
from EEJudge.GUI import Information as information

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

    demo.launch(
        # enable_queue=True,
        # share=True, 
        server_name="127.0.0.1", 
        server_port=6006,
        debug=True,
    )
