from django.db import models
from django.conf import settings
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200,verbose_name="问题")
    pub_date = models.DateTimeField('提问时间')
    '''
    （失败）
    AutoField1 = models.AutoField(verbose_name="自动字段")
    不能有一个以上自动字段
    BigAutoField1 = models.BigAutoField(verbose_name="长自动字段")
	不能有一个以上自动字段
	BinaryField1 = models.BinaryField(max_length=100,default=None)
	不知道怎么用
	DurationField1 = models.DurationField(verbose_name="时间段字段",default=0)
	不知道怎么用
    '''
    #字段类型
    BigIntegerField1 = models.BigIntegerField(default=0,verbose_name="大整数字段")
    BooleanField1 = models.BooleanField(default=False,verbose_name="布尔字段")
    CharField1 = models.CharField(max_length=5,default="无",verbose_name="字符字段")
    DateField1 = models.DateField('日期字段',default=None)
    DateTimeField1 = models.DateTimeField(auto_now=True,verbose_name="日期时间字段")
    #添加了auto_now=True参数，自动按当期时间记录。
    DecimalField1 = models.DecimalField(max_digits=10, decimal_places=2,default=0,verbose_name="十进制小数字段")
    EmailField1 = models.EmailField(max_length=10,default="wu",verbose_name="电子邮箱字段")
    FileField1 = models.FileField(upload_to='File_home/%Y/%m/%d/',default="没有上传文件。",verbose_name="上传文件字段")
    #文件上传还有更多设置需要测试，以形成完整的功能
    #FilePathField1 = models.FilePathField(path='File_home/', default="无",match=None, recursive=False, max_length=100,verbose_name="文件路径字段")
    #需要更多测试，形成完整功能
    FloatField1 = models.FloatField(default=0,verbose_name="小数字段")
    ImageField1 = models.ImageField(upload_to='File_home/%Y/%m/%d/', height_field=None, width_field=None, max_length=100,default="无",verbose_name="上传图片字段")
    #需要更多测试，形成完整功能
    IntegerField1 = models.IntegerField(default=0,verbose_name="整数字段")
    GenericIPAddressField1 = models.GenericIPAddressField(protocol='both', unpack_ipv4=False ,default="111.111.111.111",verbose_name="IP字段")
    NullBooleanField1 = models.NullBooleanField(verbose_name="空是否选项字段")
    PositiveIntegerField1 = models.PositiveIntegerField(default=337,verbose_name="正整数字段")
    PositiveSmallIntegerField1 = models.PositiveSmallIntegerField(default=1.7,verbose_name="正小数字段")
    SlugField1 = models.SlugField(max_length=10,default="ABC123",verbose_name="标签字段")
    SmallIntegerField1 = models.SmallIntegerField(default=30000,verbose_name="小整数字段")
    TextField1 = models.TextField(default="可输入很长的文本",verbose_name="文本字段")
    #TimeField1 = models.TimeField(default=0,verbose_name="时间字段")
    URLField1 = models.URLField(max_length=200 ,blank=True,verbose_name="URL字段")
    UUIDField1 = models.UUIDField(null=True,blank=True,verbose_name="UUID字段")

    #关系类型
    ForeignKey1 = models.ForeignKey(
        'text_base',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="外键字段"
    	)

    ManyToManyField1 = models.ManyToManyField(
    	"self",
    	blank=True,
    	null=True,
        verbose_name="多对多字段"
        )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="1对1字段"
    	)
    supervisor = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='supervisor_of',
        blank=True,
        null=True,
        verbose_name="1对1字段"
    	)

    class Meta:
        verbose_name='自带控件演示'
        verbose_name_plural='演示清单'

class text_base(models.Model):
    Text_Title = models.CharField(max_length=100,default="无",verbose_name="文章标题",)
    Text_Text = models.TextField(default="可输入很长的文本",verbose_name="文章正文")
    Text_Demo = models.TextField(default="可输入很长的文本",verbose_name="演示代码",null=True,blank=True)
    Text_Image = models.ImageField(upload_to='File_home/%Y/%m/%d/', height_field=None, width_field=None, max_length=100,default="无",verbose_name="上传图片",null=True,blank=True)
    Text_File = models.FileField(upload_to='File_home/%Y/%m/%d/',default="没有上传文件。",verbose_name="上传文件",null=True,blank=True)
    Text_ADD_DateTime = models.DateTimeField(auto_now=True,verbose_name="添加日期")

    class Meta:
        verbose_name='文本管理'
        verbose_name_plural='文本列表'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)