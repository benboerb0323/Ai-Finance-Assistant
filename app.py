from flask import Flask,render_template,request,redirect,url_for,session,flash
from openai import OpenAI
from dotenv import load_dotenv
import os
from database import init_db, save_chat, get_chat_history, delete_all_history, delete_history_by_id, search_chat_history, get_history_count, get_history_by_id

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
    save_chat(question, ai_text)
    return ai_text


@app.route("/",methods=["GET","POST"])
def home():
    
    result =  []
    
    user_input = ""

    messages = get_messages()

    if request.method == "POST":

        user_input = request.form.get("user_input", "").strip()

        if not user_input:
            flash("请输入问题", "error")
            return redirect(url_for("home"))

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

    flash("聊天记录已清除", "success")

    return redirect(url_for("home"))



@app.route("/history")
def history():

    keyword = request.args.get("keyword", "").strip()

    page = request.args.get("page", 1, type=int)

    per_page = 10

    if keyword:
        history_records = search_chat_history(keyword)
        history_count = len(history_records)
        total_count = history_count
        total_pages = 1
    else:
        total_count = get_history_count()
        total_pages = (total_count + per_page - 1) // per_page

        if total_pages == 0:
            total_pages = 1

        if page < 1:
            page = 1

        if page > total_pages:
            page = total_pages

        history_records = get_chat_history(page=page, per_page=per_page)
        history_count = len(history_records)



    return render_template(
        "history.html",
        history_records=history_records,
        keyword=keyword,
        history_count=history_count,
        total_count=total_count,
        total_pages=total_pages,
        page=page
    )


@app.route("/history/<int:record_id>")
def history_detail(record_id):

    record = get_history_by_id(record_id)

    if record is None:
        return "Record not found", 404

    return render_template(
        "history_detail.html",
        record=record
    )






@app.route("/delete_history", methods=["POST"])
def delete_history():

    delete_all_history()

    flash("所有历史记录已删除", "success")

    return redirect(url_for("history"))


@app.route("/delete_history/<int:record_id>", methods=["POST"])
def delete_history_record(record_id):

    delete_history_by_id(record_id)

    flash("该条历史记录已删除", "success")

    return redirect(url_for("history"))

if __name__ == "__main__":
    app.run(debug=True)