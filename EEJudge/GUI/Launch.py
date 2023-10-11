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

def test(selected_question_name):
    if selected_question_name == "Q1":

        test_word = gr.Markdown(
            """\
            ### Q1
            
            print("Hello World")
            """,  
            visible=True,
        )
    elif selected_question_name == "Q2":
        test_word = gr.Markdown(
            "### Q2", 
            visible=True,
        )
    
    return test_word

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
                    chatbot = gr.Chatbot()
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

        selected_question_name.change(
            fn=test,
            inputs=selected_question_name,
            outputs=test_word,
        )
            
    demo.launch(
        # enable_queue=True,
        # share=True, 
        server_name="127.0.0.1", 
        server_port=6006,
        debug=True,
    )
