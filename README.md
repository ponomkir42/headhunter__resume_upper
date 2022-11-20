Скрипт на Python для автоматического подъема резюме в поиске для работодателя. Для работы необходимы библиотеки requests , pytelegrambotapi , APScheduler , а также желание быть замеченным на HH :). 

В код необходимо добавить токен телеграм бота, если вы хотите получать уведомления о неправильной работе скрипта, в заголовки запроса cookie авторизованного пользователя hh.ru , а также x-xsrftoken (лежит в куках ( _xsrf ), а также в заголовках ответа любого запроса с сайта). В тело запроса идентификатор резюме (проще всего найти на странице своего резюме в адресной строке). 

Установлено 4 подъема объявления в сутки, время указано под сервер aws ( там часовой пояс по Гринвичу ), куда будет загружен для непрерывной работы этот скрипт. Также приложен файл *.service для создания демона на systemd на линукс-сервере.
