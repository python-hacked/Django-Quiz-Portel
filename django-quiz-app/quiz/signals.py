import django.dispatch

csv_uploaded = django.dispatch.Signal()

def my_function(user, csv_files):
    csv_uploaded.send(sender=None, user=user, csv_file_list=csv_files)
