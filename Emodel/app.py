import gradio

def randomfunc(name):
    return f"Hello {name}, Greetings from the Emodel team! We hope you have a great day!"

demo = gradio.Interface(
    fn=randomfunc,
    inputs=gradio.Textbox(label='Your name'),
    outputs=gradio.Textbox(label="Greeting"),
    title="Greeting App",
    description="Enter your name to get a greeting"
)

demo.launch()