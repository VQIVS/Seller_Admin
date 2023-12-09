import argparse
from scripts.model import UserManager
from scripts.functions import create_connection, delete_connection, get_save_sublink, get_access_token


class CustomHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog):
        super().__init__(prog, max_help_position=30, width=100)

    def add_argument(self, action):
        if action.option_strings:
            self._add_item(self._format_action, [action])

    def _format_action(self, action):
        if action.dest == 'action':
            return ""
        return super()._format_action(action)


def main():
    parser = argparse.ArgumentParser(
        description='User Management CLI',
        formatter_class=CustomHelpFormatter
    )

    parser.add_argument('action', choices=['create', 'delete', 'sublink'],
                        help='Action to perform: create, delete, sublink')

    parser.add_argument('--start', type=int, help='Starting user number')
    parser.add_argument('--end', type=int, help='Ending user number')
    parser.add_argument('--data', help='Data for user creation')

    args = parser.parse_args()

    user_obj = UserManager()

    get_access_token(user_obj)  # Run get_token before every other command

    if args.action == 'create':
        start = args.start or int(input('Enter the starting user number: '))
        end = args.end or int(input('Enter the ending user number: '))
        data = args.data or input('Enter the data for user creation: ')
        create_connection(user_obj, start, end, data)
    elif args.action == 'sublink':
        start = args.start or int(input('Enter the starting user number: '))
        end = args.end or int(input('Enter the ending user number: '))
        get_save_sublink(user_obj, start, end)
    elif args.action == 'delete':
        start = args.start or int(input('Enter the starting user number: '))
        end = args.end or int(input('Enter the ending user number: '))
        delete_connection(user_obj, start, end)


if __name__ == '__main__':
    main()
