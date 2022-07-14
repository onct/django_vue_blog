from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    """
    标签 Tag 也比较简单，和 Category 一样。
    再次强调一定要继承 models.Model 类！
    """
    name = models.CharField(max_length=100)


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_by = models.CharField(max_length=128)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)
    user_id = models.BigIntegerField()
    title = models.CharField(max_length=128)
    abb_name = models.CharField(max_length=128)
    content = models.TextField()
    cover = models.CharField(max_length=256)
    order = models.IntegerField()
    status = models.BinaryField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    password = models.CharField(max_length=64)
    comments_num = models.IntegerField()
    like_num = models.IntegerField()
    allow_comment = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
