from django.contrib import admin
from .models import Question

admin.site.register(Question)
#フォームは Question モデルから自動的に生成されます。
#モデルのフィールドの型 (DateTimeField 、 CharField など) はそれぞれ異なる HTML 入力ウィジェットと対応しています。各種のフィールドは、自分自身を Django admin サイトでどう表示するか知っています。
#各 DateTimeField は JavaScript ショートカットがついています。日付 (dates) のカラムには「今日 (today)」 へのショートカットとカレンダーポップアップボタンがあります。 時刻 (times) には「現在 (now)」へのショートカットと、よく入力される時刻のリストを表示するポップアップボタンがあります。

#ページ末ボタンについて
#保存 (Save) – 変更を保存して、このモデルのチェンジリストのページに戻ります。
#保存して編集を続ける (Save and continue editing) – 変更を保存して、このオブジェクトの編集ページをリロードします。
#保存してもう一つ追加 (Save and add another) – 変更を保存して、このモデルのオブジェクトを新規追加するための空の編集ページをロードします。
#削除 (Delete) – 削除確認ページを表示します。