# создаем forms.py   (20.03.2019)

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    #sender = StringField('Представьтесь', validators=[DataRequired()]
    title = StringField('Заголовок', validators=[DataRequired()])
    text = TextAreaField('Текст сообщения', validators=[DataRequired()])
    send = SubmitField('Отправить')                                 # 20.03.2019  (что использовать "send" или "submit" см. HTML-шаблон create.html