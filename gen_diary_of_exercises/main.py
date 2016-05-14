import sys
import datetime
import random
import argparse
from termcolor import colored
from gen_diary_of_exercises import generator


MAX_NUM_OF_EXERCISES_PER_DAY = len(generator.EXERCISE_TYPES)


def print_exercises_per_day(date):
    if type(date) != datetime.datetime:
        raise ValueError("Date is not datetime type!")
    count_ex = random.randint(0, MAX_NUM_OF_EXERCISES_PER_DAY)
    if count_ex == 0:
        return
    print(colored("# " + date.strftime("%d %B %Y"), "blue"))
    # Убираем повторы: храним уже распечатанные типы упражнений
    ex_types = set()
    for i in range(count_ex):
        while True:
            ex = generator.Exercise.random()
            if ex.exercise_type not in ex_types:
                ex_types.add(ex.exercise_type)
                print("* ", end="")
                print(ex)
                break


def real_main(args):
    start_date = args.start_date
    finish_date = args.finish_date
    step = datetime.timedelta(days=1)
    while start_date < finish_date:
        print_exercises_per_day(date=start_date)
        start_date += step


def valid_date(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def main():
    parser = argparse.ArgumentParser(prog="gen_diary_of_exercises")
    parser.add_argument(

        '-sd', '--start-date',
        help="The Start Date - format YYYY-MM-DD",
        required=True,
        type=valid_date
    )
    parser.add_argument(
        '-fd',
        '--finish-date',
        help="The Finish Date - format YYYY-MM-DD",
        required=True,
        type=valid_date
    )
    real_main(parser.parse_args(sys.argv[1:]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
