''' @File :message.py @Author:张宇 @Date :2020/9/30 15:18 @Desc : '''
from django.shortcuts import render,redirect,reverse
from app.model.messager import Message
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.template.loader import render_to_string
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class Message_list(View):
    TEMPLATE_NAME = 'message/message_list.html'

    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        conversation_user = Message.objects.get_all_conversation(user=user)
        unread_user_list = Message.objects.unread_user_list(user=user)
        data = {
            'user': user,
            'conversation_user': conversation_user,
            'unread_user_list': unread_user_list
        }

        return render(request, self.TEMPLATE_NAME, data)


class Message_Single(View):
    TEMPLATE_NAME = 'message/message_list.html'

    @method_decorator(login_required)
    def get(self, request, username=None):
        user = request.user
        if user.username == username:
            return redirect(reverse('settings'))
        conversation_user = Message.objects.get_all_conversation(user=user)
        unread_user_list = Message.objects.unread_user_list(user=user)
        data = {
            'user': user,
            'unread_user_list': unread_user_list,
            'conversation_user': conversation_user,
            'activeUser': username
        }
        try:
            choose_user = User.objects.get(username=username)
            data['choose'] = choose_user
        except:
            raise Http404
        if choose_user not in conversation_user:
            data['first'] = True
        else:
            data['first'] = False
            conversation_list = Message.objects.get_single_conversation(user, choose_user)
            data['conversation_list'] = conversation_list
        Message.mark_as_read(sender=choose_user,recipient=user)
        return render(request, self.TEMPLATE_NAME, data)


class PostMessage(View):
    @method_decorator(login_required)
    def post(self, request):
        content = request.POST.get('content')
        recipient_username = request.POST.get('recipient')
        if request.user.username == recipient_username:
            raise Http404
        recipient = User.objects.filter(username=recipient_username)
        if not recipient:
            raise Http404
        recipient = recipient[0]
        sender = request.user
        conversation_user = Message.objects.get_all_conversation(user=recipient)

        message = Message.objects.create(sender=sender, recipient=recipient, content=content)

        payload = {
            'type': 'receive',
            'message': render_to_string('message/recipient_message.html', {'user': sender, 'message': message}),
            'sender': sender.username
        }

        if sender not in conversation_user:
            unread_user_list = Message.objects.unread_user_list(user=recipient)
            chat_item = render_to_string('message/chat-item.html',
                                         {'conv_user': sender,'activeUser':None,'unread_user_list':unread_user_list})
            payload['chat_item'] = chat_item
        channel_layer = get_channel_layer()
        sender_message = render_to_string('message/sender_message.html', {'user': sender,'message':message})
        async_to_sync(channel_layer.group_send)(recipient_username, payload)
        return JsonResponse({
            'message': sender_message
        })

@login_required
def mark_as_read(request):
    sender_name = request.POST.get('sender')
    sender = User.objects.filter(username=sender_name)
    recipient = request.user
    if sender:
        Message.mark_as_read(sender[0],recipient)
    raise Http404