from django.conf import settings
from rest_framework.serializers import CharField

from drf_recaptcha.configurations import (
    get_v3_action_score_from_settings,
    get_v3_default_score_from_settings,
    validate_v3_settings_score_value,
)
from drf_recaptcha.constants import DEFAULT_V3_SCORE
from drf_recaptcha.validators import ReCaptchaV2Validator, ReCaptchaV3Validator


class ReCaptchaV2Field(CharField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.write_only = True

        validator = ReCaptchaV2Validator()
        self.validators.append(validator)


class ReCaptchaV3Field(CharField):
    def __init__(self, action: str, required_score: float = None, **kwargs):
        super().__init__(**kwargs)

        self.write_only = True

        action_score_from_settings = get_v3_action_score_from_settings(action)
        default_score_from_settings = get_v3_default_score_from_settings()
        validate_v3_settings_score_value(required_score, action)

        self.required_score = (
            action_score_from_settings
            or required_score
            or default_score_from_settings
            or DEFAULT_V3_SCORE
        )

        validator = ReCaptchaV3Validator(
            action=action, required_score=self.required_score
        )
        self.validators.append(validator)
