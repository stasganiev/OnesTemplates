[Главная](./../README.md)

# Каталог шаблонов

Собран из файла `GanievPRO.st`: Ganiev.PRO (v8.3.6.13 from 16 May 2024).

Сочетание это то, что набирается в модуле. Часть в квадратных скобках
набирать не обязательно: для `Проц[едура]` хватит `Проц`. Если на одно
сочетание приходится несколько шаблонов, конфигуратор покажет список на выбор.
Шаблоны без сочетания перетаскиваются в модуль из окна «Шаблоны текста».

Файл собирает скрипт `tools/make_catalog.py`. Руками его не правят.

## Русский синтаксис

### Комментарии и области

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `Облас[ть]` | Область | Область |
| `Облас[ть]` | Область (общий модуль) | Область |
| `Облас[ть]` | Область (модуль объекта) | Область |
| `Облас[ть]` | Область (модуль менеджера) | Область |
| `Облас[ть]` | Область (модуль формы) | Область |
| `Облас[ть]` | Область (модуль команды) | Область |
| `туду` | Тех.долг (тех.долг) | Технический долг |
| `туду` | Тех.долг (замечание) | Технический долг |
| `туду` | Тех.долг (ошибка) | Технический долг |
| `Коммент[арий]` | Комментарий* (заголовок процедуры) | Комментарии |
| `Коммент[арий]` | Комментарий* (заголовок функции) | Комментарии |
| `Коммент[арий]` | Комментарий* (раздел модуля) | Комментарии |
| `/ЗМ` | Заголовок модуля | Комментарии |
| `\ЗМ` | Заголовок модуля | Комментарии |
| `\хъ` | Группировка с комментарием | Комментарии |
| `/хъ` | Группировка с комментарием | Комментарии |
| `\х` | Группировка с комментарием Открыть | Комментарии |
| `/х` | Группировка с комментарием Открыть | Комментарии |
| `\ъ` | Группировка с комментарием Закрыть | Комментарии |
| `/ъ` | Группировка с комментарием Закрыть | Комментарии |
| `/+` | Фрагмент добавлен | Комментарии |
| `/-` | Фрагмент удален | Комментарии |
| `/=` | Фрагмент изменен | Комментарии |
| `/*` | Отчерк | Комментарии |
| `/+[+]` | Фрагмент добавлен с задачей | Комментарии |
| `/+[+]` | Фрагмент добавлен с задачей (однострочный) | Комментарии |
| `/+[+]` | Фрагмент добавлен с задачей и описанием | Комментарии |
| `/+[+]` | Фрагмент добавлен с задачей и описанием (однострочный) | Комментарии |
| `Модуль=` | Общий модуль | Структура модулей |
| `#М[одуль]` | Общий модуль | Структура модулей |
| `стм` | Общий модуль | Структура модулей |
| `Модуль=` | Общий модуль (только области) | Структура модулей |
| `#М[одуль]` | Общий модуль (только области) | Структура модулей |
| `стм` | Общий модуль (только области) | Структура модулей |
| `Модуль=` | Модуль объекта | Структура модулей |
| `#М[одуль]` | Модуль объекта | Структура модулей |
| `стм` | Модуль объекта | Структура модулей |
| `Модуль=` | Модуль менеджера | Структура модулей |
| `#М[одуль]` | Модуль менеджера | Структура модулей |
| `стм` | Модуль менеджера | Структура модулей |
| `Модуль=` | Модуль формы | Структура модулей |
| `#М[одуль]` | Модуль формы | Структура модулей |
| `стм` | Модуль формы | Структура модулей |
| `Модуль=` | Модуль команды | Структура модулей |
| `#М[одуль]` | Модуль команды | Структура модулей |
| `стм` | Модуль команды | Структура модулей |
| `Модуль=` | Модуль команды (только области) | Структура модулей |
| `#М[одуль]` | Модуль команды (только области) | Структура модулей |
| `стм` | Модуль команды (только области) | Структура модулей |
| `Модуль=` | Модуль бизнес-процесса | Структура модулей |
| `#М[одуль]` | Модуль бизнес-процесса | Структура модулей |
| `стм` | Модуль бизнес-процесса | Структура модулей |

### Инструкции, директивы, аннотации

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `#Е[сли]` | #Если Сервер |  |
| `№Е[сли]` | #Если Сервер |  |
| `#Е[сли]` | #Если Клиент |  |
| `№Е[сли]` | #Если Клиент |  |
| `#Е[сли]` | #Если (выбор) |  |
| `№Е[сли]` | #Если (выбор) |  |
| `#Е[сли]` | #Если (заглушка) |  |
| `№Е[сли]` | #Если (заглушка) |  |
| `Загл[ушка]` | #Если (заглушка) |  |
| `#Е[сли]` | #Если (серверный модуль) |  |
| `№Е[сли]` | #Если (серверный модуль) |  |
| `#Е[сли]` | #Если (серверный модуль с исключением) |  |
| `№Е[сли]` | #Если (серверный модуль с исключением) |  |
| `Инстр[укция]` | Инструкция препроцессора |  |
| `Инстр[укция]` | Инструкция препроцессора (без условия) |  |
| `Дирек[тива]` | Директива компиляции |  |
| `&[На]` | Директива компиляции |  |
| `&` | Аннотация расширения |  |
| `&` | Аннотация расширения (имя процедуры) |  |

### Управляющие

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `Если` | Если |  |
| `Если=` | Если (с условием) |  |
| `Если=` | Если + Иначе |  |
| `Если=` | Если + ИначеЕсли |  |
| `ИначеЕ[сли]` | ИначеЕсли |  |
| `Пока` | Пока |  |
| `Пока=` | Пока (с условием) |  |
| `Для` | Для |  |
| `Для[ Каждого]` | Для Каждого |  |
| `Возв[рат]` | Возврат |  |
| `Попы[тка]` | Попытка |  |
| `Транз[акция]` | Транзакция |  |
| `Проц[едура]` | Процедура | Процедура |
| `Проц[едура]` | Процедура (с параметрами) | Процедура |
| `Проц[едура]` | Процедура (полная) | Процедура |
| `Проц[едура]` | Процедура (полная с комментарием) | Процедура |
| `Проц[едура]` | Процедура НаКлиенте | Процедура |
| `Проц[едура]` | Процедура НаСервере | Процедура |
| `Проц[едура]` | Процедура НаСервереБезКонтекста (модуль формы) | Процедура |
| `Проц[едура]` | Процедура НаКлиентеНаСервереБезКонтекста (модуль формы) | Процедура |
| `Проц[едура]` | Процедура НаКлиентеНаСервере (модуль команды) | Процедура |
| `Функ[ция]` | Функция | Функция |
| `Функ[ция]` | Функция (с параметрами) | Функция |
| `Функ[ция]` | Функция (полная) | Функция |
| `Функ[ция]` | Функция (полная с комментарием) | Функция |
| `Функ[ция]` | Функция НаКлиенте | Функция |
| `Функ[ция]` | Функция НаСервере | Функция |
| `Функ[ция]` | Функция НаСервереБезКонтекста (модуль формы) | Функция |
| `Функ[ция]` | Функция НаКлиентеНаСервереБезКонтекста (модуль формы) | Функция |
| `Функ[ция]` | Функция НаКлиентеНаСервере (модуль команды) | Функция |

### Запросы

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `Запрос=` | Запрос с конструктором |  |
| `Запрос=` | Запрос вручную |  |
| `Запрос=` | Запрос с конструктором с обработкой результата |  |
| `Запрос=` | Запрос без конструктора с обработкой результата |  |
| `Документ.` | Документ |  |
| `Справочник.` | Справочник |  |
| `Рег[истрСведений.]` | РегистрСведений |  |
| `Рег[истрНакопления.]` | РегистрНакопления |  |
| `Рег[истрБухгалтерии.]` | РегистрБухгалтерии |  |
| `Рег[истрРасчета.]` | РегистрРасчета |  |
| `ЛЕВОЕ` | ЛЕВОЕ СОЕДИНЕНИЕ |  |
| `ПРАВОЕ` | ПРАВОЕ СОЕДИНЕНИЕ |  |
| `ВНУТРЕНН[ЕЕ]` | ВНУТРЕННЕЕ СОЕДИНЕНИЕ |  |
| `//з` | Комментарий в запросе |  |
| `//з` | Комментарий в запросе (вокруг) |  |

### Общие объекты

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `ТабДок=` | ТабДок (создать новый) | Табличный документ |
| `ТабДок=` | ТабДок (элемент обычной формы) | Табличный документ |
| `ТабДок=` | ТабДок (элемент управляемой формы) | Табличный документ |
| `ТабДок=` | ТабДок (шаблон отчета) | Табличный документ |
| `Обл=` | Область табличного документа | Табличный документ |
| `Обл=` | Область табличного документа с выводом | Табличный документ |
| `Макет=` | ПолучитьМакет | Табличный документ |
| `Макет=` | ПолучитьОбщийМакет | Табличный документ |
| `Сооб[щение]` | Сообщение пользователю | Сообщение пользователю |
| `Сооб[щение]` | Сообщение пользователю с привязкой к реквизитам | Сообщение пользователю |
| `Сооб[щение]` | Сообщение пользователю с описанием | Сообщение пользователю |
| `Блокир[овка=]` | Блокировка РегистрНакопления | Блокировки |
| `Блокир[овка=]` | Блокировка РегистрБухгалтерии | Блокировки |
| `Блокир[овка=]` | Блокировка РегистрСведений | Блокировки |
| `Блокир[овка=]` | Блокировка РегистрРасчета | Блокировки |

### Раскладка клавиатуры

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `Ю` | > |  |
| `Б` | < |  |
| `БЮ` | <> |  |
| `Б=` | <= |  |
| `Ю=` | >= |  |
| `ЕстьТгдд` | ЕстьТгдд |  |
| `ЕстьНул[ь]` | ЕстьТгдд |  |
| `тгдд` | NULL |  |
| `нул[ь]` | NULL |  |
| `хъ` | [] |  |
| `\` | \| |  |
| `ээ` | ' |  |
| `?` | & |  |
| `??` | & |  |
| `цуицвета` | WebЦвета |  |
| `вебцвета` | WebЦвета |  |
| `?НаКли[енте]` | ?НаКлиенте |  |
| `?НаСер[вере]` | ?НаСервере |  |
| `?НаСер[вереБезКонтекста]` | ?НаСервереБезКонтекста |  |
| `?НаКли[ентеНаСервереБезКонтекста]` | ?НаКлиентеНаСервереБезКонтекста |  |
| `ФТЫШ` | ANSI |  |
| `АНСИ` | ANSI |  |
| `СЩЬ` | COM |  |
| `СОМ` | COM |  |
| `АЕЗ` | FTP |  |
| `ФТП` | FTP |  |
| `ПУЕ` | GET |  |
| `ГЕТ` | GET |  |
| `РЕЬД` | HTML |  |
| `ХТМЛ` | HTML |  |
| `РЕЕЗ` | HTTP |  |
| `ХТТП` | HTTP |  |
| `ОЫЩТ` | JSON |  |
| `ЩУЬ` | OEM |  |
| `ОЕМ` | OEM |  |
| `ЗЩЗ3` | POP3 |  |
| `ПОП3` | POP3 |  |
| `ЗЩЫЕ` | POST |  |
| `ПОСТ` | POST |  |
| `ЫЬЕЗ` | SMTP |  |
| `СМТП` | SMTP |  |
| `ГКД` | URL |  |
| `УРЛ` | URL |  |
| `ГЕА` | UTF |  |
| `УТФ` | UTF |  |
| `ГТШЧ` | UNIX |  |
| `ЮНИКС` | UNIX |  |
| `ЦШТВ[ЩЦЫ]` | WINDOWS |  |
| `ВИНД[ОУС]` | WINDOWS |  |
| `ЧИФЫ[У]` | XBASE |  |
| `ЧЬД` | XML |  |
| `ХМЛ` | XML |  |

### Универсальные коллекции значений

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `Массив=` | Массив |  |
| `Коллек[ция]` | Массив |  |
| `Массив=` | Массив (создать и добавить) |  |
| `Коллек[ция]` | Массив (создать и добавить) |  |
| `Соответствие=` | Соответствие |  |
| `Коллек[ция]` | Соответствие |  |
| `Соответствие=` | Соответствие (создать и добавить) |  |
| `Коллек[ция]` | Соответствие (создать и добавить) |  |
| `СЗ=` | Список значений |  |
| `Коллек[ция]` | Список значений |  |
| `СЗ=` | Список значений (создать и добавить) |  |
| `Коллек[ция]` | Список значений (создать и добавить) |  |
| `Структура=` | Структура |  |
| `Коллек[ция]` | Структура |  |
| `Структура=` | Структура (создать и добавить) |  |
| `Коллек[ция]` | Структура (создать и добавить) |  |
| `Структура=` | Структура (создать конструктором) |  |
| `Коллек[ция]` | Структура (создать конструктором) |  |
| `Структура=` | Структура (проверка свойства) |  |
| `Коллек[ция]` | Структура (проверка свойства) |  |
| `ТЗ=` | ТЗ |  |
| `Коллек[ция]` | ТЗ |  |
| `ТЗ=` | ТЗ (создать и добавить колонку) |  |
| `Коллек[ция]` | ТЗ (создать и добавить колонку) |  |
| `Дерево=` | ДеревоЗначений |  |
| `ДеревоЗначений=` | ДеревоЗначений |  |
| `Коллек[ция]` | ДеревоЗначений |  |
| `Ключ=` | Ключ и значение (обход коллекции) |  |
| `Коллек[ция]` | Ключ и значение (обход коллекции) |  |

### Прикладные объекты

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `Переч[исления.]` | Значение перечисления |  |
| `СчетДт=` | ВыборСчетаДт |  |
| `СчетКт=` | ВыборСчетаКт |  |
| `Движение=` | Движение |  |
| `СубконтоДт` | СубконтоДт |  |
| `СубконтоКт` | СубконтоКт |  |
| `Граница=` | Граница |  |
| `ВидД[вижения=]` | РегистрыНакопления | ВидДвижения |
| `ВидД[вижения=]` | РегистрыБухгалтерии | ВидДвижения |
| `НаборЗаписей=` | РегистрСведений | Записи регистров |
| `НаборЗаписей=` | РегистрНакопления | Записи регистров |
| `НаборЗаписей=` | РегистрБухгалтерии | Записи регистров |
| `НаборЗаписей=` | РегистрРасчета | Записи регистров |
| `Запись=` | ЗаписьРегистраРасчетов | Записи регистров |

### Диалоговые

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `НастройкаПер[иода=]` | НастройкаПериода |  |
| `ВыборФайла=` | Диалог выбора файла |  |
| `Пр[едупреждение]` | Предупреждение | Предупреждение |
| `ПоказатьПр[едупреждение]` | Предупреждение | Предупреждение |
| `ПоказатьПр[едупреждение]` | Предупреждение c обработкой оповещения | Предупреждение |
| `Ответ=` | Вопрос | Вопрос |
| `ПоказатьВо[прос]` | Вопрос | Вопрос |
| `Воп[рос]` | Вопрос | Вопрос |
| `Ответ=` | Вопрос с анализом результата | Вопрос |
| `ПоказатьВо[прос]` | Вопрос с анализом результата | Вопрос |
| `Воп[рос]` | Вопрос с анализом результата | Вопрос |
| `ПоместитьФ[айл]` | ПоместитьФайл | НачатьПомещениеФайла |
| `НачатьПо[мещениеФайла]` | ПоместитьФайл | НачатьПомещениеФайла |
| `ОткрытьФ[орму]` | Основная форма нового объекта | Открыть форму (упраляемая) |
| `ОткрытьФ[орму]` | Основная форма новой группы | Открыть форму (упраляемая) |
| `ОткрытьФ[орму]` | Основная форма списка или выбора | Открыть форму (упраляемая) |
| `ОткрытьФ[орму]` | Произвольная форма | Открыть форму (упраляемая) |
| `ОткрытьФ[орму]` | Основная форма существующего объекта | Открыть форму (упраляемая) |
| `ОткрытьФ[орму]` | Форма списка с позиуционированием на элементе | Открыть форму (упраляемая) |
| `ОткрытьФ[орму]` | Список подчиненного справочника с отбором по владельцу | Открыть форму (упраляемая) |

### Сокращения

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `НМ` | НачалоМесяца |  |
| `КМ` | КонецМесяца |  |
| `НД` | НачалоДня |  |
| `КД` | КонецДня |  |
| `ТД` | ТекущаяДата |  |
| `ТД[С]` | ТекущаяДатаСеанса |  |
| `ПДН` | ПериодДействияНачало |  |
| `ПДК` | ПериодДействияКонец |  |
| `БПН` | БазовыйПериодНачало |  |
| `БПК` | БазовыйПериодКонец |  |
| `ПВХ` | ПланыВидовХарактеристик |  |
| `ПВР` | ПланыВидовРасчета |  |
| `ДМ` | ДобавитьМесяц |  |
| `Неоп[ределено]` | Неопределено |  |
| `УП` | УстановитьПараметр |  |
| `Конт[рагент]` | Контрагент |  |
| `Номе[нклатура]` | Номенклатура |  |
| `Коли[чество]` | Количество |  |
| `Стои[мость]` | Стоимость |  |
| `УЗП` | УстановитьЗначениеПараметра |  |
| `МВ` | МоментВремени |  |
| `ЗЗ[С]` | ЗаполнитьЗначенияСвойств |  |
| `ЗЗ` | ЗначениеЗаполнено |  |
| `БК` | БиблиотекаКартинок |  |

### Прочие

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `Формат` | Формат |  |
| `Тип=` | Конструктор описания типов |  |
|  | Проверка типа |  |
| `Шрифт=` | Шрифт |  |
| `Число[Прописью]` | ЧислоПрописью (Рубль, Россия) |  |
| `Число[Прописью]` | ЧислоПрописью (Доллар, США) |  |
| `Число[Прописью]` | ЧислоПрописью (Евро, Германия) |  |
| `Число[Прописью]` | ЧислоПрописью (Роны, Румыния) |  |
| `Выборка=` | Выборка |  |
| `НСтр` | НСтр RU |  |
| `НСтр` | НСтр RU EN |  |
| `Экс[порт]` | Экспорт |  |

### Расширения

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `#Вста[вка]` | #Вставка (расширения) |  |
| `№Вста[вка]` | #Вставка (расширения) |  |
| `#Удал[ение]` | #Удаление (расширения) |  |
| `№Удал[ение]` | #Удаление (расширения) |  |
| `Расш[ирение]` | Расширение #Вставка |  |
| `Расш[ирение]` | Расширение #Удаление |  |
| `Проц[едура]` | Расширение &Перед | Процедура |
| `Проц[едура]` | Расширение &После | Процедура |
| `Проц[едура]` | Расширение &Вместо | Процедура |
| `Проц[едура]` | Расширение &ИзменениеИКонтроль | Процедура |
| `Расш[ирение]` | Расширение Процедура | Процедура |
| `Функ[ция]` | Расширение &Перед | Функция |
| `Функ[ция]` | Расширение &После | Функция |
| `Функ[ция]` | Расширение &Вместо | Функция |
| `Проц[едура]` | Расширение &ИзменениеИКонтроль | Функция |
| `Расш[ирение]` | Расширение Функция | Функция |

### Асинхронные вызовы

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `Опис[ание]` | Описание оповещения | Оповещение и обещание |
| `Оповещ[ение]` | Описание оповещения | Оповещение и обещание |
| `Опис[ание]` | Описание оповещения (с описанием обработчика) | Оповещение и обещание |
| `Оповещ[ение]` | Описание оповещения (с описанием обработчика) | Оповещение и обещание |
| `Опис[ание]` | Описание оповещения с обработчиком ошибки | Оповещение и обещание |
| `Оповещ[ение]` | Описание оповещения с обработчиком ошибки | Оповещение и обещание |
| `Опис[ание]` | Описание оповещения с обработчиком ошибки (с описанем обработчика) | Оповещение и обещание |
| `Оповещ[ение]` | Описание оповещения с обработчиком ошибки (с описанем обработчика) | Оповещение и обещание |
| `Обещ[ание=]` | Обещание | Оповещение и обещание |
| `Проц[едура]` | Асинх Процедура | Процедура |
| `Асинх[ Процедура]` | Асинх Процедура | Процедура |
| `Асинх[Процедура]` | Асинх Процедура | Процедура |
| `Проц[едура]` | Асинх Процедура (с параметрами) | Процедура |
| `Асинх[Процедура]` | Асинх Процедура (с параметрами) | Процедура |
| `Проц[едура]` | Асинх Процедура (полная) | Процедура |
| `Асинх[Процедура]` | Асинх Процедура (полная) | Процедура |
| `Проц[едура]` | Асинх Процедура (полная с комментарием) | Процедура |
| `Асинх[Процедура]` | Асинх Процедура (полная с комментарием) | Процедура |
| `Проц[едура]` | Асинх Процедура НаКлиенте | Процедура |
| `Асинх[Процедура]` | Асинх Процедура НаКлиенте | Процедура |
| `Проц[едура]` | Асинх Процедура НаСервере | Процедура |
| `Асинх[Процедура]` | Асинх Процедура НаСервере | Процедура |
| `Проц[едура]` | Асинх Процедура НаСервереБезКонтекста (модуль формы) | Процедура |
| `Асинх[Процедура]` | Асинх Процедура НаСервереБезКонтекста (модуль формы) | Процедура |
| `Проц[едура]` | Асинх Процедура НаКлиентеНаСервереБезКонтекста (модуль формы) | Процедура |
| `Асинх[Процедура]` | Асинх Процедура НаКлиентеНаСервереБезКонтекста (модуль формы) | Процедура |
| `Проц[едура]` | Асинх Процедура НаКлиентеНаСервере (модуль команды) | Процедура |
| `Асинх[Процедура]` | Асинх Процедура НаКлиентеНаСервере (модуль команды) | Процедура |
| `Функ[ция]` | Асинх Функция | Функция |
| `Асинх[ Функция]` | Асинх Функция | Функция |
| `Асинх[Функция]` | Асинх Функция | Функция |
| `Функ[ция]` | Асинх Функция (с параметрами) | Функция |
| `Асинх[Функция]` | Асинх Функция (с параметрами) | Функция |
| `Функ[ция]` | Асинх Функция (полная) | Функция |
| `Асинх[Функция]` | Асинх Функция (полная) | Функция |
| `Функ[ция]` | Асинх Функция (полная с комментарием) | Функция |
| `Асинх[Функция]` | Асинх Функция (полная с комментарием) | Функция |
| `Функ[ция]` | Асинх Функция НаКлиенте | Функция |
| `Асинх[Функция]` | Асинх Функция НаКлиенте | Функция |
| `Функ[ция]` | Асинх Функция НаСервере | Функция |
| `Асинх[Функция]` | Асинх Функция НаСервере | Функция |
| `Функ[ция]` | Асинх Функция НаСервереБезКонтекста | Функция |
| `Асинх[Функция]` | Асинх Функция НаСервереБезКонтекста | Функция |
| `Функ[ция]` | Асинх Функция НаКлиентеНаСервереБезКонтекста (только модули упр.форм) | Функция |
| `Асинх[Функция]` | Асинх Функция НаКлиентеНаСервереБезКонтекста (только модули упр.форм) | Функция |
| `Функ[ция]` | Асинх Функция НаКлиентеНаСервере (только модули команд) | Функция |
| `Асинх[Функция]` | Асинх Функция НаКлиентеНаСервере (только модули команд) | Функция |
| `Ответ=` | Асинх Вопрос | Вопрос |
| `ПоказатьВо[прос]` | Асинх Вопрос | Вопрос |
| `Воп[рос]` | Асинх Вопрос | Вопрос |
| `Ответ=` | Асинх Вопрос с анализом результата | Вопрос |
| `ПоказатьВо[прос]` | Асинх Вопрос с анализом результата | Вопрос |
| `Воп[рос]` | Асинх Вопрос с анализом результата | Вопрос |
|  | Поместить файл | Помещение файла во временное хранилище |
|  | Поместить файл Асинх | Помещение файла во временное хранилище |

### Полезняшки

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
|  | Добавить реквизит формы | Формы |
|  | Добавить команду формы | Формы |
|  | Добавить элемент - кнопка формы | Формы |
|  | Добавить элемент - группа формы | Формы |
|  | Добавить элемент - поле формы | Формы |
|  | Добавить элемент - декорация формы | Формы |
|  | Добавить элемент - таблица формы | Формы |
|  | Загрузка данных из Excel Асинх |  |
|  | Открыть форму записи РС (вариант 1) |  |
|  | Открыть форму записи РС (вариант 2) |  |

### HTTP сервисы

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `http=` | HTTP соединение |  |
| `хттп=` | HTTP соединение |  |
| `http=` | HTTP соединение защищенное Windows |  |
| `хттп=` | HTTP соединение защищенное Windows |  |
| `http=` | HTTP запрос |  |
| `хттп=` | HTTP запрос |  |
| `http=` | HTTP ответ |  |
| `хттп=` | HTTP ответ |  |
|  | Добавить параметры к строке адреса |  |
| `http=` | HTTP входящий запрос - параметр URL |  |
| `http=` | HTTP входящий запрос - параметр запроса |  |
| `http=` | HTTP входящий запрос - перебор параметров запроса |  |
| `http=` | HTTP входящий запрос - параметр из тела запроса |  |

### СКД - альфа версия

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `СКД=` | СхемаКомпоновки | НаборыДанных |
| `Источник[ДанныхСКД]=` | ИсточникДанныхСКД | НаборыДанных |
| `НаборД[анных=]` | Набор данных Запрос | НаборыДанных |
| `НаборД[анных=]` | Набор данных Объект | НаборыДанных |
| `НаборД[анных=]` | Набор данных Объединение | НаборыДанных |
| `ПолеСКД=` | ПолеСКД | НаборыДанных |
| `РесурсСКД=` | РесурсСКД | Ресурсы |
| `ПараметрСКД=` | ПараметрСКД | Параметры |
| `НастройкиСКД=` | НастройкиСКД Новый вариант | Настройки |
| `НастройкиСКД=` | НастройкиСКД Настройки по умолчанию | Настройки |
| `ГруппировкаСКД=` | ГруппировкаСКД - новая группировка в корень | Настройки |
| `ГруппировкаСКД=` | ГруппировкаСКД - вложенная группировка | Настройки |
| `ВыбранноеПолеСКД=` | ВыбранноеПолеСКД - АвтоПоле | Настройки |
| `ВыбранноеПолеСКД=` | ВыбранноеПолеСКД - Произольное поле | Настройки |
| `ПолеСортировкиСКД=` | ПолеСортировкиСКД - Авто | Настройки |
| `ПолеСортировкиСКД=` | ПолеСортировкиСКД - Произольное поле | Настройки |
|  | ЗначениеПараметраСКД | Настройки |
|  | ОтборСКД | Настройки |

## Английский синтаксис

### Comments and regions

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `Regi[on]` | Region | Region |
| `Regi[on]` | Region (common module) | Region |
| `Regi[on]` | Region (object module) | Region |
| `Regi[on]` | Region (manager module) | Region |
| `Regi[on]` | Region (form module) | Region |
| `Regi[on]` | Region (command module) | Region |
| `todo` | To-do | Technical debt |
| `todo` | To-do (alert) | Technical debt |
| `todo` | To-do (mistake) | Technical debt |
| `Comm[ent]` | Comment (procedure title) | Comments |
| `Comm[ent]` | Comment (function title) | Comments |
| `Comm[ent]` | Comment (module title) | Comments |
| `/mt` | Module title | Comments |
| `\mt` | Module title | Comments |
| `\[]` | Grouping with comment | Comments |
| `/[]` | Grouping with comment | Comments |
| `\[` | Grouping with comment Open | Comments |
| `/[` | Grouping with comment Open | Comments |
| `\]` | Grouping with comment Close | Comments |
| `/]` | Grouping with comment Close | Comments |
| `\+` | Snippet Add | Comments |
| `\-` | Snippet Delete | Comments |
| `\=` | Snippet Edit | Comments |
| `\*` | Dash | Comments |
| `\+[+]` | Snippet Add & task | Comments |
| `\+[+]` | Snippet Add & task (oneline) | Comments |
| `\+[+]` | Snippet Add & task & description | Comments |
| `\+[+]` | Snippet Add & task & description (oneline) | Comments |
| `Module=` | Common module | Module structure |
| `#M[odule]` | Common module | Module structure |
| `mst` | Common module | Module structure |
| `Module=` | Common module (regions only) | Module structure |
| `#M[odule]` | Common module (regions only) | Module structure |
| `mst` | Common module (regions only) | Module structure |
| `Module=` | Object module | Module structure |
| `#M[odule]` | Object module | Module structure |
| `mst` | Object module | Module structure |
| `Module=` | Manager module | Module structure |
| `#M[odule]` | Manager module | Module structure |
| `mst` | Manager module | Module structure |
| `Module=` | Form module | Module structure |
| `#M[odule]` | Form module | Module structure |
| `mst` | Form module | Module structure |
| `Module=` | Command module | Module structure |
| `#M[odule]` | Command module | Module structure |
| `mst` | Command module | Module structure |
| `Module=` | Command module (regions only) | Module structure |
| `#M[odule]` | Command module (regions only) | Module structure |
| `mst` | Command module (regions only) | Module structure |
| `Module=` | Business process module | Module structure |
| `#M[odule]` | Business process module | Module structure |
| `mst` | Business process module | Module structure |

### Instructions, directives, annotations

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `#If` | #If Server |  |
| `#If` | #If Client |  |
| `#If` | #If (selection) |  |
| `#If` | #If (plug) |  |
| `Plug` | #If (plug) |  |
| `#If` | #If (server module) |  |
| `#If` | #If (server module with exception) |  |
| `Instru[ction]` | Instruction |  |
| `Instru[ction]` | Instruction (without condition) |  |
| `Direc[tive]` | Directive |  |
| `&At` | Directive |  |
| `&` | Extension annotation |  |
| `&` | Extension annotation (procedure name) |  |

### Managed

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `If` | If |  |
| `If=` | If (with condition) |  |
| `If=` | If + Else |  |
| `If=` | If + ElsIf |  |
| `ElsIf` | ElsIf |  |
| `While` | While |  |
| `While=` | While (with condition) |  |
| `For` | For |  |
| `For` | For Each |  |
| `Retu[rn]` | Return |  |
| `Try` | Try |  |
| `Trans[action]` | Transaction |  |
| `Proc[edure]` | Procedure | Procedure |
| `Proc[edure]` | Procedure (with parameters) | Procedure |
| `Proc[edure]` | Procedure (full version) | Procedure |
| `Proc[edure]` | Procedure (full version with comment) | Procedure |
| `Proc[edure]` | Procedure AtClient | Procedure |
| `Proc[edure]` | Procedure AtServer | Procedure |
| `Proc[edure]` | Procedure AtServerNoContext (form's module) | Procedure |
| `Proc[edure]` | Procedure AtClientAtServerNoContext (form's module) | Procedure |
| `Proc[edure]` | Procedure AtClientAtServer (command module) | Procedure |
| `Func[tion]` | Function | Function |
| `Func[tion]` | Function (with parameters) | Function |
| `Func[tion]` | Function (full version) | Function |
| `Func[tion]` | Function (full version with comment) | Function |
| `Func[tion]` | Function AtClient | Function |
| `Func[tion]` | Function AtServer | Function |
| `Func[tion]` | Function AtServerNoContext (form's module) | Function |
| `Func[tion]` | Function AtClientAtServerNoContext (form's module) | Function |
| `Func[tion]` | Function AtClientAtServer (command module) | Function |

### Queries

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `Query=` | Query by wizard |  |
| `Query=` | Query manually |  |
| `Query=` | Query by wizard with result processing |  |
| `Query=` | Query without wizard with result processing |  |
| `Document.` | Document |  |
| `Catalog.` | Catalog |  |
| `Reg[ister.]` | InformationRegister |  |
| `Reg[ister.]` | AccumulationRegister |  |
| `Reg[ister.]` | AccountingRegister |  |
| `Reg[ister.]` | CalculationRegister |  |
| `LEFT` | LEFT JOIN |  |
| `RIGHT` | RIGHT JOIN |  |
| `INNER` | INNER JOIN |  |
| `//q` | Text query comment |  |
| `//q` | Text query comment (around) |  |

### Common objects

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `TablDoc=` | TablDoc (create new) | Spreadsheet document |
| `TablDoc=` | TablDoc (ordinary form item) | Spreadsheet document |
| `TablDoc=` | TablDoc (managed form item) | Spreadsheet document |
| `TablDoc=` | TablDoc (report template) | Spreadsheet document |
| `Area=` | Area | Spreadsheet document |
| `Area=` | Area output | Spreadsheet document |
| `Templ[ate=]` | GetTemplate | Spreadsheet document |
| `Templ[ate=]` | GetCommonTemplate | Spreadsheet document |
| `Mess[age]` | User message | User message |
| `Mess[age]` | User message with attribute joining | User message |
| `Mess[age]` | User message with description | User message |
| `Lock=` | DataLock InformationRegister | Data lock |
| `Lock=` | DataLock AccumulationRegister | Data lock |
| `Lock=` | DataLock AccountingRegister | Data lock |
| `Lock=` | DataLock CalculationRegister | Data lock |

### Quick snippets

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `&AtCl[ient]` | &AtClient |  |
| `&AtSer[ver]` | &AtServer |  |
| `&AtSer[ver]` | &AtServerNoContext |  |
| `&AtCl[ient]` | &AtClientAtServerNoContext |  |
| `&AtCl[ient]` | &AtClientAtServer |  |

### Universal value collections

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `Array=` | Array |  |
| `Collec[tion]` | Array |  |
| `Array=` | Array (create and append) |  |
| `Collec[tion]` | Array (create and append) |  |
| `Map=` | Map |  |
| `Collec[tion]` | Map |  |
| `Map=` | Map (create and append) |  |
| `Collec[tion]` | Map (create and append) |  |
| `List=` | List of values |  |
| `Collec[tion]` | List of values |  |
| `List=` | List of values (create and append) |  |
| `Collec[tion]` | List of values (create and append) |  |
| `Structure=` | Structure |  |
| `Collec[tion]` | Structure |  |
| `Structure=` | Structure (create and append) |  |
| `Collec[tion]` | Structure (create and append) |  |
| `Structure=` | Structure (create by contructor) |  |
| `Collec[tion]` | Structure (create by contructor) |  |
| `Structure=` | Structure (property check) |  |
| `Collec[tion]` | Structure (property check) |  |
| `VTab=` | Values table |  |
| `Collec[tion]` | Values table |  |
| `VTab=` | Values table (create and append a column) |  |
| `Collec[tion]` | Values table (create and append a column) |  |
| `Tree=` | Value tree |  |
| `ValueTree=` | Value tree |  |
| `Collec[tion]` | Value tree |  |
| `Key=` | KeyAndValue (round collection) |  |
| `Collec[tion]` | KeyAndValue (round collection) |  |

### Applied objects

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `Enums=` | Enum value |  |
| `Account[Dr=]` | AccountDrChoice |  |
| `Account[Cr=]` | AccountCrChoice |  |
| `Register[Record=]` | RegisterRecord |  |
| `ExtDimen[sionsDr=]` | ExtDimensionsDr |  |
| `ExtDimen[sionsCr=]` | ExtDimensionsCr |  |
| `Boundary=` | Boundary |  |
| `ВидД[вижения=]` | AccumulationRegisters | RecordType |
| `ВидД[вижения=]` | AccountingRegisters | RecordType |
| `RecordSet=` | RecordSet InformationRegister | Registers records |
| `RecordSet=` | RecordSet AccumulationRegister | Registers records |
| `RecordSet=` | RecordSet AccountingRegister | Registers records |
| `RecordSet=` | RecordSet CalculationRegister | Registers records |
| `Record=` | Calculation register record | Registers records |

### Dialogs

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `PeriodSet[tings]` | PeriodSettings |  |
| `FileChoice` | FileDialog |  |
| `FileDialog` | FileDialog |  |
| `ShowM[essageBox]` | Message box | Message box |
| `ShowM[essageBox]` | Message box with callback | Message box |
| `Answer=` | Question | Question |
| `ShowQ[ueryBox]` | Question | Question |
| `Ques[tion]` | Question | Question |
| `DoQuery[Box]` | Question | Question |
| `Answer=` | Question with result analysis | Question |
| `ShowQ[ueryBox]` | Question with result analysis | Question |
| `Ques[tion]` | Question with result analysis | Question |
| `DoQuery[Box]` | Question with result analysis | Question |
| `PutFile` | PutFile | BeginPutFile |
| `OpenF[orm]` | General form of new object | Open form (managed) |
| `OpenF[orm]` | General form of new folder | Open form (managed) |
| `OpenF[orm]` | List form or choice form | Open form (managed) |
| `OpenF[orm]` | Free form | Open form (managed) |
| `OpenF[orm]` | General form of existing object | Open form (managed) |
| `OpenF[orm]` | List form and activate the item | Open form (managed) |
| `OpenF[orm]` | List of subcatalog with filter by owner | Open form (managed) |

### Abbreviation

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `BM` | BegOfMonth |  |
| `EM` | EndOfMonth |  |
| `BD` | BegOfDay |  |
| `ED` | EndOfDay |  |
| `CD` | CurrentDate |  |
| `CD` | CurrentSessionDate |  |
| `CSD` | CurrentSessionDate |  |
| `BEP` | BegOfEffectivePeriod |  |
| `EEP` | EndOfEffectivePeriod |  |
| `BBP` | BegOfBasePeriod |  |
| `EBP` | EndOfBasePeriod |  |
| `CCT` | ChartsOfCharacteristicTypes |  |
| `CCT` | ChartsOfCalculationTypes |  |
| `AM` | AddMonth |  |
| `Undef[ined]` | Undefined |  |
| `SP` | SetParameter |  |
| `Cou[nterparty]` | Counterparty |  |
| `Prod[ucts]` | Products |  |
| `Cou[nt]` | Count |  |
| `Amo[unt]` | Amount |  |
| `SPV` | SetParameterValue |  |
| `PIT` | PointInTime |  |
| `PT` | PointInTime |  |
| `FPV` | FillPropertyValues |  |
| `VIF` | ValueIsFilled |  |
| `VF` | ValueIsFilled |  |
| `PL` | PictureLib |  |

### Other

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `Format` | Format |  |
| `Type=` | Type description constructor |  |
|  | Type check |  |
| `Font=` | Font |  |
| `Number[InWords]` | NumberInWords |  |
| `Number[InWords]` | NumberInWords (RUB, Russia) |  |
| `Number[InWords]` | NumberInWords (Dollars, USA) |  |
| `Number[InWords]` | NumberInWords (Euro, Germany) |  |
| `Number[InWords]` | NumberInWords (RON, Romania) |  |
| `Select[ion=]` | Selection |  |
| `NStr` | NStr EN |  |
| `NStr` | NStr EN RU |  |
| `Exp[ort]` | Export |  |

### Extensions

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `#Ins[ert]` | #Insert (extensions) |  |
| `#Del[ete]` | #Delete (extensions) |  |
| `Ext[ension]` | Extension #Insert |  |
| `Ext[ension]` | Extension #Delete |  |
| `Proc[edure]` | Extension &Before | Procedure |
| `Proc[edure]` | Extension &After | Procedure |
| `Proc[edure]` | Extension &Around | Procedure |
| `Proc[edure]` | Extension &ChangeAndValidate | Procedure |
| `Ext[ension]` | Extension Procedure | Procedure |
| `Func[tion]` | Extension &Before | Function |
| `Func[tion]` | Extension &After | Function |
| `Func[tion]` | Extension &Around | Function |
| `Func[tion]` | Extension &ChangeAndValidate | Function |
| `Ext[ension]` | Extension Function | Function |

### Asynchronous calls

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `Call[back]` | Callback description | Callback and promise |
| `Call[back]` | Callback description (handler description) | Callback and promise |
| `Call[back]` | Callback description with error handling | Callback and promise |
| `Call[back]` | Callback description with error handling (handler description) | Callback and promise |
| `Prom[ise=]` | Promise | Callback and promise |
| `Proc[edure]` | Async Procedure | Procedure |
| `Async[Procedure]` | Async Procedure | Procedure |
| `Proc[edure]` | Async Procedure (with parameters) | Procedure |
| `Async[Procedure]` | Async Procedure (with parameters) | Procedure |
| `Proc[edure]` | Async Procedure (full version) | Procedure |
| `Async[Procedure]` | Async Procedure (full version) | Procedure |
| `Proc[edure]` | Async Procedure (full version with comment) | Procedure |
| `Async[Procedure]` | Async Procedure (full version with comment) | Procedure |
| `Proc[edure]` | Async Procedure AtClient | Procedure |
| `Async[Procedure]` | Async Procedure AtClient | Procedure |
| `Proc[edure]` | Async Procedure AtServer | Procedure |
| `Async[Procedure]` | Async Procedure AtServer | Procedure |
| `Proc[edure]` | Async Procedure AtServerNoContext (form's module) | Procedure |
| `Async[Procedure]` | Async Procedure AtServerNoContext (form's module) | Procedure |
| `Proc[edure]` | Async Procedure AtClientAtServerNoContext (form's module) | Procedure |
| `Async[Procedure]` | Async Procedure AtClientAtServerNoContext (form's module) | Procedure |
| `Proc[edure]` | Async Procedure AtClientAtServer (command module) | Procedure |
| `Async[Procedure]` | Async Procedure AtClientAtServer (command module) | Procedure |
| `Func[tion]` | Async Function | Function |
| `Async[Function]` | Async Function | Function |
| `Func[tion]` | Async Function (with parameters) | Function |
| `Async[Function]` | Async Function (with parameters) | Function |
| `Func[tion]` | Async Function (full version) | Function |
| `Async[Function]` | Async Function (full version) | Function |
| `Func[tion]` | Async Function (full version with comment) | Function |
| `Async[Function]` | Async Function (full version with comment) | Function |
| `Func[tion]` | Async Function AtClient | Function |
| `Async[Function]` | Async Function AtClient | Function |
| `Func[tion]` | Async Function AtServer | Function |
| `Async[Function]` | Async Function AtServer | Function |
| `Func[tion]` | Async Function AtServerNoContext (form's module) | Function |
| `Async[Function]` | Async Function AtServerNoContext (form's module) | Function |
| `Func[tion]` | Async Function AtClientAtServerNoContext (form's module) | Function |
| `Async[Function]` | Async Function AtClientAtServerNoContext (form's module) | Function |
| `Func[tion]` | Async Function AtClientAtServer (command module) | Function |
| `Async[Function]` | Async Function AtClientAtServer (command module) | Function |
| `Answer=` | Async Question | Question |
| `ShowQ[ueryBox]` | Async Question | Question |
| `Ques[tion]` | Async Question | Question |
| `DoQuery[Box]` | Async Question | Question |
| `Answer=` | Async Question with result analysis | Question |
| `ShowQ[ueryBox]` | Async Question with result analysis | Question |
| `Ques[tion]` | Async Question with result analysis | Question |
| `DoQuery[Box]` | Async Question with result analysis | Question |
|  | Put file | Put the file in temporary storage |
|  | Put file Async | Put the file in temporary storage |

### Helpfulness

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
|  | Add form requisite | Forms |
|  | Add form command | Forms |
|  | Add item - form button | Forms |
|  | Add item - form group | Forms |
|  | Add item - form field | Forms |
|  | Add item - form decoration | Forms |
|  | Add item - form table | Forms |
|  | Data import from Excel Async |  |
|  | Open information register record form (option 1) |  |
|  | Open information register record form (option 2) |  |

### HTTP services

| Сочетание | Шаблон | Подгруппа |
| --- | --- | --- |
| `http=` | HTTP connection |  |
| `http=` | HTTP connection security Windows |  |
| `http=` | HTTP request |  |
| `http=` | HTTP response |  |
|  | Add parameters to source address |  |
| `http=` | HTTP incoming request - URL parameter |  |
| `http=` | HTTP incoming request - request's parameter |  |
| `http=` | HTTP incoming request - request's parameters selecting |  |
| `http=` | HTTP incoming request - parameters from request body |  |

---

[Назад](./../README.md)
