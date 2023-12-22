from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'Ivanov', 'first_name': 'Ivan'},
            {'last_name': 'Petrov', 'first_name': 'Petr'},
            {'last_name': 'Srmenov', 'first_name': 'Semen'},
            {'last_name': 'Sidorov', 'first_name': 'Nikolay'},
            {'last_name': 'Tolstoy', 'first_name': 'Lev'},
            {'last_name': 'Loghkin', 'first_name': 'Slava'},
            {'last_name': 'Karpin', 'first_name': 'Adam'},
        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)    # Каждый раз при исполнении метода create, идет обращение
        #                                               #     к базе, что очень долго при больших объемах

        # Лучше сделать пакетное добавление, чтобы к базе обратиться всего один раз, для записи всего пакета

        student_for_create = []
        for student_item in student_list:
            student_for_create.append(
                Student(**student_item)
            )
        # print(student_for_create)
        Student.objects.bulk_create(student_for_create) # с помощью команды bulk_create  мы можем добавлять пакет
