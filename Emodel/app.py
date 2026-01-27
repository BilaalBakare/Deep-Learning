import gradio

def randomfunc(name):
    return f"Hello {name}, Greetings from Bilaal"

demo = gradio.interface(
    fn=randomfunc,
    inputs=gradio.Textbox(label='Your name'),
    outputs=gradio.Textbox(label="Greeting"),
    title="Greeting App",
    description="Enter your name to get a greeting"
)

demo.launch()