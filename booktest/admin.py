from django.contrib import admin
from bookTest.models import BookInfo, HeroInfo


# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    '''模型后台管理类'''
    list_display = ['id', 'btitle', 'bpub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    # 根据gender的值判断性别
    def gethgender(self, instance):
        return "男" if instance.hgender is True else "女"
    # 显示主人公所在的书名
    def getBtitle(self, instance):
        return instance.hbook.btitle

    list_display = ['id', 'hname', 'gethgender', 'hcomment', 'getBtitle']
    fields = ['编号', '姓名', '性别', '独门绝技', '武侠著作']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
