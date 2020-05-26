import time
import os
import django
import schedule

if os.environ['DJANGO_ENV'] in ("prod", "production"):
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "newsboard.settings.production"
    )
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newsboard.settings.dev")
django.setup()

from django.conf import settings
from main.models import Post


def runjob(cancel=False):
    print("reset upvotes")
    Post.objects.all().update(upvotes=0)
    if cancel:
        return schedule.CancelJob


def develop():
    schedule.every(10).seconds.do(runjob, cancel=True)
    while True:
        schedule.run_pending()
        time.sleep(42)


def main():
    schedule.every().day.at("23:45").do(runjob)
    while True:
        schedule.run_pending()
        time.sleep(42)


if __name__ == '__main__':
    if settings.DEBUG:
        develop()
    else:
        main()
