from flask import Blueprint, request, render_template, g, redirect, url_for, flash
from .forms import QuestionForm, AnswerForm
from models import QAModel, AnswerModel
from exts import db
from decorators import login_required

bp = Blueprint("qa", __name__, url_prefix="/")


# http://127.0.0.1:5000
@bp.route("/")
def index():
    questions = QAModel.query.order_by(QAModel.create_time.desc()).all()
    return render_template("index.html", questions=questions)


@bp.route("/publish", methods=["GET", "POST"])
@login_required
def publish_question():
    if request.method == "GET":
        return render_template("publish_question.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QAModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            # todo：跳转到详情页
            return redirect("/")
        else:
            print(form.errors)
            return redirect(url_for('qa.publish_question'))


@bp.route("/detail/<int:qa_id>")
def qa_detail(qa_id):
    question = QAModel.query.get(qa_id)
    if not question:
        flash("问题不存在")
        return redirect(url_for('qa.index'))

    # 获取该问题的所有答案，按时间排序
    answers = AnswerModel.query.filter_by(question_id=qa_id).order_by(AnswerModel.create_time.asc()).all()

    return render_template("detail.html", question=question, answers=answers)


@bp.route("/answer/publish", methods=['POST'])
@login_required
def publish_answer():
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        question_id = form.question_id.data
        answer = AnswerModel(content=content, question_id=question_id, author=g.user)
        db.session.add(answer)
        db.session.commit()
        flash("回答发布成功！")
        return redirect(url_for('qa.qa_detail', qa_id=question_id))
    else:
        print(form.errors)
        flash("回答发布失败，请检查内容")
        return redirect(url_for('qa.qa_detail', qa_id=request.form.get("question_id")))


@bp.route("/search")
def search():
    q = request.args.get('q')

    if q and q.strip():
        search_term = f"%{q.strip()}%"  # 使用通配符
        questions = QAModel.query.filter(
            QAModel.title.like(search_term) |
            QAModel.content.like(search_term)
        ).order_by(QAModel.create_time.desc()).all()
    else:
        questions = []
        flash("请输入搜索关键词")

    return render_template("index.html", questions=questions, search_query=q)