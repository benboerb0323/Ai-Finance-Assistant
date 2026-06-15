from flask import Flask,render_template,request,redirect,url_for,session
from openai import OpenAI
from dotenv import load_dotenv
import os
from database import init_db

load_dotenv()

client=OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

init_db()
def get_messages():

    if "messages" not in session:

        session["messages"] = [
            {
                "role":"system",
                "content":"你是一名专业银行AI助手"
            }
        ]
    
    return session["messages"]



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

    messages = get_messages()

    messages.append(
        {
            "role":"user",
            "content":question
        }
    )
    response=client.chat.completions.create(

        model="deepseek-chat",
        messages=messages
    )
    ai_text = response.choices[0].message.content

    messages.append(
        {
            "role":"assistant",
            "content":ai_text
        }
    )

    session["messages"] = messages
    
    return ai_text


@app.route("/",methods=["GET","POST"])
def home():
    
    result =  []
    
    user_input = ""

    messages = get_messages()

    if request.method == "POST":

        user_input = request.form["user_input"]

        ai_reply(user_input)

        messages = get_messages()


    chat_count = (len(messages) - 1) // 2

    quick_questions = [
        "基金适合长期持有吗",
        "低风险理财推荐",
        "债券基金适合新手吗？",
        "每月工资怎么规划？"
    ]

    return render_template(
        "index.html",
        result=result,
        user_input="",
        messages=messages,
        chat_count=chat_count,
        quick_questions=quick_questions
        )




@app.route("/clear",methods=["POST"])
def clear_chat():

    session["messages"] = [
        {
            "role":"system",
            "content":"你是一名专业银行AI助手"
        }
    ]

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)