from django.core.mail import send_mail


def send_activation_mail(user):
    user.create_activation_code()
    message = f"""Спасибо за регистрацию. Активируйте свой аккаунт по ссылке: http://127.0.0.1:8000/accounts/activation/?u={user.activation_code}"""
    send_mail(
        'Активация аккаунта',
        message,
        'test@my_project.com',
        [user.email,])


#TODO: генерация кода активации create_activation_code()
#TODO: активация
#TODO: логин
#TODO: логаут
#TODO: смена пароля
#TODO: забыли пароль
#TODO: smtp 