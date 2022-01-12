import datetime
import random
import finam_utills as gen
import logging
import sys

logging.basicConfig(encoding='utf-8', level=logging.INFO)

with open('data_for_finam.sql', 'w', encoding='utf-8') as f:
    list_querry = []
    list_querry.append('USE finam;\n\n')

    # ============= Данные для таблицы document =======================
    logging.debug('Данные для таблицы document')

    table_name = 'document'
    headers = ['document_name']
    list_querry.append(f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES \n')
    row_dict = {}
    documents = gen.get_documents()                  
    for doc in documents:
        row_dict['document_name'] = doc
        row = '   ('
        for col in headers:
            row += f"'{row_dict[col]}', "
        row = row[0:-2] + f'),\n'  
        list_querry.append(row)

    list_querry[len(list_querry)-1] = f"{list_querry[len(list_querry)-1][:-2]};\n"
    list_querry.append('\n')  

    # ============= Данные для таблицы client ======================
    logging.debug('Данные для таблицы client')
    table_name = 'client'
    headers = ['second_name', 'first_name', 'patronymic',
                'birthday', 'document_id', 'doc_serial', 'doc_number',
                'doc_date', 'birthplace', 'inn', 'registration_address',
                'residence_address', 'mailing_address', 'mobile_phone',
                'email']
    list_querry.append(f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES \n')
    num_clients = 500
    mobile_phone = gen.mobile_phone_init(num_mobiles=num_clients)
    get_inn = gen.get_inn_init(num_inns=num_clients)
    get_mail = gen.get_mail_init()
    for num_row in range(1, num_clients + 1):
        row_dict = {}
        row_dict['second_name'] = gen.get_second_name()
        row_dict['first_name'] = gen.get_first_name()
        row_dict['patronymic'] = gen.get_patronymic()
        row_dict['birthday'] =  gen.get_date(date_from = '1960-01-01', date_to = '2002-01-01')
        passport = gen.get_passport(row_dict['birthday']) 
        row_dict['document_id'] = passport[0]
        row_dict['doc_serial'] = passport[1]
        row_dict['doc_number'] = passport[2]
        row_dict['doc_date'] = passport[3]

        row_dict['birthplace'] = gen.get_city()
        row_dict['inn'] = get_inn()
        row_dict['registration_address'] = gen.get_address()
        row_dict['residence_address'] = gen.get_address()
        row_dict['mailing_address'] = row_dict['residence_address']
        row_dict['mobile_phone'] = mobile_phone()
        row_dict['email'] = get_mail(second_name=row_dict['second_name'], 
                                    first_name=row_dict['first_name'], 
                                    birth_year=row_dict['birthday'].year)
        row = '   ('
        for col in headers:
            row += f"'{row_dict[col]}', "
        row = row[0:-2] + f'),\n'  
        list_querry.append(row)

    list_querry[len(list_querry)-1] = f"{list_querry[len(list_querry)-1][:-2]};\n"
    list_querry.append('\n')   

    # ============= Данные для таблицы tariff_plan ======================
    logging.debug('Данные для таблицы tariff_plan')
    table_name = 'tariff_plan'
    headers = ['tariff_plan_name']
    list_querry.append(f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES \n')
    row_dict = {}
    
    tariff_plans = ['Дневной', 'Фиксированный', 'Тест-драйв', 
            'Консультационный', 'Дневной ИЦБ', 'Консультационный ИЦБ']
    num_tariff_plans = len(tariff_plans)
    for doc_type in tariff_plans:
        row_dict['tariff_plan_name'] = doc_type
        row = '   ('

        for col in headers:
            row += f"'{row_dict[col]}', "
        row = row[0:-2] + f'),\n'  
        list_querry.append(row)
    list_querry[len(list_querry)-1] = f"{list_querry[len(list_querry)-1][:-2]};\n"
    list_querry.append('\n')

    # ============= Данные для таблицы brokerage_agreement ======================
    logging.debug('Данные для таблицы brokerage_agreement')
    # 21Б/2806-1839/1 от 28.06.2021
    # Номер счета
    # КлФ-1291610
    # Торговый код
    # 341066R89RI/341066R89RI
    # Тарифный план
    # Инвестор
    # Депозитарный договор
    # 21В/2806-1839/1 от 28.06.21

    table_name = 'brokerage_agreement'
    headers = ['brokerage_agreement', 'client_id', 'account_number', 'trading_code', 
               'tariff_plan_id', 'custody_agreement']

    list_querry.append(f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES \n')
    row_dict = {}

    get_brokerage_agreement = gen.get_brokerage_agreement_init(num_clients*3)
    count_br_agr_ids = 0
    for num_client in range(1, num_clients+1):
        num_brokerage_agreement_for_client = random.randint(1,3)
        row_dict['client_id'] = num_client
        for repeat in range(num_brokerage_agreement_for_client):
            count_br_agr_ids += 1
            b_a = get_brokerage_agreement()
            row_dict['brokerage_agreement'] = b_a[0]
            row_dict['account_number'] = b_a[1]
            row_dict['trading_code'] = b_a[2]
            row_dict['tariff_plan_id'] = random.randint(1,num_tariff_plans)
            row_dict['custody_agreement'] = b_a[3]
            row = '   ('
            for col in headers:
                row += f"'{row_dict[col]}', "
            row = row[0:-2] + f'),\n' 
            list_querry.append(row)
    list_querry[len(list_querry)-1] = f"{list_querry[len(list_querry)-1][:-2]};\n" 
    list_querry.append('\n')

    # ============= Данные для таблицы type_asset ======================
    logging.debug('Данные для таблицы type_asset')
    table_name = 'type_asset'
    headers = ['type_asset_name']
    list_querry.append(f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES \n')
    row_dict = {}
    
    type_assets = ['Валюта', 'Акции', 'Облигации']
    num_type_assets = len(type_assets)
    for type_asset in type_assets:
        row_dict['type_asset_name'] = type_asset
        row = '   ('

        for col in headers:
            row += f"'{row_dict[col]}', "
        row = row[0:-2] + f'),\n'  
        list_querry.append(row)
    list_querry[len(list_querry)-1] = f"{list_querry[len(list_querry)-1][:-2]};\n"
    list_querry.append('\n')   

    # ============= Данные для таблицы asset ======================
    logging.debug('Данные для таблицы asset')

    table_name = 'asset'
    headers = ['type_asset_id', 'asset_name', 
               'valuation_currency_id', 'price']

    list_querry.append(f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES \n')
    row_dict = {}

    all_assets = gen.get_all_assets()
    count_all_assets = len([asset for key, assets in all_assets.items() for asset in assets])

    for type_asset, sub_assets_key in enumerate(all_assets, 1):
        row_dict['type_asset_id'] = type_asset
        for num_asset, asset_key in enumerate(all_assets[sub_assets_key], 1):
            row_dict['asset_name'] = asset_key
            row_dict['valuation_currency_id'] = 1
            row_dict['price'] = round(float(all_assets[sub_assets_key][asset_key]), 4)
            row = '   ('
            for col in headers:
                row += f"'{row_dict[col]}', "
            row = row[0:-2] + f'),\n' 
            list_querry.append(row)
    list_querry[len(list_querry)-1] = f"{list_querry[len(list_querry)-1][:-2]};\n"
    list_querry.append('\n')

    # ============= Данные для таблицы common_portfolio ======================
    logging.debug('Данные для таблицы common_portfolio')

    table_name = 'common_portfolio'
    headers = ['brokerage_agreement_id', 'asset_id', 'asset_num']

    list_querry.append(f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES \n')
    row_dict = {}

    number_set = [i for i in range(1,501)]
    weight_set = [i**5 for i in range(500,0,-1)] 
    
    for br_agr_id in range(1, count_br_agr_ids + 1):
        br_agr_set = set()
        row_dict['brokerage_agreement_id'] = br_agr_id
        br_agr_assets = gen.get_assets()
        number_assets_for_cl = random.randint(1,50)
        br_agr_id_set = ['1', '2'] + random.sample(range(3, count_all_assets + 1), k=number_assets_for_cl)
        for asset_id in br_agr_id_set:
            row_dict['asset_id'] = asset_id
            row_dict['asset_num'] = random.choices(number_set, weights=weight_set, k=1)[0]
            if asset_id == '1': #рубли
                row_dict['asset_num'] *= 1000
            elif asset_id == '2': #доллары
                row_dict['asset_num'] *= 10
            row = '   ('
            for col in headers:
                row += f"'{row_dict[col]}', "
            row = row[0:-2] + f'),\n' 
            list_querry.append(row)

    list_querry[len(list_querry)-1] = f"{list_querry[len(list_querry)-1][:-2]};\n"
    list_querry.append('\n')

    # ============= Данные для таблицы type_trade ======================
    logging.debug('Данные для таблицы type_trade')

    table_name = 'type_trade'
    headers = ['type_trade_name']
    list_querry.append(f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES \n')
    row_dict = {}
    
    type_trades = ['Покупка', 'Продажа']
    for type_trade in type_trades:
        row_dict['type_trade_name'] = type_trade
        row = '   ('
        for col in headers:
            row += f"'{row_dict[col]}', "
        row = row[0:-2] + f'),\n'  
        list_querry.append(row)
    list_querry[len(list_querry)-1] = f"{list_querry[len(list_querry)-1][:-2]};\n"
    list_querry.append('\n')    

    # ============= Данные для таблицы trade =======================
    logging.debug('Данные для таблицы trade')

    table_name = 'trade'
    headers = ['trade_datetime', 'brokerage_agreement_id', 'asset_id', 
               'type_trade_id', 'asset_num', 'settlement_currency_id', 'price']

    list_querry.append(f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES \n')
    row_dict = {}
    # Пусть каждый 1000 аккаут совершает 10 операций в день, 
    # из остальных каждый 99 1 операцию в день,
    # остальные 1 операцию в месяц.
    # Рассмотрим только последний месяц
    today = datetime.datetime.now()


    def create_row_trade(row_dict, headers, trade_datetime):
        row_dict['asset_id'] = random.choice(range(1, count_all_assets + 1))
        row_dict['type_trade_id'] = random.randint(1,len(type_trades))
        row_dict['asset_num'] = random.choices(number_set, weights=weight_set, k=1)[0]//10+1
        row_dict['settlement_currency_id'] = '1'
        row_dict['trade_datetime'] = trade_datetime

        count = 0
        for type_asset, sub_assets_key in enumerate(all_assets, 1):
            for num_asset, asset_key in enumerate(all_assets[sub_assets_key], 1):
                count += 1
                if row_dict['asset_id'] == count:
                    row_dict['price'] = round(
                        float(all_assets[sub_assets_key][asset_key])*random.randint(50, 100)/100, 2)
                    break
        row = '   ('
        for col in headers:
            row += f"'{row_dict[col]}', "
        row = row[0:-2] + f'),\n'  
        list_querry.append(row)

    for cur_day in range(30, -1, -1):
        trade_baseday = today - datetime.timedelta(days=cur_day)
        for br_agr_id in range(1, count_br_agr_ids + 1): 
            row_dict['brokerage_agreement_id'] = br_agr_id
            if br_agr_id % 1000 == 0: 
                num_intervals = 10
                acc = 10
                intervals = []
                for i in range(10):
                    intervals.append(acc)
                    acc += 8/10
                t_segments_sec = [round((t +  + 8/10*random.random())*60*60) for t in intervals]
                t_segments_hour = [t // (60*60) for t in t_segments_sec]
                t_segments_min = [t % (60*60) // 60 for t in t_segments_sec]
                t_segments_sec = [t % 60 for t in t_segments_sec]
                for time in zip(t_segments_hour, t_segments_min, t_segments_sec):
                    trade_datetime = datetime.datetime(trade_baseday.year,
                                                        trade_baseday.month,
                                                        trade_baseday.day,
                                                        *time)
                    create_row_trade(row_dict, headers, trade_datetime)         
            elif  br_agr_id % 99 == 0:
                trade_datetime = datetime.datetime(trade_baseday.year,
                                                    trade_baseday.month,
                                                    trade_baseday.day,
                                                    random.randint(10, 17),
                                                    random.randint(0, 59),
                                                    random.randint(0, 59))
                create_row_trade(row_dict, headers, trade_datetime)
            elif cur_day == 15:
                trade_datetime = datetime.datetime(trade_baseday.year,
                                                    trade_baseday.month,
                                                    trade_baseday.day,
                                                    random.randint(10, 17),
                                                    random.randint(0, 59),
                                                    random.randint(0, 59))
                create_row_trade(row_dict, headers, trade_datetime)
    list_querry[len(list_querry)-1] = f"{list_querry[len(list_querry)-1][:-2]};\n"
    list_querry.append('\n')   

    # ============= Данные для таблицы signature_status =======================
    logging.debug('Данные для таблицы signature_status')

    table_name = 'signature_status'
    headers = ['signature_status_name']
    list_querry.append(f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES \n')
    row_dict = {}
    
    signature_status_name = ['Требуется подпись', 'Подпись не требуется', 'Подписано']

    for sig_st in signature_status_name:
        row_dict['signature_status_name'] = sig_st
        row = '   ('
        for col in headers:
            row += f"'{row_dict[col]}', "
        row = row[0:-2] + f'),\n'  
        list_querry.append(row)
    list_querry[len(list_querry)-1] = f"{list_querry[len(list_querry)-1][:-2]};\n"
    list_querry.append('\n') 

    # ============= Данные для таблицы main_document =======================
    logging.debug('Данные для таблицы main_document')

    table_name = 'main_document'
    headers = ['client_id', 
               'document_id',
               'signature_status_id',]
    list_querry.append(f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES \n')
    row_dict = {}
    len_sig_st = len(signature_status_name)
    for client_id in range(1, num_clients + 1):
        for doc_id in range(1, len(documents) + 1):
            row_dict['client_id'] = client_id
            row_dict['document_id'] = doc_id
            row_dict['signature_status_id'] = random.choice(range(1, len_sig_st + 1))
            row = '   ('
            for col in headers:
                row += f"'{row_dict[col]}', "
            row = row[0:-2] + f'),\n'  
            list_querry.append(row)

    list_querry[len(list_querry)-1] = f"{list_querry[len(list_querry)-1][:-2]};\n"
    list_querry.append('\n') 

    # ============= Данные для таблицы statement_type =======================
    logging.debug('Данные для таблицы statement_type')

    table_name = 'statement_type'
    headers = ['statement_type_name']
    list_querry.append(f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES \n')
    row_dict = {}
    statement_types = ['Вывод денежных средств с брокерского счета',
                    'Перевод денежных средств между брокерскими счетами',
                    'Перевод на брокерский счет',
                    'Возврат налогов и подача декларации',
                    'Данные о налогах',
                    'Заказ справки 2-НДФЛ',
                    'Заказ справки об убытках',
                    'Заявление на перерасчет НДФЛ',
                    'Заявление на возврат НДФЛ',
                    'Расчет налога по Эмитентам',
                    'Подтверждение затрат на приобретение ценных бумаг',
                    'Форма W-8BEN',
                    'Форма 1042S',
                    'Получение выписки со счета ДЕПО',
                    'Получение отчета об операциях по счету ДЕПО',
                    'Получение выписки из НРД',
                    'Журнал отчетов депозитария',
                    'Данные о налогах']
    for statement_type in statement_types:
        row_dict['statement_type_name'] = statement_type
        row = '   ('
        for col in headers:
            row += f"'{row_dict[col]}', "
        row = row[0:-2] + f'),\n'  
        list_querry.append(row)

    list_querry[len(list_querry)-1] = f"{list_querry[len(list_querry)-1][:-2]};\n"
    list_querry.append('\n') 

    # ============= Данные для таблицы client_statement =======================
    logging.debug('Данные для таблицы client_statement')

    table_name = 'client_statement'
    headers = ['statement_datetime', 
               'client_id',
               'statement_type_id',]
    list_querry.append(f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES \n')
    row_dict = {}

    today = datetime.datetime.today().date()

    def create_row_client_statement(row_dict, headers, len_st_type):
        row_dict['statement_type_id'] = random.randint(1,len_st_type)
        row = '   ('
        for col in headers:
            row += f"'{row_dict[col]}', "
        row = row[0:-2] + f'),\n'  
        list_querry.append(row)

    # Пусть каждый 1000 аккаут совершает 10 операций в день, 
    # из остальных каждый 99 1 операцию в день,
    # остальные 1 операцию в месяц.
    # Рассмотрим только последний 300 дней
    len_st_type = len(statement_types)
    for cur_day in range(300, -1, -1):
        row_dict['statement_datetime'] = today - datetime.timedelta(days=cur_day)
        for client_id in range(1, num_clients + 1): 
            row_dict['client_id'] = client_id
            
            if br_agr_id % 1000 == 0:
                for i in range(10):
                    create_row_client_statement(row_dict, headers, len_st_type)         
            elif  br_agr_id % 99 == 0:
                create_row_client_statement(row_dict, headers, len_st_type)
            elif cur_day % 27 == 0:
                create_row_client_statement(row_dict, headers, len_st_type)
    list_querry[len(list_querry)-1] = f"{list_querry[len(list_querry)-1][:-2]};\n"
    list_querry.append('\n') 
         

    f.write(''.join(list_querry))




    


