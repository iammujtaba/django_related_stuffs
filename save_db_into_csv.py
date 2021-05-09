import os
from django.apps import apps
from csv import DictWriter


def write_in_csv_table_wise(model,columns):
    table_name = model.__name__
    print(f"started writing {table_name} table data into csv file")
    print("Current working directory",os.getcwd())
    with open(f"{table_name}.csv",'w',newline='') as file:
        writer = DictWriter(file,fieldnames=columns)
        writer.writeheader()
        values = model.objects.all()
        for val in values:
            row_data = [str(getattr(val,column,None)) for column in columns]
            writer.writerow(dict(zip(columns,row_data)))
    print(f"finished writing {table_name} table data into csv file")

def write_db_into_csv(table_names=[]):
    model_list = apps.get_models()
    for model in model_list:
        columns = []
        for django_field in model._meta.get_fields():
            columns.append(django_field.name)
        if not table_names or model.__name__ in table_names:
            write_in_csv_table_wise(model,columns)

if __name__=="__main__":
    write_db_into_csv()