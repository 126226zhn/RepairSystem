

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    nickname = models.CharField(max_length=50, null=True, verbose_name='用户昵称')
    mobile = models.CharField(max_length=11, null=True, verbose_name='电话')
    upassword=models.CharField(max_length=20,null=True, verbose_name='密码')
    address = models.CharField(max_length=100, null=True, verbose_name='住址')
    sex = models.CharField(max_length=10, null=True, verbose_name='性别')
    # head_img = models.ImageField(upload_to='%Y/%m', verbose_name='头像', null=True)

    """
    用户等级表：
    0- 普通用户
    1- 维修工程师
    2- 客服
    """
    roles = models.IntegerField(default=0, null=True,verbose_name='用户等级')

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
#工单表
class RepairFormModel(models.Model):
    repairform_num=models.CharField(max_length=50,null=True,verbose_name='报修单号')
    custom= models.CharField(max_length=50, null=True, verbose_name='客户名称')
    custom_mobile = models.CharField(max_length=11, null=True, verbose_name='报修人电话')
    electric_type=models.CharField(max_length=20,null=True,verbose_name='电器种类')
    electric_brand=models.CharField(max_length=20,null=True,verbose_name='电器品牌')
    description=models.CharField(max_length=100,null=True,verbose_name='损坏情况描述')
    repair_address=models.CharField(max_length=50,null=True,verbose_name='报修地址')
    report_order_time=models.DateTimeField(null=True,verbose_name='报修时间',auto_now_add=True)
    #添加 可预约维修时间
    order_time=models.CharField(max_length=20, null=True, verbose_name='预约时间')
    #repair_status报修状态(未派单、已派单、未完成、已完成)  客户评价
    repair_status=models.CharField(max_length=20,verbose_name='报单状态')
    
    #根据地址匹配工程师
    repair_people=models.CharField(max_length=20,null=True,verbose_name="工程师")
    repair_mobile = models.CharField(max_length=11, null=True, verbose_name='工程师电话')
    take_address=models.CharField(max_length=50,null=True,verbose_name='工程师负责地址')
    #与用户表关联(一对多)
    user = models.ForeignKey(UserModel,related_name='user',null=True,on_delete=models.CASCADE,verbose_name='用户')
    class Meta:
        db_table = 'repair_form'
        verbose_name = '工单表'
        verbose_name_plural = verbose_name

class AreaInfo(models.Model):
    title=models.CharField(max_length=20)
    parent=models.ForeignKey('self',null=True,blank=True,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dt_area'

