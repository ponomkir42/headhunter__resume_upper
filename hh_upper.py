import requests
import time
import telebot
from apscheduler.schedulers.blocking import BlockingScheduler
# укажите здесь токен своего телеграм бота
bot = telebot.TeleBot('TOKEN')

url = 'https://chelyabinsk.hh.ru/applicant/resumes/touch'

headers_hh = {
    # укажите cookies своей учетной записи HH
    'cookie': 'COOKIES',
    "accept": "application/json",
    "x-hhtmfrom": "resume_list",
    "x-hhtmsource": "resume",
    "x-requested-with": "XMLHttpRequest",
    # укажите токен своей учетной записи HH
    "x-xsrftoken": "TOKEN_HH",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"

}

data = dict(
    # укажите уникальный идентификатор резюме
    resume=(None, "ID OF RESUME"),
    undirectable=(None, "true"),
)


def hh_resume_upper():
    resp = requests.post(url, headers=headers_hh, files=data)
    if resp.status_code != 200:
        # укажите чат айди диалога с телеграм ботом, от которого хотите получать уведомления об ошибках
        bot.send_message('CHAT ID', f'Произошла ошибка: {resp.status_code}, {resp.headers}')

sched = BlockingScheduler()
sched.add_job(hh_resume_upper, trigger="cron", hour=4)
sched.add_job(hh_resume_upper, trigger="cron", hour=8, minute=2)
sched.add_job(hh_resume_upper, trigger="cron", hour=12, minute=4)
sched.add_job(hh_resume_upper, trigger="cron", hour=16, minute=8)

sched.start()

# бесконечный цикл, рекомендованный разработчиками PyTelegrambotAPI, чтобы обеспечить стабильную работу скрипта
while True:
    try:
        bot.polling(none_stop=True)
    except:
        time.sleep(5)
