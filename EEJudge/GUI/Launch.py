# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/06
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import gradio as gr
from typing import Any
from EEJudge.GUI import Information as information
from EEJudge.Judge.Judge import get_code
from EEJudge.ChatBot.Chat import respond
from EEJudge.Utils.Listener import background_listener

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
            with gr.Row():
                with gr.Column():
                    gr.Markdown(
                        "Question Descriptions"
                    )
                    selected_question_name = gr.Dropdown(
                        label="Select Question", 
                        value="Q1",
                        choices=[
                            "Q1",
                            "Q2"
                        ],
                        interactive=True,
                    )

                    test_word = gr.Markdown(
                        """\
                        ### Q1
                        
                        print("Hello World")
                        """, 
                        visible=True,
                    )
                with gr.Column():
                    chatbot = gr.Chatbot(
                        label="EE Chat",
                        show_label=True,
                    )
                    msg = gr.Textbox()
                    clear = gr.ClearButton([msg, chatbot])
                    msg.submit(respond, [msg, chatbot], [msg, chatbot])

            txt = gr.Textbox(
                label="Paste Your code here", 
            )

            txt_3 = gr.Textbox(
                label="Your code results"
            )

            btn = gr.Button(value="Submit")
            btn.click(get_code, inputs=[txt], outputs=[txt_3])            

        with gr.Tab("Submitted History"):
            gr.Markdown(
                "We will record the submitted history in the future..."
            )

        with gr.Tab("Judge Mechanism"):
            gr.Markdown(
                "We will record the judge mechanism in the future..."
            )

        background_listener(
            selected_question_name,
            test_word
        )

    return demo
