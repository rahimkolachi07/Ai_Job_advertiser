import gradio as gr
from gemini.gemini import g_model
def model(Company_Name,Job_Title,Location,Salary_Description,What_does_your_company_do,Role_Description):
    txt=g_model(f"you are job advertiser. write an job advertisement post. these are basic details of job={Company_Name}, {Job_Title},{Location},{Salary_Description},{What_does_your_company_do},{Role_Description}, write with heading and sub headings")
    return txt
app=gr.Interface(fn=model,inputs=["text","text","text","text","text","text"],outputs="text")
app.launch(share=True)
