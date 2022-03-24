class UserInteractions:

    def get_string(question):
        print(question)
        answer = input()
        return answer

    def get_string_in_items(question, items):
        answer = 'w'
        while answer not in items:
            print(question)
            answer = input().lower()
        return answer

    def get_integer(question):
        while 'answer' not in locals():
            try:
                print(question)
                answer = int(input())
                return answer
            except ValueError:
                print("The response must be an integer.  Please try again.")

    def get_float(question):
        while 'answer' not in locals():
            try:
                print(question)
                answer = float(input())
                return answer
            except ValueError:
                print("The response must be a float.  Please try again.")

    def get_item_by_id(obj_list, id):
        for item in obj_list:
            if item.id == id:
                return item
        return -1

    def get_valid_from_list(obj_list):
        for item in obj_list:
            print(str(item))
        print("Which ID would you like to use?")
        id = -1
        while id==-1:
            try:
                id = int(input())
            except ValueError:
                print("The id must be a number.  Please try again or enter 0 if you wish to cancel account creation.")

        if id == 0:
            return -1
        else:
            return id
