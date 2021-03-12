# Защита от спама
Модуль позволяет защитить WEB сервис от спама с помощью reCAPTCHA.

## Требования
*   Python: 3.6, 3.7, 3.8, 3.9
*   Django: 2.2, 3.0, 3.1

## Установка
1.  Зарегистрируйтесь в сервисе [reCAPTCHA](https://www.google.com/recaptcha/)
2.  Выполните установку `./setup.py install`
3.  Добавьте `"recaptcha"` в `INSTALLED_APPS` в `settings.py`.
4.  Добавьте настройку `DRF_RECAPTCHA_SECRET_KEY=<секретный ключ>`

```python
INSTALLED_APPS = [
   "recaptcha",
    # ...
]

DRF_RECAPTCHA_SECRET_KEY = "<секретный ключ>"
```

## Использование
```python
from rest_framework.serializers import Serializer, ModelSerializer
from recaptcha.fields import ReCaptchaV2Field, ReCaptchaV3Field
from feedback.models import Feedback


class V2Serializer(Serializer):
    recaptcha = ReCaptchaV2Field()
    ...

class GetOTPView(APIView):
    def post(self, request):
        serializer = V2Serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        ...

class V3Serializer(Serializer):
    recaptcha = ReCaptchaV3Field(action="example")
    ...

class V3WithScoreSerializer(Serializer):
    recaptcha = ReCaptchaV3Field(
        action="example",
        required_score=0.6,
    )
    ...

class FeedbackSerializer(ModelSerializer):
    recaptcha = ReCaptchaV2Field()

    class Meta:
        model = Feedback
        fields = ("phone", "full_name", "email", "comment", "recaptcha")

    def validate(self, attrs):
        attrs.pop("recaptcha")
        ...
        return attrs
```
