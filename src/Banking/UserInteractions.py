class UserInteractions:

    def get_string(question):
        print(question)
        answer = input()
        return answer

    def get_integer(question):
        while 'answer' not in locals():
            try:
                print(question)
                answer = int(input())
                return answer
            except ValueError:
                print("The response must be an integer.  Please try again.")