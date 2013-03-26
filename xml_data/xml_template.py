# -*- coding: utf-8 -*-

import json
import MySQLdb

def gen_field_sql(field_name,field_type):
    sql = ''
    if field_type == 'auto':
        sql = field_name+" int not null auto_increment primary key"
    elif field_type == 'int':
        sql = field_name+" int not null default 0"
    elif field_type.find('varchar') == 0:
        sql = field_name+" "+field_type+" not null default ''"
    elif field_type == 'float':
        sql = field_name+" float not null default 0"
    elif field_type == 'text':
        sql = field_name+" text not null default ''"
    elif field_type == 'tinyint':
        sql = field_name+" tinyint not null default 0"
    elif field_type == 'date':
        sql = field_name+" date not null default ''"
    elif field_type == 'timestamp':
        sql = field_name+" timestamp not null default ''"
    else:
        raise VauleError, 'invalid field_type'
    return sql

def template_to_sql(json_template):
    tables_sql = {}
    for table_item in json_template.items():
        table_name = 't_'+table_item[0].encode('utf-8')
        fields_sql = []
        for field_item in table_item[1].items():
            field_name = field_item[0].encode('utf-8')
            field_type = field_item[1].encode('utf-8')
            field_sql = gen_field_sql(field_name,field_type)
            fields_sql.append(field_sql)
        table_sql = "create table "+table_name+"("+",".join(fields_sql)+");"
        tables_sql[table_name] = table_sql
    return tables_sql 
            

def create_mysql_table(mysql_connect,tables_sql):
    mysql_connect.query("show tables")
    result = mysql_connect.store_result()
    exist_tables = []
    for i in range(result.num_rows()):
        exist_tables.append(result.fetch_row()[0][0])

    for table in tables_sql.items():
        if table[0] not in exist_tables:
            mysql_connect.query(table[1])
    

def init_template(mysql_connect,str_template):
    json_object = json.loads(str_template)
    tables_sql = template_to_sql(json_object)
    create_mysql_table(mysql_connect,tables_sql)
    

if __name__ == "__main__":
    mysql_connect = MySQLdb.connect(user='root',passwd='sd-9898w',db='showtest')
    mysql_connect.query("set names utf8")
    str_template = """{
"video_data":{
"id":"auto",
"video_id":"int",
"daquan_id":"int",
"video_type":"varchar(10)",
"title":"varchar(255)",
"img_link":"text",
"year":"int",
"area":"varchar(50)",
"score":"float",
"score_num":"int",
"type":"varchar(255)",
"brief_comment":"varchar(255)",
"comment":"text",
"resolution":"varchar(50)",
"director":"varchar(255)",
"actor":"varchar(255)",
"play_num":"int",
"download":"tinyint",
"download_num":"int",
"num_total":"int",
"num_current":"int",
"date_current":"date",
"content_provider":"varchar(50)",
"is_cancel":"tinyint",
"is_valid":"tinyint",
"invalid_msg":"varchar(255)",
"has_update":"tinyint",
"modify_ts":"timestamp",
"insert_ts":"timestamp",
"alias_title":"varchar(255)",
"is_crawl":"tinyint",
"vmovie":"tinyint",
"free_status":"tinyint",
"free_duration":"int",
"ori_price":"int",
"price":"int",
"price_text":"varchar(255)"
},
"play_data":{
"id":"int",
"title":"varchar(255)",
"brief_comment":"varchar(255)",
"number":"int",
"update_date":"date",
"language":"tinyint",
"play_link":"text",
"flash_play_link":"text",
"sub_img_link":"text",
"sub_number":"int"
}
}"""
    init_template(mysql_connect,str_template)         
