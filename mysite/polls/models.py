from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    #___Fieldの最初の文字列引数では人間可読のフィールド名を付けることができる
    pub_date=models.DateTimeField("date published")
    def was_published_recently(self):
        return self.pub_date>=timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    #リレーションシップの定義、一つのChoiceと一つのQuestionの関連付け
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

    """
    sqlmigrate コマンドは実際にはデータベースにマイグレーションを実行しません。ただ、Djangoが必要としているSQLが何であるかをスクリーンに表示するだけです。これはDjangoが何をしようとしているかを確認したり、データベース管理者に変更のためのSQLスクリプトを要求されているときに役に立ちます。
    """

    #migrateの手引き
    #1 モデルを変更する (models.py の中の)
    #2 これらの変更のためのマイグレーションを作成するために python3 manage.py makemigrations を実行します。
    #3 データベースにこれらの変更を適用するために python3 manage.py migrate を実行します。
