# Test keys https://developers.google.com/recaptcha/docs/faq
#
# For reCAPTCHA v3, create a separate key for testing environments.
# Scores may not be accurate as reCAPTCHA v3 relies on seeing real traffic.
#
# For reCAPTCHA v2, use the following test keys.
# You will always get No CAPTCHA and all verification requests will pass.

TEST_V2_SECRET_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
# SITE_KEY: 6Lf4f8EZAAAAAATdYSJV0kJQ2w_KTx8pdNRTvR8w
TEST_V3_SECRET_KEY = "6Lf4f8EZAAAAAEHo2Z78ZFgwTJFsWaBIzG-Xc_AZ"

DEFAULT_RECAPTCHA_DOMAIN = "www.google.com"

# https://developers.google.com/recaptcha/docs/v3
#
# reCAPTCHA v3 returns a score (1.0 is very likely a good interaction, 0.0 is very likely a bot).
# Based on the score, you can take variable action in the context of your site.

DEFAULT_V3_SCORE = 0.5
