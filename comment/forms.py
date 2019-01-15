from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from ckeditor.widgets import CKEditorWidget
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.CharField(widget=forms.HiddenInput)
    text = forms.CharField(widget=CKEditorWidget(config_name='comment_ckeditor'))

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(CommentForm, self).__init__(*args, **kwargs)
    def clean(self):
        #判斷用戶是否登錄
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用戶尚未登錄')
        #評論對象驗證
        content_type = self.cleaned_data['content_type']
        object_id = self.cleaned_data['object_id']
        text = self.cleaned_data['text']
 
        try:
            model_class = ContentType.objects.get(model=content_type).model_class() #取得模型中的評論方法
            model_obj = model_class.objects.get(pk=object_id) #取得評論對應的編號
            self.cleaned_data['content_object'] = model_obj
        except ObjectDoesNotExist: #若對象不存在
            raise forms.ValidationError('評論對象不存在')
 
        return self.cleaned_data 