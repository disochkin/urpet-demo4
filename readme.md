Демо приложение для демо экзамена
Реализован функционал:
2.2. Возможность редактирования заявок:
- Изменение этапа выполнения (выполнено, в работе, не выполнено);
- Изменение описания проблемы;
- Изменение, ответственного за выполнение работ.
2.3. Возможность отслеживания статуса заявки:
- Отображение списка заявок;
- Получение уведомлений о смене статуса заявки;
- Поиск заявки по номеру или по параметрам.
2.4. Возможность назначения ответственных за выполнение работ:
- Добавление исполнителя к заявке;
- Отслеживание состояния работы и получение уведомлений о ее завершении;
- Исполнитель может добавлять комментарии на форме заявки.
2.5. Расчет статистики работы отдела обслуживания:
- Количество выполненных заявок;
- Среднее время выполнения заявки;
- Статистика по типам неисправностей.

Запуск приложения:
1) Клонировать репозиторий:
   >> git clone https://github.com/disochkin/urpet-demo4.git
2) Рекомендуется активировать виртуальное окружение 
   Перейти в каталог со скаченным приложением, запустить команды:
   python3 -m venv myenv
   myenv\Scripts\activate
3) Запусить веб-сервер из каталога front
   python3 -m http.server 8080
4) Запустить веб-приложение
   uvicorn app:app --reload

