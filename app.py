from flask import Flask,render_template,request
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)



def analyse_financial_needs(user_input):

    result =  []

    if "低风险" in user_input:

        result.append("客户偏好：稳健型")

    if "高收益" in user_input:

        result.append("客户偏好：进取型")

    if "半年" in user_input:

        result.append("推荐期限：6个月")

    if len(result) == 0:

        result.append("暂时无法识别客户需求")
    
    return result


def ai_reply(question):

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(f"""

        你是一名专业银行AI助手。

请用简洁、稳健、专业的语气回答用户问题。

用户问题：
{question}
"""
    )

    return response.text


@app.route("/",methods=["GET","POST"])

def home():
    
    result =  []
    
    user_input = ""


    if request.method == "POST":

        user_input = request.form["user_input"]

        result = [ai_reply(user_input)]


        
    return render_template("index.html",result=result,user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)