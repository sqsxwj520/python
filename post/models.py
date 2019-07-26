from django.db import models
from user.models import User


class Post(models.Model):
    class Meta:
        db_table = 'post'

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False)  # 文章标题不可以为空
    postdate = models.DateTimeField(null=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT)  # 指定外键，migrate会生成author_id字段
    delete = models.BooleanField(null=False)

    # self.content是Content的实例，其内容是self.content.content

    def __repr__(self):
        return "<Post {} {} {} {}>".format(self.id, self.title, self.postdate, self.content)

    __str__ = __repr__


class Content(models.Model):
    class Meta:
        db_table = "content"

    # 没有主键，会自动创建一个自增主键
    post = models.OneToOneField(Post, primary_key=True, on_delete=models.PROTECT)
    # 一对一，这边会有一个外键post_id引用post.id;models.PROTECT是不允许删除
    content = models.TextField(null=False)
    delete = models.BooleanField(null=False)

    def __repr__(self):
        return "<Content {} {}>".format(self.post.id, self.content[:20])

    __str__ = __repr__
