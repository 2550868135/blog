''' @File :messager.py @Author:张宇 @Date :2020/9/30 14:36 @Desc : '''
from django.db import models
from django.contrib.auth.models import User
import uuid


# 自定义查询集
class MessageQueryset(models.query.QuerySet):
    def get_single_conversation(self, sender, recipient):
        # 获取单个私信的内容
        sender_messages = self.filter(sender=sender, recipient=recipient).select_related('sender', 'recipient')
        recipient_messages = self.filter(sender=recipient, recipient=sender).select_related('sender', 'recipient')
        return sender_messages.union(recipient_messages).order_by('create_time').select_related('sender', 'recipient')

    def get_all_conversation(self, user):
        # 获取所有私信过的用户
        conv_list = []
        recipient = self.filter(sender=user).order_by('create_time').select_related('sender', 'recipient')
        for r in recipient:
            if r.recipient not in conv_list:
                conv_list.append(r.recipient)
        sender = self.filter(recipient=user).order_by('create_time').select_related('sender', 'recipient')
        for s in sender:
            if s.sender not in conv_list:
                conv_list.append(s.sender)
        return conv_list[:6]

    def unread_user_list(self, user):
        # 查看未读的消息
        s = set()
        unread_message = self.filter(recipient=user, unread=True).select_related('sender', 'recipient')
        for m in unread_message:
            s.add(m.sender)
        # 返回的是未读消息的用户列表
        return s

    def has_unread(self):
        unread_list = self.filter(unread=True).select_related('sender', 'recipient')
        if len(unread_list):
            return True
        else:
            return False


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sended_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipiented_messages')
    content = models.TextField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, db_index=True)
    unread = models.BooleanField(default=True, verbose_name='是否未读')

    objects = MessageQueryset.as_manager()

    class Meta:
        verbose_name = "消息"
        verbose_name_plural = verbose_name
        ordering = ("-create_time",)

    @classmethod
    def mark_as_read(cls, sender, recipient):
        unread_message = cls.objects.filter(sender=sender, recipient=recipient, unread=True).select_related('sender','recipient')
        unread_message.update(unread=False)
