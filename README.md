По заданию:
___


Нам необходимо разработать интернет-ресурс для фанатского сервера одной известной MMORPG — что-то вроде доски объявлений. Пользователи нашего ресурса должны иметь возможность зарегистрироваться в нём по e-mail, получив письмо с кодом подтверждения регистрации. После регистрации им становится доступно создание и редактирование объявлений. Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент. Пользователи могут отправлять отклики на объявления других пользователей, состоящие из простого текста. При отправке отклика пользователь должен получить e-mail с оповещением о нём. Также пользователю должна быть доступна приватная страница с откликами на его объявления, внутри которой он может фильтровать отклики по объявлениям, удалять их и принимать (при принятии отклика пользователю, оставившему отклик, также должно прийти уведомление). Кроме того, пользователь обязательно должен определить объявление в одну из следующих категорий: Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.

Также мы бы хотели иметь возможность отправлять пользователям новостные рассылки.
___

Был создан проект NewsPost

Регистрация по Email, c подтверждением по коду из Email работает корректно.

Зарегистрированные пользователи могут создавать и редактировать объявления, также производится проверка пользователя на редактирование объявления, если пользователь не автор объявления, то он не сможет отредактировать его и кнопка редактировать не отобразится на странице с объявлением.

Есть возможность добавить 2 картинки и 2 ссылки на видео с YouTube, картинки и видео отображаются на странице с объявлением. На главной странице отображаются все объявления с одной картинкой.

На странице с объявлением есть кнопка 'добавить отклик'. При добавлении отклика, автору объявления приходит оповещение на email, отклик отобразится в разделе "меню пользователя", 
отклики будут заранее отфильтрованы по объявлениям. У новых откликов будет доступна кнопка "изменить статус", если поставить "подтвержден", то на email отправителя отклика придет письмо с оповещением о принятии отклика и отклик отобразится
на странице объявления, если поставить статус 'удалить', то отклик исчезнет из меню пользователя. 

Выбор категорий при создании объявления реализован и работает корректно.

Также был создан раздел 'Новости', в котором отображаются все новости. Создавать новость может только суперюзер, также если суперюзер авторизован, то у него в разделе 'Новости' будет отображаться кнопка 'Cоздать новость', после создания новости, всем зарегистрированным пользователям придет письмо на Email с этой новостью
