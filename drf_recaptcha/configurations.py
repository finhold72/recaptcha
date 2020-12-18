from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def validate_v3_settings_score_value(value: int or float or None, action: str = None):
    if value is None:
        return

    if not isinstance(value, (int, float)):
        if action:
            message = f"Score value for action '{action}' should be int or float"
        else:
            message = "Default score value should be int or float"

        raise ImproperlyConfigured(message)

    if value < 0.0 or 1.0 < value:
        if action:
            message = f"Score value for action '{action}' should be between 0.0 - 1.0"
        else:
            message = "Default score value should be between 0.0 - 1.0"

        raise ImproperlyConfigured(message)


def get_v3_action_score_from_settings(action: str) -> int or float or None:
    scores_from_settings = getattr(settings, "DRF_RECAPTCHA_ACTION_V3_SCORES", None)

    if scores_from_settings is None:
        return None

    if not isinstance(scores_from_settings, dict):
        raise ImproperlyConfigured("DRF_RECAPTCHA_ACTION_V3_SCORES should be a dict.")

    action_score_from_settings = scores_from_settings.get(action, None)
    validate_v3_settings_score_value(action_score_from_settings, action)
    return action_score_from_settings


def get_v3_default_score_from_settings() -> int or float or None:
    default_score_from_settings = getattr(
        settings, "DRF_RECAPTCHA_DEFAULT_V3_SCORE", None
    )
    validate_v3_settings_score_value(default_score_from_settings)
    return default_score_from_settings
